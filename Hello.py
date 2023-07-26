from ast import FloorDiv
from random import randint
import copy

print("Welcome to the Madlib Games")

playing= input( "lets start, shall we\n")

if playing.lower() != "yes":
    quit()

    print("Okay, let's play the game: \n")


    noun1= input("Enter your Name: ")
    noun2= input("Enter your Friend's Name: ")
    noun3= input("Enter another Friends Name: ")
    place= input("Enter a place name: ")
    adjective1= input("Enter and Adjective: ")
    adjective2= input("Enter another Adjective: ")
    adjective3= input("Enter one more Adjective: ")
    adverb1= input("Enter an Adverb: ")
    adverb2= input("Enter another Adverb: ")
    Exclamation= input("Enter and Emotion: ")

    #print Story

    print(
        "One day\t" + noun1 + "went to" + place +"."
        "He felt very Lonely, even though the view was" + adjective1 +"."
        "He decied to call his two best friends" + noun2 + "and" + noun3 +"."
        "When they came, they told" + noun1 + "something" + adjective2 + "had happened"
        "When he came he found out that his other friend was falling off a cliff"
        + noun1 + "said" + Exclamation + "Inside he was feeling" + adjective +"."
        "After  that they had a" + adverb2 + "celebration"
        "They all laughed")
    