# !/usr/bin/env python
#  -*- coding: utf-8 -*-

class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memery = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        return '\n'.join([self.memery, self.hdd, self.gpu])


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('AF23385193')

    def configure_memory(self, amount):
        self.computer.memery = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        self.builder.configure_gpu(gpu)
        self.builder.configure_hdd(hdd)
        self.builder.configure_memory(memory)

    @property
    def computer(self):
        return self.builder.computer


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd='500', memory='8', gpu='GeForce GTX 650 Ti')
    print engineer.computer


if __name__ == '__main__':
    main()
