class Employee:
	def basicpay(self):
		self.r=100000
		print(self.r)
class Freshers:
	def total(self,basic):
		basic.basicpay()
e=Employee()
f=Freshers()
Freshers.total(f,e)
print('or')
f.total(e)