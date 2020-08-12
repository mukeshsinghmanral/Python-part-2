class Student:
	school='NIT'
	def __init__(self,ram,cpu):
		self.r=ram
		self.c=cpu
	def details(self,name,roll_no):
		self.n=name
		self.rn=roll_no
		self.school='NIT Trichy'
		print('name:',self.n,'roll_no:',self.rn)
		print(self.r,self.c,self.school)
s1=Student(8,'i5')
s2=Student(16,'ryzen5')
print(s1.school)
print(s2.school)
print(Student.school)
Student.school='amity'
print(s1.school)
print(s2.school)
print(Student.school)