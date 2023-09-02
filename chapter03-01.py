#simple conversation program
user = input("input : ")

g_sentence = "hello"
t_sentence = "time"

if g_sentence in user:
    print("hello.")
elif t_sentence in user:
    print("It is 22 o'clock now.")
else:
    print(user)
