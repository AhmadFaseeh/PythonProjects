t=int(input ("Enter time"))
h=int(input ("Enter hours"))

if(t>12 and t<16):
    print("Good Afternoon")
elif(t>16 and t<20):
    print("Good Evening")
elif(t>20 and t<24):
    print("Good Night")
elif(t>=0 and t<12):
    print("Good morning")
else:
    print("Invalid time entered")