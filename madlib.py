# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to ____"


# youtuber = "hatice" # some string variable

# # a few ways to dp this

# print("subscribe to " + youtuber)
# print("subscribe to {} ".format(youtuber))
# print(f"subscribe to {youtuber}")


adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
fomous_person = input("Famous person: ")
madlib = f"Computer is so {adj}! It makes me so all the time because I love to {verb1}. " \
         f"Stay hydrated and {verb2}  like you are {fomous_person}! "

print(madlib)
