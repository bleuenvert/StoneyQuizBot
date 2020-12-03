import time

correct = 0 #Storing the correct answers
total_questions = 0 #storing number of question (for extendability)

name = input ("Hello, I am StoneyQuizbotAlpha, what is your name?\n") #Storing the user's name

print("Nice to meet you " + name +"! \n Note that: for nasals a `^` symbol will be put after the vowel; for voiced interdental fricative dh will be used" + "\n Let's get started!")
#I need to find some way of including the orthography of stoney. Might need to find a module that builds a graphical interface. (Maybe that way latex symbols could be used?)
time.sleep(2)

total_questions += 1 #adds a counter for each question
print ("Question 1\n Translate: Wapta ze tha^ch")
print (" A:This river (near the speaker) is white \n B:That white river (near speaker) \n C:That white river(near listener) \n D:That river (near the listener) is white ")
choice = input(">>> ")
A = [ "D", "d" ]
if choice in A:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

total_questions += 1
print ("Question 2\n Translate: A'an ne ana^yarapta^ch")
print (" A:You are listening to this(near speaker) crow \n B:I am listening to that(near listener) crow\n C:I am listening to this (near speaker) crow \n D:You are listening to that(near listener) crow ")
choice = input(">>> ")
A = ["A", "a"  ]
if choice in A:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

total_questions += 1
print ("Question 3\n Translate: Me, I'm walking")
print (" A:Niye ma^wani^ch \n B:Iye ma^wani^ch \n C:Miye ma^wani^ch \n D:I^ygi^ye ma^nani^ch ")
choice = input(">>> ")
A = ["C", "c"  ]
if choice in A:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

total_questions += 1
print ("Question "+ str(total_questions) + "\nTranslate: Ade i^na yarhogabi kuch")
print (" A:My dad gave bread to my mom \n B:My mom gave bread to my dad \n C:Bread gave my mom to my dad \n D:My mom gave my dad to bread ")
choice = input(">>> ")
A = ["a", "A" ]
if choice in A:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

total_questions += 1
print ("Question "+ str(total_questions) + "\nTranslate: you all are playing drums")
print (" A:Gamubi yihotuch \n B:Gamubi nihotuch \n C:Gamubi yihotubich \n D:Gamubi nihotubich")
choice = input(">>> ")
A = ["D", "d"  ]
if choice in A:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

total_questions += 1
print ("Question " + str(total_questions) + "\n Translate: Mu thich")
print (" A:Yellow thunder \n B:Thunder is yellow \n C:Is thunder yellow? \n D:There is yellow thunder ")
choice = input(">>> ")
A = ["B", "b"  ]
if choice in A:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

total_questions += 1
print ("Question " + str(total_questions) + "\n Translate: The ball(out of sight) is blue")
print (" A:Tababan ze toch \n B:Tababan ga toch \n C:Tababan ke toch  \n D:Tababan hecha toch")
choice = input(">>> ")
A = ["C", "c"  ]
if choice in A:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

total_questions += 1
print ("Question " + str(total_questions) + "\n Translate:Thijabi hecha baha ga uch ")
print (" A:A squirrel is at that hill(far away) \n B:Some squirrels are at that hill (far awar) \n C:That squirrel(near listener) is at this hill(near speaker) \n D:A squirrel is at this hill(near speaker) ")
choice = input(">>> ")
A = ["B", "b"  ]
if choice in A:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

total_questions += 1
print ("Question " + str(total_questions) + "\n Translate: Ozija ga yakuch")
print (" A:You gave it to that spirit(distant) \n B:I gave it to that bear(distant) \n C:You gave it to that bear(distant) \n D:I gave it to that spirit(distant) ")
choice = input(">>> ")
A = ["C", "c"  ]
if choice in A:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

total_questions += 1
print ("Question " + str(total_questions) + "\n Translate: Ta ze i^sti^ma^ch")
print (" A:That moose (near the listener) is sleeping \n B:That bear(ntl) is sleeping \n C:That dog (ntl) is sleeping \n D:That squirrel (ntl) is sleeping ")
choice = input(">>> ")
A = ["A", "a"  ]
if choice in A:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)

"""
total_questions += 1
print ("Question #")
print (" A: \n B: \n C: \n D: ")
choice = input(">>> ")
A = ["set of answers" ]
if choice in A#:
  correct += 1 #If correct, the user gets one point
  print("That is right!")
else:
  correct += 0
  print("Sorry that is not correct")
time.sleep(1)
"""
# Above is a sample structure of a question

if correct / total_questions == 1:
    print("Wow great job " + name + ". You got a perfect score!")
elif correct / total_questions >= 0.7:
    print("Good work " + name + ". You got ", correct, "out of", total_questions)
else:
    print("We should do some more studying! You got", correct, "out of", total_questions)
