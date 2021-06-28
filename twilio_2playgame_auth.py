from twilio.rest import Client
from random import randint
# Your Account SID from twilio.com/console
account_sid = "ACc05e97aa306494354bbdbda7b6d2b548"
# Your Auth Token from twilio.com/console
auth_token  = "a375b9482227094h76713bf2655d9d7c"

client = Client(account_sid, auth_token)


number = randint(0000,9999)
to = "+447624420296"

message = client.messages.create(
    to=to, 
    from_="+14049984082",
    body="hello"
    )

message = client.messages.create(
    to="+447624420296",
    from_="+14049984082",
    body="whatcha doin'"
    )

print("enter the word sent to your number")

if input() == number:
    def Hangman():
    
     word = input(" enter a word,player 1")
     print("good luck player 2!")
     guessed = []
     wrong = []

     tries = 7

    while tries > 0:

        out = ""
        for letter in word:
            if letter in guessed:
                out = out + letter
            else:
                out = out + "_"

        if out == word:
            break

        print("Guess the word:", out)
        print(tries, "chances left")

        guess = input().lower()

        if guess in guessed or guess in wrong:
            print("Already guessed", guess)
        elif guess in word:
            print("Yay!!!")
            guessed.append(guess)
        else:
            print("No,try again!")
            tries = tries - 1
            wrong.append(guess)

        print()

    if tries:
        print("You guessed", word)
    else:
        print("You didn't get", word)
else:
    print("sorry, validation failed")