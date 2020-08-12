class Student:
	school='st lawrence sec school'
	def __init__(self,ram,cpu):
		self.r=ram
		self.c=cpu
	def details(self,name,roll_no):
		self.n=name
		self.rn=roll_no
		print('name:',self.n,'roll_no:',self.rn)
		print(self.r,self.c)
	@classmethod
	def classs(cls):
		cls.school='AMITY'
s1=Student(8,'i5')
s2=Student(16,'ryzen5')
print(s1.school)
print(s2.school)
s1.details('mukesh_manral',46)
s2.details('viru',43)
print(s1.school)
print(Student.school)
print(s2.school)
print(Student.school)
Student.classs()
print(Student.school)
print(s1.school)
print(s2.school)

