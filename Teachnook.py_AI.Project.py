import random
from textblob import TextBlob
import sys

#1 Name and Nickname conversation:-

print("Hello Dear, what's your name?!")
name = input()
print('Do you have a nickname?! [y/n] ')
ans = input()
if 'y' in ans.lower():
  print("What's your nickname?!")
  nickname = input()
  print('Good to meet you ' + nickname + '')
else:
  name_list = ['killua', 'don', 'idiot', 'yoyo', 'kimchi', 'phineas','dumb', 'cutie', 
               'gwen', 'meow', 'tuple', 'silly goose', 'babe', 'rose', 'tupperware', 'dude']
  nickname = random.choice(name_list)
  print('I will call you '+nickname )
  #2 greeting selection
greetings = [
    'How are you today ' + nickname + '?',
    'Howdy ' + nickname + " friend, how you feelin' today?",
    "What's up " + nickname + '?',
    'Greetings ' + nickname + ' are you well?',
    'How are things going ' + nickname + '?'
]
print(random.choice(greetings))
ans = input()
blob = TextBlob(ans)

if blob.polarity > 0:
  print('--->Sentimental Status :Positive')
elif blob.polarity < 0:
  print('--->Sentimental Status :Negative')
else:
  print('--->Sentimental Status :Neutral')
topics = [
    'football',
    'coding',
    'Marvel',
    'DC',
    'Python',
    'Computer Games',
    'your college',
    'COD'
]
print(r'"Quit" to leave chat...')
questions = [
    'What is your take on ',
    'What do you think about ',
    'How do you feel about ',
    'What do you reckon about ',
    'I would like your opinion on '
]
for i in range(0, random.randint(3, 4)):
  question = random.choice(questions)
  questions.remove(question)
  topic = random.choice(topics)
  topics.remove(topic)
  print(question + topic+'?')
  ans = input()
  if (ans.lower()=='quit'):
    print('It was good talking to u ' +  nickname +'.Have a good day.')
    sys.exit()
  blob = TextBlob(ans)
  if blob.polarity > 0:
    print('--->Sentimental Status :Positive')
  elif blob.polarity < 0:
    print('--->Sentimental Status :Negative')
  else:
    print('--->Sentimental Status :Neutral')

  if blob.polarity > 0.5:
    print("OMG, you really love "+topic)
  elif blob.polarity > 0.5:
    print("Well, you clearly like "+topic)
  elif blob.polarity < -0.5:
    print("Uff, you totally hate "+topic)
  elif blob.polarity < -0.1:
    print("So you don't like "+topic)
  else:
    print('That is a very common view on '+topic)

  if blob.subjectivity > 0.6:
    print('and you are so biased!')
  elif blob.subjectivity > 0.3:
    print('and you are bit biased!')
  else:
    print('and you are quite objective, huh!')
# Goodbyes selection
goodbyes = [
    'It was good talking to u ' +  nickname +  'I gotta go now!',
    "OK I'm bored"  +  nickname + "I go watch NetFlix",
    "Bye Bye" + nickname + "I'm out!",
    "Catch ya later " + nickname
]

print(random.choice(goodbyes))