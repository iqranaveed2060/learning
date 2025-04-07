successful = True
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    # print("attempt 3 time but failed")