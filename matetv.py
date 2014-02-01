#!/usr/bin/env python
from PyQt4 import QtCore, QtGui, Qt, QtNetwork
from PyQt4.QtGui import QApplication, QLineEdit, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QFileDialog
from gui import Ui_Form

import struct
import time
import sys
import cv
import socket


RESX = 40
RESY = 16
IP = "matelight.cbrp3.c-base.org"
PORT = 1337
KAMERA_NR = 0

TOTAL_PIXELS = RESX * RESY
FRAMES_PER_SECOND = 10
TIME_BETWEEN_FRAMES = 1.0 / FRAMES_PER_SECOND
INTERFACE_UDP = 0

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.pushButton_browse, QtCore.SIGNAL("clicked()"), self.cmd_browse_file)
        QtCore.QObject.connect(self.ui.pushButton_send_image, QtCore.SIGNAL("clicked()"), self.cmd_send_image)
        QtCore.QObject.connect(self.ui.pushButton_stream_webcam, QtCore.SIGNAL("clicked()"), self.cmd_stream_webcam)
        QtCore.QObject.connect(self.ui.horizontalSlider_fps, QtCore.SIGNAL("valueChanged(int)"), self.cmd_fps_changed)
        QtCore.QObject.connect(self.ui.checkBox_equalize, QtCore.SIGNAL("clicked(bool)"), self.cmd_equalize_changed)
        QtCore.QObject.connect(self.ui.verticalSlider_red, QtCore.SIGNAL("valueChanged(int)"), self.cmd_red_slider_changed)
        QtCore.QObject.connect(self.ui.verticalSlider_green, QtCore.SIGNAL("valueChanged(int)"), self.cmd_green_slider_changed)
        QtCore.QObject.connect(self.ui.verticalSlider_blue, QtCore.SIGNAL("valueChanged(int)"), self.cmd_blue_slider_changed)
        QtCore.QObject.connect(self.ui.verticalSlider_gamma, QtCore.SIGNAL("valueChanged(int)"), self.cmd_gamma_slider_changed)
        QtCore.QObject.connect(self.ui.verticalSlider_brightness, QtCore.SIGNAL("valueChanged(int)"), self.cmd_brightness_slider_changed)


        # Network init
        self.sock = QtNetwork.QUdpSocket()
        self.sock.bind(QtNetwork.QHostAddress.Any, PORT)
        self.connect(self.sock, QtCore.SIGNAL("readyRead()"), self.on_recv_udp_packet)

        self.image = None
        self.debug_image = None
        self.streaming = False
        self.threshold = 128
        self.equalize = False
        self.fps = FRAMES_PER_SECOND
        self.time_between_frames = TIME_BETWEEN_FRAMES
        self.cam = cv.CaptureFromCAM(KAMERA_NR)

        self.max_red   = 100
        self.max_green = 100
        self.max_blue  = 100
        self.max_gamma = 200
        self.max_brightness = 25


    def cv_load_image(self, file_path):
        image = cv.LoadImage(file_path)
        conv_img = self.cv_get_converted_image_for_matelight(image)
        return conv_img

    def convert_img_matrix_to_matelight(self, mat):
        bitstring = []

        for row in xrange(mat.rows):
            for column in xrange(mat.cols):
                # convert 24 bit to 12 bit 4:4:4 (rounding up using 0.5 + x trick)
                red   = int(mat[row, column][2] * self.max_red   / 100.0)
                green = int(mat[row, column][1] * self.max_green / 100.0)
                blue  = int(mat[row, column][0] * self.max_blue  / 100.0)

                bitstring.extend(struct.pack('BBB', red, green, blue))

        return bytearray(bitstring)

    def cv_resize_and_grayscale(self, input_image, threshold, doEqualize):
        image = cv.CreateImage((input_image.width, input_image.height), 8, 1)
        cv.CvtColor(input_image, image, cv.CV_BGR2GRAY)
    
        if doEqualize:
            cv.EqualizeHist(image, image) # equalize the pixel brightness
        cv.Threshold(image, image, threshold, 255, cv.CV_THRESH_OTSU) # convert to black / white image

        image_resized = cv.CreateImage( (RESX, RESY), image.depth, image.channels) # resize to fit into r0ket display
        cv.Resize(image, image_resized, cv.CV_INTER_NN)

        return image_resized


    # GUI events
    def cmd_load_image(self):
        file_path = str(self.ui.lineEdit_file_path.text())
        self.image = self.cv_load_image(file_path)
        print "image loaded!"

    def cmd_stream_webcam(self):
        end_time = 0
        counter = 1
        
        while True:
            frame = cv.QueryFrame(self.cam)
            c = cv.WaitKey(1)
        
            if c == 27: # esc
                return

            g = cv.CreateImage(cv.GetSize (frame), cv.IPL_DEPTH_8U, frame.channels)
            gr = frame[128: 384, 0: 640] # Crop from x, y, w, h -> 100, 200, 100, 200
            ml = cv.CreateImage((40, 16), cv.IPL_DEPTH_8U, frame.channels)
            cv.Resize(gr, ml)
            cv.ShowImage("w1", gr)
            
            if time.time() > end_time:
               end_time = time.time() + self.time_between_frames
               #self.cmd_send_image(ml, 0.25, 2)
               self.cmd_send_image(ml, self.max_brightness, self.max_gamma)
               
            print counter
            counter += 1

    def cmd_send_image(self, image, brightness, gamma):
        mg_mat = cv.GetMat(image)
        ml_data = self.convert_img_matrix_to_matelight(mg_mat) + "\00\00\00\00"
        data_c = bytearray([int(((x / 255.0) ** (gamma / 100.0)) * 255 * (brightness / 100.0)) for x in list(ml_data)])
        #data_c = bytearray([int(((x / 255.0) ** gamma) * 255 * brightness) for x in list(ml_data)])

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(data_c, (IP, PORT))

    def cmd_fps_changed(self, value):
        self.fps = value
        self.time_between_frames = 1.0 / self.fps

    def cmd_red_slider_changed(self, value):
        self.max_red = value
        print "red slider changed to %d %%" % value

    def cmd_green_slider_changed(self, value):
        self.max_green = value
        print "green slider changed to %d %%" % value

    def cmd_blue_slider_changed(self, value):
        self.max_blue = value
        print "blue slider changed to %d %%" % value

    def cmd_gamma_slider_changed(self, value):
        self.max_gamma = value
        print "gamma slider changed to %d %%" % value

    def cmd_brightness_slider_changed(self, value):
        self.max_brightness = value
        print "brightness slider changed to %d %%" % value

        
    def cmd_equalize_changed(self, state):
        self.equalize = state
        print state

    def cmd_browse_file(self):
        self.ui.lineEdit_file_path.setText(QFileDialog.getOpenFileName())

    def send_udp_packet(self, payload):
        self.sock.writeDatagram(payload, QtNetwork.QHostAddress(IP), PORT)


    def on_recv_udp_packet(self):
        print "UDP packet received but ignored. TODO: implement handler.\n"

def main():
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()