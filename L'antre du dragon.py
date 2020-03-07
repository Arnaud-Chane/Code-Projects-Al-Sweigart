import random
import time

def displayIntro():
  print(''' 
Tu es dans un pays rempli de dragons. 
Devant toi, tu vois deux grottes. 
Dans l'une, le dragon est amical et partagera son tresor avec toi. 
Dans l'autre, le dragon est affamé et te dévora s'il te voit.
''')
  print()

def chooseCave():
  cave = ''
  while cave != '1' and cave != '2':
    print('Dans quelle grotte vas-tu entrer (1 ou 2) ?')
    cave = input()
  return cave

def checkCave(chosenCave):
  print("Tu t'approches de la grotte ... ")
  time.sleep(2)
  print("Tout est sombre et effrayant ... ")
  time.sleep(2)
  print("Un énorme dragon saute juste devant toi ! " + "Il ouvre grand ses machoires et ... ")
  print()
  time.sleep(2)
  
  friendlyCave = random.randint(1, 2)

  if chosenCave == str(friendlyCave):
    print("te donne son trésor !")
  else:
    print("t'avale d'un seul coup !")
  print()

playAgain = "Oui"
while playAgain == "Oui" or playAgain == "O":
  displayIntro()
  caveNumber = chooseCave()
  checkCave(caveNumber)

  print("Veux-tu rejouer (oui ou non) ?")
  playAgain = input()