#Kate Blunt
#Practice
#Old McDonald


def chorus(animal, sound):

    print("Old MacDonal had a farm, E-I-E-I-O, and on that farm he had a "
          + animal + " E-I-E-I-O.")
    print("With a " + sound + " " + sound + " here and a " + sound + " "
          + sound+ " there. ")
    print("Here a " + sound  + " there a "+ sound
          + " everywhere a " + sound  + " " + sound)

    print("OldMacDonald had a farm, E-I-E-I-O.")



def ending (sound):
    
    print("With a " + sound + " " + sound + " here and a " + sound + " "
            + sound+ " there.")
    print("Here a " + sound  + " there a "  + sound
            +" everywhere a " + sound  + " " + sound)

   

def title():
    print("Old McDonald Had A Farm Program")


    
def main():

    #variables
    soundSingle = ""
    animalSingle = ""
    choice = "y"
    animals = []
    sounds = []
    length = 0
    lengthSound = 0
    
    #call title
    title()

    print()

    while choice.lower() == "y":
         
        animalSingle = input("Please enter an animal name: ")
        animals.append(animalSingle)
        print()
        soundSingle = input("Please enter the sound that animal makes: ")
        sounds.append(soundSingle)
        print()
        choice = input("Enter another animal? Y/N? ")
        print()

    length = len(animals)
    i = 0
    #while i is less than the length of the string go through each array
    #i is 0, so it points to the first spot in the array!
    #then when it becomes one it goes to the next spot in the array. 
    while i < length: 
    
        chorus(animals[i],sounds[i])
        i+=1

    print()
    print()

    lengthSound = len(sounds)
    #call backwards
    #subtract two from the length, thus not repeating the last cluck cluck
    #have to subtract two because arrays start at 0
    j = lengthSound - 2
    while j >= 0:

        ending(sounds[j])
        
        j -= 1

    print("Old MacDonald had a farm E-I-E-I-OOOOOOO.........")
    print()
    print("Thanks for singing along!")
     print("This is changes to see how branches work")


    
main()
