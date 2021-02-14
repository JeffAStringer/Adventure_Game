import time

def fireManGame():
    print("""Today is your first day on Fire Crew 317, welcome to the crew!\n..And guess what!  Do you hear that?  That's the alarm bell,
time to respond to your first call!
    A man called to say he smells gas in his house, we need to go check it out, do we...
    (A), speed to the house with our sirens on?
    (B), drive the speed limit with no sirens?""")
    choiceOne = input()
    if choiceOne == 'A':      
        print("""You turn on your sirens and speed to the house, getting there quickly but also safely
        You see the man and his family standing outside on the curb, they tell you when they woke up, the whole house smelled like gas
        Do you...
                (A), rush in the house to identify the source of the gas?
                (A), find the main gas line and shut it off before going inside?""")
        choiceTwo = input()
        if choiceTwo == 'a':
              print('You rush in the house, only to hear the fire chief scream at you that you forgot to turn the gas off!')
        elif choiceTwo == 'b':
              print('You find the main gas line, and shut if off before going inside.')
        
    elif choiceOne == 'b':              
          print("""You leave the station without your sirens on, and get stuck in traffic on a busy road!
Nobody moves out of the way because they don't know there is an emergency!
Unfortunately, you didn't make it in time, the house is now full of gas and will have to be fumigated for the next 24 hours until the family can go back inside.
Game over.""")
         
       

