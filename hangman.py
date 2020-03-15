import random

HANGMAN_PICS = ['''

  +---+
      |
      |
      |
     ===''','''
  +---+
  0   |
      |
      |
     ===''','''
  +---+
  0   |
  |   |
      |
     ===''','''
  +---+
  0   |
 /|   |
      |
     ===''','''
  +---+
  0   |
 /|\  |
      |
     ===''','''
  +---+
  0   |
 /|\  |
 /    |
     ===''','''
  +---+
  0   |
 /|\  |
 / \  |
     ===''']


words = 'aigle babouin baleine belette blaireau bouc canard canari castor cerf chameau '.split()

def getRandomWord(wordList):
  # Retourne un mot au hasar parmi ceux d'une liste.
  wordIndex = random.randint(0, len(wordList) - 1)
  return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
  print(HANGMAN_PICS[len(missedLetters)])
  print()

  print('Mauvaises lettres :', end = ' ')
  for letter in missedLetters:
    print(letter, end=' ')
  print()

  blanks = '_' * len(secretWord)
  # Remplace les tirets par les lettres correctement devinées.
  for i in range(len(secretWord)):
    if secretWord[i] in correctLetters:
      blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    # Affiche le mot secret avec des espaces entre les lettres.
    for letter in blanks:
      print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
  # Affiche la lettre saisie par le joueur. S'assure qu'il s'agit d'une unique lettre de rien d'autre.
  while True:
    print('Propose une lettre.')
    guess = input()
    guess = guess.lower()
    if len(guess) != 1:
      print("Propose une seule lettre STP.")
    elif guess in alreadyGuessed:
      print("Tu as déjà demandé cette lettre.")
    elif guess not in 'abcdefghijklmnoprstuvwxyz':
      print("Propose une LETTRE STP.")
    else:
      return guess

def playAgain():
  # Retourne True si le joueur veut recommencer, False sinon.
  print("Veux-tu rejouer (oui ou non) ?")
  return input().lower().startswitch('o')


print("P E N D U")
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
  displayBoard(missedLetters, correctLetters, secretWord)

  # Invite le joueur à proposer une lettre.
  guess = getGuess(missedLetters + correctLetters)

  if guess in secretWord :
    correctLetters = correctLetters + guess

    # Verifie si le joueur a gagné.
    foundAllLetters = True
    for i in range(len(secretWord)):
      if secretWord[i] not in correctLetters:
        foundAllLetters = False
      break
    
    if foundAllLetters:
      print('Oui ! Le mot secret est "' + secretWord + '" ! Tu as gagné !')
      gameIsDone = True
  else:
    missedLetters = missedLetters + guess

    # Verifie si le joueur a perdu.
    if len(missedLetters) == len(HANGMAN_PICS) - 1:
      displayBoard(missedLetters, correctLetters, secretWord)
      print('Tu as épuisé tous tes essais !\nAprès ' + str(len(missedLetters)) + ' mauvaises lettres et ' + str(len(correctLetters)) + 'lettres exactes, le mot secret était "' + secretWord + '".')
    gameIsDone = True

  # Demande au joueur s'il veut recommencer (seulment si la partie est finie).
  if gameIsDone :
    if playAgain():
      missedLetters =''
      correctLetters =''
      gameIsDone = False
      secretWord = getRandomWord(words)
    else:
      break