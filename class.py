class student:
	name=raw_input("enter yoyr name ")
	roll_no=input("Enter your roll no :")
	score=input("enter the score")
	

	def grades(self):
		if(self.score>80):
			print("got 1st class A grade")
		elif(self.score>60):
			print("got B grade")
		elif(self.score>50):
			print("got C grade")
		else:
			print("got F grade")

function1=student()
print(student.score)

function1.grades()



