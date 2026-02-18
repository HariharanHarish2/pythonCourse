score=int(input())
if(score<35):
    print("poor Student")
elif(score>35 and score<70):
    print("Average Student")
elif(score>70 and score<100):
    print("good Student")
else:
    print("Invalid Syntax")
