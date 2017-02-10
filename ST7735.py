#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import spidev  # sudo pip install spidev
import time


class ST7735:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.BMPData = 0xf000 * [0xfffff]

        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 16000000
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(24, GPIO.OUT)
        GPIO.setup(25, GPIO.OUT)

        # reset
        GPIO.output(25, False)
        time.sleep(0.1)
        GPIO.output(25, True)
        time.sleep(0.1)

        self.write_cmd(0x11)
        time.sleep(0.12)
        # フレームレート設定
        self.write((0xB1, 0x01, 0x2C, 0x2D))
        self.write((0xB2, 0x01, 0x2C, 0x2D))
        self.write((0xB3, 0x01, 0x2C, 0x2D, 0x01, 0x2C, 0x2D))
        # 液晶反転設定
        self.write((0xB4, 0x07))
        # 電源設定（PWCTR1～3）
        self.write((0xC0, 0xA2, 0x02, 0x84))
        self.write((0xC1, 0xC5))
        self.write((0xC2, 0x0A, 0x00))
        self.write((0xC3, 0x8A, 0x2A))
        self.write((0xC4, 0x8A, 0xEE))
        self.write((0xC5, 0x0E))
        self.write_cmd(0x20)
        # ガンマ設定
        self.write(
            (0xE0, 0x0F, 0x1A, 0x0F, 0x18, 0x2F, 0x28, 0x20, 0x22, 0x1F, 0x1B, 0x23, 0x37, 0x00, 0x07, 0x02, 0x10))
        self.write(
            (0xE1, 0x0F, 0x1B, 0x0F, 0x17, 0x33, 0x2C, 0x29, 0x2E, 0x30, 0x30, 0x39, 0x3F, 0x00, 0x07, 0x03, 0x10))
        self.write_cmd(0x29)
        self.write_cmd(0x13)
        # 液晶描画方向設定 縦長 0x40 横長0x20
        self.write((0x36, 0x40))
        # 描画エリア設定 0～BMPのサイズ
        self.write((0x2A, 0x00, 0x00, 0x00, self.width))
        self.write((0x2B, 0x00, 0x00, 0x00, self.height))
        self.write((0x3A, 0x06))
        # 表示RAM転送モードに設定
        self.write_cmd(0x2C)

    def write_cmd(self, cmd):
        GPIO.output(24, False)  # RS=0:コマンドレジスタ指定
        self.spi.xfer2([cmd])

    def write_data(self, data):
        GPIO.output(24, True)  # RS=1:データレジスタ指定
        self.spi.xfer2([data])

    def write(self, cmd):
        if len(cmd) == 0:
            return
        GPIO.output(24, False)  # RS=0:コマンドレジスタ指定
        self.spi.xfer2([cmd[0]])
        GPIO.output(24, True)  # RS=1:データレジスタ指定
        self.spi.xfer2(list(cmd[1:]))

    def dot(self, x, y, color):
        pos = (x + (y * self.width)) * 3
        self.BMPData[pos] = (color & 0xff0000) >> 16
        self.BMPData[pos + 1] = (color & 0xff00) >> 8
        self.BMPData[pos + 2] = color & 0xff

    def sendbuf(self):
        for i in range(0xf000):
            self.write_data(self.BMPData[i])
            # print "{0:X}".format(self.BMPData[i]),
