import random

inStick = 20
print("there are", inStick ,"sticks in the pile")
player2 = str(input("What is your name: "))
player1 = "Smart Computer"
i=1 
loopFlag = True
while i<=inStick:
  loopFlag = True
  if inStick >= 4 or inStick == 1: #ถ้าอยากให้คอมชนะตลอดให้เอาเงื่อนไขหลัง or ออก
    p1Stick = random.randint(1,2)
    remainStick=inStick-p1Stick
    print(player1+" take" ,p1Stick, "sticks in the pile")
    print("There are" ,remainStick, "sticks in the pile")
    inStick = remainStick 
    if inStick <= 0:
      print(player2 + " win")
      break
  elif inStick == 2:
    p1Stick = 1
    remainStick=inStick-p1Stick
    print(player1+" take" ,p1Stick, "sticks in the pile")
    print("There are" ,remainStick, "sticks in the pile")
    inStick = remainStick 
  elif inStick == 3:
    p1Stick = 2
    remainStick=inStick-p1Stick
    print(player1+" take" ,p1Stick, "sticks in the pile")
    print("There are" ,remainStick, "sticks in the pile")
    inStick = remainStick 
  while inStick>0 and loopFlag == True:
    outStick = int(input(player2+ " How many sticks you will take  1 or 2: "))
    if outStick>0 and outStick<=2:
      remainStick=inStick-outStick
      print("There are" ,remainStick, "sticks in the pile")
      inStick = remainStick 
      loopFlag = False
      if remainStick <= 0:
        print(player1 + " win")
        break
    elif outStick>2:
      print("No you cannot take more than 2 sticks!")
    else:
      print("No you cannot take less than 1 sticks!")
