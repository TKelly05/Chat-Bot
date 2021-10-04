import pyttsx3
pyttsx3.init()
engine.runAndWait()
engine.say("I am feeling fine")


print("Hello!")
a = input("What's your name?")
print("Nice to meet you," + a)

print("So,")
b = input("How are you doing today?")
print("That's good to hear!")

print("I have been having a good day so far too!")
c = input("What are you plans?")
print("That sounds exciting!")

print("Actually,")
d = input("What will you be doing there?")
print("I might have to try that myself.")

e = input("Would you like to know my name? Yes/No?")

if e == "Yes":
    print("My name is Tobias Jakey the Third")

elif e == "No":
    print("Well too bad, my name is Tobias Jakey the Third")
else:
    print("Sorry. that is not an option!")
