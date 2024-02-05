from time import sleep
from pandas import *
from tqdm import tqdm
import random

print("")
sleep(0.1)
print("o                                                          o                                                      oOoOOoOOo  o                    ")
sleep(0.1)
print("O                                                          O                                  o                        o     O     o               ")
sleep(0.1)
print("o                                                          o                                                           o     o                     ")
sleep(0.1)
print("o                                                          o                                                           O     O                     ")
sleep(0.1)
print("O       .oOoO' 'OoOo. .oOoO O   o  .oOoO' .oOoO .oOo.      O       .oOo. .oOoO' `OoOo. 'OoOo. O  'OoOo. .oOoO          o     OoOo. O  'OoOo. .oOoO ")
sleep(0.1)
print("O       O   o   o   O o   O o   O  O   o  o   O OooO'      O       OooO' O   o   o      o   O o   o   O o   O          O     o   o o   o   O o   O ")
sleep(0.1)
print("O       O   o   o   O o   O o   O  O   o  o   O OooO'      O       OooO' O   o   o      o   O o   o   O o   O          O     o   o o   o   O o   O ")
sleep(0.1)
print("o     . o   O   O   o O   o O   o  o   O  O   o O          o     . O     o   O   O      O   o O   O   o O   o          O     o   O O   O   o O   o ")
sleep(0.1)
print("OOoOooO `OoO'o  o   O `OoOo `OoO'o `OoO'o `OoOo `OoO'      OOoOooO `OoO' `OoO'o  o      o   O o'  o   O `OoOo          o'    O   o o'  o   O `OoOo ")
sleep(0.1)
print("                          O                   O                                                             O                                    O ")
sleep(0.1)
print("                       OoO'                OoO'                                                          OoO'                                 OoO' ")
print("""
      
      
      """)

questionno = 1
answeredcorrectly = 0
answeredincorrectly = 0

# Read of CSV File (https://www.studytonight.com/python-howtos/how-to-read-csv-to-list-in-python)
filepath = input("Absolute path of csv (tagalog.csv by default): ")
if filepath == "":
    filepath = "tagalog.csv"
df = read_csv(filepath)
language_list = df['language'].tolist()
english_list = df['english'].tolist()
startpracticeq = input("Start Practice Now? (y/n): ")
nested_list = [english_list, language_list]
while True:
    if startpracticeq == "y":
        startpracticebool = 1
        break
    elif startpracticeq == "n":
        startpracticebool = 0
        break
    else:
        startpracticeq = input("Start Practice Nw? (y/n): ")
if startpracticebool == 1:
    print("Loading...")
    sleep(1)
    for i in tqdm(range(5)):
        sleep(0.5)
    while True:
        while True:
            selected_list = random.randint(0,1)
            if selected_list == 0:
                selected_word = random.choice(nested_list[0])
                wordposition = nested_list[0].index(selected_word)
                realanswer = nested_list[1][wordposition]
            elif selected_list == 1:
                selected_word = random.choice(nested_list[1])
                wordposition = nested_list[1].index(selected_word)
                realanswer = nested_list[0][wordposition]
            else:
                print("Exiting due to random number breakage")
            print("")
            practiceanswer = input("Question " + str(questionno) + ": What does " + selected_word + " mean? ")
            questionno = questionno + 1
            if practiceanswer == realanswer:
                print("Correct!")
                answeredcorrectly = answeredcorrectly + 1
            elif practiceanswer == "brk":
                totalanswered = questionno - 2
                averagescore = answeredcorrectly / totalanswered * 100
                
                print("")
                print("Practice Statistics:")
                print("    Total Questions Answered: " + str(totalanswered))
                print("    Total Questions Answered Correctly: " + str(answeredcorrectly))
                print("    Total Questions Answered Incorrectly: " + str(answeredincorrectly))
                print("    Overall Accuracy: " + str(averagescore))
                break
            else:
                print("Incorrect")
                print("The correct answer is " + realanswer)
                answeredincorrectly = answeredincorrectly + 1
        break
elif startpracticebool == 0:
    print("Exiting...")
else:
    print("Exiting due to break in loop")