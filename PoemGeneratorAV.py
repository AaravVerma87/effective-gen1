import random

#PHRASES
a = ["As the sun rises over the sky,", "Forget the sorrow don't be shy,", "The gentle breeze softly flows by,", "When twilight falls, the north star shines high,", "In the forests where shadows lie,", "As the river flows gently by,", "When winter blankets all in white,"]
b = ["With all the happiness it brings,", "Do not dwell on little things,", "As flowers bloom with vibrant things,", "The world tranforms with silent rings,", "The whispers of secrets it brings,", "Reflecting the stories it sings,", "The chill of the evening it clings,"]
c = ["Bid the moon and its friends goodbye,", "Look up above at the bright sky,", "Embrace the warmth and let love fly,", "Release your worries, let them fly,", "Beneath the branches dreams can fly,", "Every ripple tells of a high,", "Yet warmth awaits in the firelight,"]
d = ["And hear the little birds sing", "You'll know when to unfurl your wings", "And hear the joyful robin sing", "Feel the joy that music brings", "Dance along with nature's strings", "And low tides of life's endless flings", "As comfort from friendship softly springs"]

print("Welcome to the Poem Generator!\n")
    
#RUN LOOP
i = 1
while i > 0:

    #CHOICE
    print("1. Continue program", "\n2. End program")
    x = int(input("Enter your choice: "))

    #START
    if x == 1:
        print("\nPoem generated:\n")
        
        rand = random.randint(0,6)
        print(a[rand])
        rand = random.randint(0,6)
        print(b[rand])
        rand = random.randint(0,6)
        print(c[rand])
        rand = random.randint(0,6)
        print(d[rand]+"\n")
        continue
    
    #END
    elif x == 2:
        print("\nProgram Ended")
        break

    else:
        print("\nInvalid input!"+"\n")
        continue
