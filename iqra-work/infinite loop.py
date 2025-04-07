#  infinite loops that loops run forever
while True:
   command =  input (">")
   print("ECHO",command)
   if command.lower() == "quiet":
      break