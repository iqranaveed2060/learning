#  break mean if condition  is true program execute and else part not execute if con false else part execute
# ist use false then true
successful = True
for number in range (3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("attempted 3 times and failed")