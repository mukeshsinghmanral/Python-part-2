import sublime
import sublime_plugin
from time import sleep
from threading import *
class Hello(Thread):
	def run(self):
		for i in range(6):
			print('hello')
			sleep(1)
class Hi(Thread):
	def run(self):
		for i in range(6):
			print('hi')
			sleep(1)
a=Hello()
b=Hi()
a.start()
sleep(0.2)
b.start()
a.join()
b.join()
print('bye')

