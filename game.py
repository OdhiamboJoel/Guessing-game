fav_language = 'Python'
guess = ''
guesses = 3
guess_count = 0
guess_limit = False


while guess != fav_language and not (guess_limit):
    guess = input('Guess my favourite language: ')
    if guess_count < guesses:
        guess_count += 1
        print('Wrong! Try again!')

    else:
        guess_limit=True
if guess_limit:        
    print('You have exhausted your free trials. Please upgrade to premium account for a free guess pack.')
else:
    print('Correct! You knew it all along')
    
