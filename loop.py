ylet=24
num=13
row= 0
letter=0
num2=13
for i in range(num):
    for j in range((num - i) - 1):
        print(end=" ")
    for j in range(1):
        print("***", end="")
    for s in range(row * 2):
        if i == 6 or i == 7:
            print("*", end="")
        else:
            print(end=" ")
    row = row + 1
    for k in range(1):
        print("***", end=" ")
    # the first A ended with variable i,j,k,num,row
    for y in range(15):
        print(end=" ")
    for a in range(1):
        print("***", end="")
    for b in range(ylet):
        print(end=" ")
    ylet = ylet - 2
    for c in range(1):
        print("***", end="")
# the Y letter (the top part only) ended with variable y,a,b,c,ylet
    for t in range(20):
        print(end=" ")


    for l in range(1):
            print("***", end="")
    for m in range(letter * 2):
            if i== 6 or i == 7:
              print("*", end="")
            else:
                print(end=" ")
    letter = letter + 1
    for n in range(1):
            print("***", end="")
    print(" ")
for sp in range (6):
  for space in range(46):
    print (end=" ")
  for p in range(1):
     print("******")