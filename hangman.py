import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


i=random.randint(1,len(words))
print (words[i])
print(HANGMANPICS[0])

secretword=words[i]
#the classic programming way
#coveredword=''
#for k in range(0,len(words[i])):
#  coveredword+='_ '
#print(coveredword)

# the python way
coveredword='_ '*len(words[i])
print(coveredword)


correctcount=0
wrongcount=0
correctletters=''
wrongletters=''

while wrongcount <=5 and correctcount<len(secretword):

  
  l=''
  while (len(l)!=1) or (l not in'abcdefghijklmnopqrstuvwxyz') and (l!='.'):
    print('Guess one letter',end='')
    l=input().lower()

  if l in correctletters or l in wrongletters:
    print('Already chosen')
  else:
    if l in secretword:
      correctletters=correctletters+l
      print('Right')
      for x in secretword:
        if x==l:
          correctcount+=1
    else:
      wrongletters=wrongletters+l
      wrongcount+=1
      print('Wrong',wrongcount)
      print(HANGMANPICS[wrongcount])
      
  #print(correctletters,' ' , wrongletters)
  coveredword=''
  for x in secretword:
    if x in correctletters:
      coveredword=coveredword+x+' '
    else:
      coveredword=coveredword+'_ '
  print(coveredword)

if len(secretword)>correctcount:
  print('Sorry you lost',correctcount,'-',wrongcount)
  print('The secret word was:',secretword)
else:
  print('Bravo!',correctcount,'-',wrongcount)
