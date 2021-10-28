'''
File: Shiba Adventure
Author: Lily Huang
'''


print("Introduction:")
print("In this game, you are the cuteest shiba dog in the world, Chai Chai. Today is Friday, 22, Octber of 2021.")
print("You met her three years ago. In these years, you have been experience the coolest lifetime with Lily.")
print("You went to different cities in Taiwan and some places in the States. You're a international Shiba! HOW COOL IT IS!")
print("You love Lily very much and vice versa.")
print("You will choose in between two choice in this game. Every choices have different scenarios and consequences. Chai Chai's adventure is on your hand. Enjoy!")
print()
print("Story start:")
input("Press Enter to continue...")
print("Raise and shine! Today is a new day to be with my best owner, Lily.")
print("Chai Chai thinks")
print("Lily has prepared my food and we have breakfast together. After breakfast, Lily needs to go to work, I walk with her to the door and sit to wait for her ")
print("to give me a kiss because this is our daily routine since I was with her. " )
print("I missed the COVID time, because we can be with each other all the time. That is the best time......")
print("But! I am a good boy, I will be brave and good to wait for her until she gets back!")
input("Press Enter to continue...")


# go 
first = input("After saying good-bye to Lily, you want to GO OUT or STAY? (Type the answer)\n")
scenarios1 = False
if first.upper() == "GO OUT":
    print(" Woof! That's go out and have woof adventure")
    adv = input("Woof! That's go out and have woof adventure! Which way should we go out? DOG DOOR or WINDOW (Type the answer) \n ")
    if adv.upper() == "THROUGH THE DOG DOOR":
        print("Congras! You just saw your girlfriend Mimi! And now you get to play with her")
        gf = input("Oh my woofness! Why she can be that gorgeous all the time? What do you want to do with her? GIVE HER A KISS or BRING HER A FLOWER (Type the answer)\n")
        if gf.upper() == "GIVE HER A KISS":
            print("Opps! Mimi's owner Chloe gets mad. Take her away from me...\U0001F62D I guess our relationship is end.")
        elif gf.upper() == "BRING HER A FLOWER": 
            print("Mimi's owner Chloe think I am super sweet. I think she start likes me! Maybe one day Mimi and I can start a family!\U0001F970")
            print("Mimi and I play until sunset, what a good day!")
            print("Oh! I have to go home otherwise Lily will be worried.")
            input("Press Enter to continue...")
            print("Woof! Lily is  home, she carrying out some groceries. I am going to help her.")
            input("Press Enter to continue...")
            print("Lily: Here you are! I am wondering where have you been.")
            print("Chai Chai: woof! woof")
            print("So good to see you! I miss you! Today is a such good day, I go out and met Mimi. You would never believe she still that beautiful and......")
            input("Press Enter to continue...")
            print("The end. Thanks for bring a good day for Chai Chai! See you next time")

        else:
            print("Come man! Do something with your typo!")
    elif adv.upper() == "WINDOW":
            print("Ooch! You just hit your head becasue the window is too clear! Now going to the hospital.")
            hospital = input("Oh no...What have I done? Lily will be so worry about me. STAY AT THE HOSPITAL or INSIST GO HOME (Type the answer) \n")
            if hospital.upper() == "STAY AT THE HOSPITAL":
                print("Awww! There is a cute and kind vet, Andy. I need to be a good Shiba so he can remember me and hehe I can be Cupid!")
                print("I want somebody can take care of her. He is a good guy, I can tell from my magical sniff!")
                print("After reciving call from the hospital, Lily takes a day off and come to pick me up.")
                print("I bit Andy's cloth and won't let go. Lily have to talk to him!")
                input("Press Enter to continue...")
                print("At first, Andy is confuse why I did that BUT! He gets me after see Lily. Andy winks at me! Hey man, I got you!")
                print("Today is another good day with Lily, Chai Chai thinks.")
                input("Press Enter to continue...")
                print("The end. Thanks for bring a good day for Chai Chai! See you next time")
            elif hospital.upper() == "INSIST GO HOME":
                print("Oh! no! I feel like the whole world is shaking! I can't feel the strenth from my feet. I am pass out!")
                input("Press Enter to continue...")
                input("You wake up, and realize you were homed. Lily went to hospital and pick you up this afternoon.")
                print("The end. Thanks for bring a good day for Chai Chai! See you next time")
            else:
                print("Dude! Type the same word, ok?")
# stay 
elif first.upper() == "STAY":
    print(" Woof! Let's stay")
    home = input("What do you want to do at home? MAKE A MESS or TAKE A NAP (Type the answer)\n")
    if home.upper() == "MAKE A MESS":
        print("Hehe! Evil me.")
        home_mess = input("Where to go and mess around? KITCHEN or BATHROOM (Type the answer)\n")
        if home_mess.upper() == "KITCHEN":
            print("Wee! Look what I found! My snack! Forgetful Lily didn't hide it. Woof! Snack all you can eat!")
            print("'Finished the snack bag'")
            print("Hoooo! My tommy is full, my heart is full, too! Now, I want to take a nap.")
            input("Press Enter to continue...")
            print("Lily is home! She find out I eat all the snack... She says I don't have dinner tonight\U0001F62D")
            print("The end. Thanks for bring a good day for Chai Chai! See you next time")
        elif home_mess.upper() == "BATHROOM":
            print("OPPS. The toilet got stock with tissue.")
            print("Crap! There is no way I can fix it. ")
            print("After few hours, toilet gets worse......")
            input("Press Enter to continue...")
            print("Lily is home now. She saw the toilet but she doesn't get mad. Thank God.")
            print("Chai Chai: woof! woof! Lily, I am so sorry! I PROMISE I WON'T MESS BATHROOM, AGAIN!\U0001F62D")
            input("Press Enter to continue...")
            print("The end. Thanks for bring a good day for Chai Chai! See you next time")
        else:
            print("... What do you expect me to do? RESTART!")
    elif home.upper() == "TAKE A NAP":
        print("Sweat dream. I slept entire day. Lily is home! She is so happy to see me because I am such a good boy!")
        input("Press Enter to continue...")
        print("The end. Thanks for bring a good day for Chai Chai! See you next time")
    else:
        print("MAKE A MESS or TAKE A NAP? You say you can't choose? Now you have to restart again!")
else:
    print("I just want to do either this one or the other one. Now you have to restart. Booooo.") 
print()
print()

print("\U0001F923 \U0001F923 \U0001F923 \U0001F923 \U0001F923 Smile up!")
print("test")
print("haha")


import datetime
x = datetime.datetime.now()
print(x)
print()

