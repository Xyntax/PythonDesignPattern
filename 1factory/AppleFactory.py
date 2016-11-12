# !/usr/bin/env python
#  -*- coding: utf-8 -*-
MINI14 = '1.4GHz MAC Mini'


class AppleFactory:
    class MacMini14:  # 采用内部类禁止其直接实例化
        def __init__(self):
            self.memory = '4'
            self.hdd = '500'
            self.gpu = 'Intel HD Graphics 5000'

        def __str__(self):
            return '\n'.join(['Mac mini', self.memory, self.hdd, self.gpu])

    class MacPro:
        pass

    def build_computer(self, model):
        if model == MINI14:
            return self.MacMini14()
        else:
            print 'model not found'


if __name__ == '__main__':
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI14)
    print mac_mini
