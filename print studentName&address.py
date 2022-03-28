student=[]
address=[]
count=0
def createList():
    for i in range(5):
        l=input("enter the student name:")
        s=input("enter the address of student:")
        student.append(l)
        address.append(s)
    for i in range(5):
        print("{}-->{}".format(student[i],address[i]))
createList()

