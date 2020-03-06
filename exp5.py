class student:
	def __init__(self,roll_no,name,score):
		self.name=name
		self.roll_no=roll_no
		self.score=score
	def grade(self):
		if self.score>=80:
			print("A grade")
		elif self.score<80 and self.score>=60:
			print("B grade")
		elif self.score>=50 and self.score<60:
			print("C grade")
		else :
			print("F grade")

s1=student(8691,"rahul",76)
s1.grade()

