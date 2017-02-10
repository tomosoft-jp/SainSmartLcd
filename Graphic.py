#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ST7735 import ST7735


class Graphic:
    def __init__(self, pst7735):
        self._st7735 = pst7735

    def drawline(self, x0p, y0p, x1p, y1p, color):
        if (x0p >= self._st7735.width) or (y0p >= self._st7735.height):
            print " drawline x0, y0 Range error"
            return
        if (x1p >= self._st7735.width) or (y1p >= self._st7735.height):
            print " drawline x1, y1 Range error"
            return
        x0 = x0p
        y0 = y0p
        x1 = x1p
        y1 = y1p

        steep = abs(y1 - y0) > abs(x1 - x0)
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        dx = x1 - x0
        dy = abs(y1 - y0)
        err = dx / 2
        ystep = -1
        if y0 < y1:
            ystep = 1
        for xx0 in range(x0, x1):
            if steep:
                self._st7735.dot(y0, xx0, color)
            else:
                self._st7735.dot(xx0, y0, color)
            err -= dy
            if err < 0:
                y0 += ystep
                err += dx

    def drawrect(self, x, y, w, h, color):
        if (x >= self._st7735.width) or (y >= self._st7735.height):
            print " drawrect x, y Range error"
            return
        if ((x + w) >= self._st7735.width) or ((y + h) >= self._st7735.height):
            print " drawrect w, h Range error"
            return
        self.drawline(x, y, x + w - 1, y, color)
        self.drawline(x, y + h - 1, x + w - 1, y + h - 1, color)
        self.drawline(x, y, x, y + h - 1, color)
        self.drawline(x + w - 1, y, x + w - 1, y + h - 1, color)

    def fillrect(self, x, y, w, h, color):
        if (x >= self._st7735.width) or (y >= self._st7735.height):
            print " fillrect x, y Range error"
            return
        # print " fillrect:{0:X}".format(x)
        if (x + w - 1) >= self._st7735.width:
            w = self._st7735.width - x
        if (y + h - 1) >= self._st7735.height:
            h = self._st7735.height - y
        for xx in range(x, x + w):
            for yy in range(y, y + h):
                self._st7735.dot(xx, yy, color)

    def fillscreen(self, color):
        self.fillrect(0, 0, self._st7735.width, self._st7735.height, color)

    def drawcircle(self, x0, y0, r, color):
        f = 1 - r
        ddf_x = 1
        ddf_y = -2 * r
        x = 0
        y = r
        self._st7735.dot(x0, y0 + r, color)
        self._st7735.dot(x0, y0 - r, color)
        self._st7735.dot(x0 + r, y0, color)
        self._st7735.dot(x0 - r, y0, color)

        while x < y:
            if f >= 0:
                y -= 1
                ddf_y += 2
                f += ddf_y

            x += 1
            ddf_x += 2
            f += ddf_x

            self._st7735.dot(x0 + x, y0 + y, color)
            self._st7735.dot(x0 - x, y0 + y, color)
            self._st7735.dot(x0 + x, y0 - y, color)
            self._st7735.dot(x0 - x, y0 - y, color)
            self._st7735.dot(x0 + y, y0 + x, color)
            self._st7735.dot(x0 - y, y0 + x, color)
            self._st7735.dot(x0 + y, y0 - x, color)
            self._st7735.dot(x0 - y, y0 - x, color)

    def drawcirclehelper(self, x0, y0, r, cornername, color):
        f = 1 - r
        ddf_x = 1
        ddf_y = -2 * r
        x = 0
        y = r

        while x < y:
            if f >= 0:
                y -= 1
                ddf_y += 2
                f += ddf_y

            x += 1
            ddf_x += 2
            f += ddf_x
            if cornername and 0x4:
                self._st7735.dot(x0 + x, y0 + y, color)
                self._st7735.dot(x0 + y, y0 + x, color)

            if cornername and 0x2:
                self._st7735.dot(x0 + x, y0 - y, color)
                self._st7735.dot(x0 + y, y0 - x, color)

            if cornername and 0x8:
                self._st7735.dot(x0 - y, y0 + x, color)
                self._st7735.dot(x0 - x, y0 + y, color)

            if cornername and 0x1:
                self._st7735.dot(x0 - y, y0 - x, color)
                self._st7735.dot(x0 - x, y0 - y, color)

    def fillcirclehelper(self, x0, y0, r, cornername, delta, color):
        f = 1 - r
        ddf_x = 1
        ddf_y = -2 * r
        x = 0
        y = r

        while x < y:
            if f >= 0:
                y -= 1
                ddf_y += 2
                f += ddf_y

            x += 1
            ddf_x += 2
            f += ddf_x

            if cornername & 0x1:
                self.drawline(x0 + x, y0 - y, x0 + x, y0 - y + (2 * y + 1 + delta), color)
                self.drawline(x0 + y, y0 - x, x0 + y, y0 - x + (2 * x + 1 + delta), color)

            if cornername & 0x2:
                self.drawline(x0 - x, y0 - y, x0 - x, y0 - y + (2 * y + 1 + delta), color)
                self.drawline(x0 - y, y0 - x, x0 - y, y0 - x + (2 * x + 1 + delta), color)

    def fillcircle(self, x0, y0, r, color):
        self.drawline(x0, y0 - r, x0, y0 - r + (2 * r + 1), color)
        self.fillcirclehelper(x0, y0, r, 3, 0, color)


if __name__ == "__main__":
    ST7735_TFTWIDTH = 128
    ST7735_TFTHEIGHT = 160

    ST7735_BLACK = 0x000000
    ST7735_BLUE = 0x0000FF
    ST7735_RED = 0xFF0000
    ST7735_GREEN = 0x008000
    ST7735_CYAN = 0x00FFFF
    ST7735_MAGENTA = 0xFF00FF
    ST7735_YELLOW = 0xFFFF00
    ST7735_WHITE = 0xFFFFFF

    st7735 = ST7735(ST7735_TFTWIDTH, ST7735_TFTHEIGHT)
    graphic = Graphic(st7735)
    try:
        graphic.fillscreen(ST7735_RED)
        graphic.drawline(10, 10, ST7735_TFTWIDTH - 10, ST7735_TFTHEIGHT - 10, ST7735_BLACK)
        graphic.drawrect(0, 40, 20, 40, ST7735_CYAN)
        graphic.fillrect(80, 60, 40, 20, ST7735_YELLOW)
        graphic.drawcircle(64, 40, 15, ST7735_MAGENTA)
        graphic.fillcircle(64, 120, 30, ST7735_GREEN)
        st7735.sendbuf()

    except KeyboardInterrupt:
        print '\nbreak'
        # GPIO.cleanup()
