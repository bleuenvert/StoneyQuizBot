import time

A1 = [ "D", "d" ]
A2 = ["A", "a"  ]
A3 = ["C", "c"  ]
A4 = ["A", "a"  ]
A5 = ["D", "d"  ]
A6 = ["B", "b"  ]
A7 = ["C", "c"  ]
A8 = ["B", "b"  ]
A9 = ["C", "c"  ]
A10 = ["C", "c" ]
correct = 0 #Storing the correct answers
total_questions = 0 #storing number of question (for extendability)

name = input ("Hello, I am StoneyQuizbotAlpha, what is your name?\n") #Storing the user's name

print("Nice to meet you " + name +"! \n Note that: for nasals a `^` symbol will be put after the vowel; for voiced interdental fricative dh will be used" + "\n Let's get started!")
#I need to find some way of including the orthography of stoney. Might need to find a module that builds a graphical interface. (Maybe that way latex symbols could be used?)
time.sleep(2)

print ("Question 1\n Translate: Wapta ze tha^ch")
print (" A:This river (near the speaker) is white \n B:That white river (near speaker) \n C:That white river(near listener) \n D:That river (near the listener) is white ")
total_questions += 1 #adds a counter for each question
choice = input(">>> ")
if choice in A1:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

print ("Question 2\n Translate: A'an ne ana^yarapta^ch")
print (" A:You are listening to this(near speaker) crow \n B:I am listening to that(near listener) crow\n C:I am listening to this (near speaker) crow \n D:You are listening to that(near listener) crow ")
total_questions += 1
choice = input(">>> ")
if choice in A2:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

print ("Question 3\n Translate: Me, I'm walking")
print (" A:Niye ma^wani^ch \n B:Iye ma^wani^ch \n C:Miye ma^wani^ch \n D:I^ygi^ye ma^nani^ch ")
total_questions += 1
choice = input(">>> ")
if choice in A3:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

print ("Question 4\n Translate: ta ze i^sti^ma^ch")
print (" A:That moose (near the listener) is sleeping \n B:That bear(ntl) is sleeping \n C:That dog (ntl) is sleeping \n D:That squirrel (ntl) is sleeping ")
total_questions += 1
choice = input(">>> ")
if choice in A4:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

print ("Question 5\n translate: you all are playing drums")
print (" A:Gamubi yihotuch \n B:Gamubi nihotuch \n C:Gamubi yihotubich \n D: Gamubi nihotubich")
total_questions += 1
choice = input(">>> ")
if choice in A5:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

print ("Question 6\n Translate: mu thich")
print (" A:Yellow thunder \n B:Thunder is yellow \n C:Is thunder yellow? \n D:There is yellow thunder ")
total_questions += 1
choice = input(">>> ")
if choice in A6:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

print ("Question 7\n Translate: the ball(out of sight) is blue")
print (" A:tababan ze toch \n B:tababan ga toch \n C:tababan ke toch  \n D: tababan hecha toch")
total_questions += 1
choice = input(">>> ")
if choice in A7:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

print ("Question 8\n Translate:thijabi hecha baha ga uch ")
print (" A:a squirrels is at that hill(far away) \n B:some squirrels are at that hill (far awar) \n C:That squirrel(near listener) is at this hill(near speaker) \n D:a squirrel is at this hill(near speaker) ")
total_questions += 1
choice = input(">>> ")
if choice in A8:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

print ("Question 9\n Translate: ozija ga yakuch")
print (" A:you gave it to that spirit(distant) \n B:I gave it to that bear(distant) \n C:you gave it to that bear(distant) \n D:I gave it to that spirit(distant) ")
total_questions += 1
choice = input(">>> ")
if choice in A9:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

print ("Question 10\n Translate: Life is good")
print (" A:ni^bi da'a u^ch \n B:ni^bi da'ach \n C:Ni^bi wathtech \n D:ni^bi wathte u^ch ")
total_questions += 1
choice = input(">>> ")
if choice in A10:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

"""
print ("Question #")
print (" A: \n B: \n C: \n D: ")
total_questions += 1
choice = input(">>> ")
if choice in A#:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)
"""
# Above is a sample structure of a question
print("\nYou're finished, " + name +". You got", correct, "out of " + str(total_questions) + " correct.")
