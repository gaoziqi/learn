from multiprocessing import Process
from random import randint
import os

def fish():
	while True:
		os.system("adb shell input tap 550 1490")

def helper():
	while True:
		os.system("adb shell input tap %d %d" % (randint(500, 600), randint(950, 1050)))


if __name__ == '__main__':
	p = Process(target = fish)
	p1 = Process(target = helper)
	p.start()
	p1.start()
	p.join()
	p1.join()