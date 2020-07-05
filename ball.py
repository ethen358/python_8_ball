import random

# Print two empty strings to seperate from command line
print('')
print('')

# Variables for answers:
magic_number = random.randint(1, 20)
print("What is your question?")
question = input()

def roll_ball(magic=magic_number):
    if magic_number == 1:
        return 'As I see, yes.'
    if magic_number == 2:
        return 'Ask again later.'
    if magic_number == 3:
        return 'Better not tell you now.'
    if magic_number == 4:
        return 'Cannot predict now.'
    if magic_number == 5:
        return 'Concentrate and ask again.'
    if magic_number == 6:
        return 'Don\'t count on it.'
    if magic_number == 7:
        return 'It is certain.'
    if magic_number == 8:
        return 'It is decidely so.'
    if magic_number == 9:
        return 'Most likely.'
    if magic_number == 10:
        return 'My reply is no.'
    if magic_number == 11:
        return 'My sources say no.'
    if magic_number == 12:
        return 'Outlook is not so good.'
    if magic_number == 13:
        return 'Outlook is good.'
    if magic_number == 14:
        return 'Reply hazy, try again.'
    if magic_number == 15:
        return 'Signs point to yes.'
    if magic_number == 16:
        return 'Very doubtful.'
    if magic_number == 17:
        return 'Without a doubt.'
    if magic_number == 18:
        return 'Yes.'
    if magic_number == 19:
        return 'Yes... Definitely.'
    if magic_number == 20:
        return 'You can rely on it.'
answer = roll_ball()

print("You asked: "+question+'?')
print("")
print(answer)
print("")
print("")