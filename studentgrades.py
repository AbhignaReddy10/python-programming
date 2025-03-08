#program to print the student grade
obtained_marks= int(input("enter the obtained marks(out of 100)"))
marks= int(obtained_marks)
if marks>= 90:
    print("the obtained grade is:A")
elif marks>=80:
    print("the obtained grade is :B")
elif marks>= 70:
    print("the obtained grade is: C")
elif  marks>= 60:
    print("the obtained grade is:D")
elif marks>= 50:
    print("the  obtained grade is: E")
elif marks>= 40:
    print("OOPS! you failed")
