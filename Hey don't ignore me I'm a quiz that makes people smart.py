score=0
#Question 1
print("welcome to random quiz")

print("Question1:")
print("what IBM stand for?")
print("A.International Big Machines")
print("B.International Business Machines")
print("C.I Beat Microsoft")
answer=input("choose A,B,C?:")
if answer.upper()=="A":
    print("incorrect!")
    score += 1
elif answer.lower()=="b":
    print("incorrect your a good patootie!")
elif answer.lower()=="c":
    print("nah are serious rn bro")
else:
        print("pick at the selected letters A,B,C")
 
  #Question 2  
print("Question 2:")
answer=input("sigma or gigachad:")
if answer.lower()=="gigachad":
    print("good boy~")
    score += 1
elif answer.lower()=="sigma":
    print("you may need 2-3 years dagestan")
else:
        print("pick at the selected question!")
       
print("Final score:", score, "/2")
