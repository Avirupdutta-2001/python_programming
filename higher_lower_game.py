import random
import os

data=[
{
    'name': "Jenny's Lecture's",
    'follower_count': 1,
    'description': 'Youtuber',
    'country': 'India'
},
{
    'name':"Cristiano Ronaldo",
    'follower_count':600,
    'description':'Footballer',
    'country':'Portugal'
},
{
    'name':"Narendra Modi",
    'follower_count':90,
    'description':'Prime Minister',
    'country':'India'
},
{
    'name':"Fit Tuber",
    'follower_count':7,
    'description':'Youtuber',
    'country':'India'
},
{
    'name':"Selena Gomez",
    'follower_count':420,
    'description':'Musician and actress',
    'country':'United States'
},
{
    'name':"Kylie Jenner",
    'follower_count':400,
    'description':'Reality TV personalit and businesswoman and Self-Made Billionaire',
    'country':'United States'
},
{
    'name':"Pankaj Tripathi",
    'follower_count':5,
    'description':'Actor',
    'country':'India'
},
{
    'name':"Lionel Messi",
    'follower_count':480,
    'description':'Footballer',
    'country':'Argentina'
},
{
    'name':"Beyonce",
    'follower_count':315,
    'description':'Musician',
    'country':'United States'
},
{
    'name':"T-Series",
    'follower_count':245,
    'description':'Music Label & Movie Studio',
    'country':'India'
},
{
    'name':"Neeraj Chopra",
    'follower_count':6,
    'description':'Athelete',
    'country':'India'
},
{
    'name':"Justin Bieber",
    'follower_count':293,
    'description':'Musician',
    'country':'Canada'
},
{
    'name':"Taylor Swift",
    'follower_count':267,
    'description':'Musician',
    'country':'United States'
},
{
    'name':"Jennifer Lopez",
    'follower_count':249,
    'description':'Musician and actress',
    'country':'United States'
},
{
    'name':"Shakira",
    'follower_count':87,
    'description':'Musician',
    'country':'Clombia'
},
{
    'name':"NASA",
    'follower_count':94,
    'description':'Space Agency',
    'country':'United States'
},
{
    'name':"ISRO",
    'follower_count':1,
    'description':'Space Agency',
    'country':'India'
},
{
    'name':"Virat Kohli",
    'follower_count':254,
    'description':'Cricketer',
    'country':'India'
},
]
score=0
def display_accountinfo(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return f"{name}, a {description}, from {country}"
def check_answer(guess,followers_1,followers_2):
    if followers_1<followers_2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            False

account_2=random.choice(data)

continue_flag=True
while continue_flag:
    account_1=account_2
    account_2=random.choice(data)
    while account_1==account_2:
        account_2=random.choice(data)
    
    print(f"Compare 1: {display_accountinfo(account_1)}")
    print("\n     VS\n")
    print(f"Compare 2: {display_accountinfo(account_2)}")
    guess=int(input("Who has more followers? Type 1 or Type 2: "))
    followers_count_1=account_1["follower_count"]
    followers_count_2=account_2["follower_count"]
    is_correct=check_answer(guess,followers_count_1,followers_count_2)
    os.system('cls')
    if is_correct:
        score+=1
        print(f"You are right. Your Score is: {score}")
    else:
        print(f"You are wrong... Your final score is: {score}")
        continue_flag=False
