class Company:
	def __init__(self,no_emp,sal,exp):
		self.no_emp=no_emp
		self.sal=sal
		self.exp=exp
	def __add__(self, other):
		total_emp=self.no_emp+other.no_emp
		total_sal=self.sal+other.sal
		total_exp=self.exp+other.exp
		e3=Company(total_emp,total_sal,total_exp)
		print(e3.no_emp,e3.sal,e3.exp)
e1=Company(450,120000,10)
e2=Company(150,450000,20)
e3=e1+e2