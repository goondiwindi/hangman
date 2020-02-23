def hangman(word):
    wrong = 0
    stages = ['_____ ',
              '|    |',
              '|    O',
              '|   /|\\',
              '|   / \\',
              '|']
    letters = list(word)
    board = ["_"] * len(word)
    win = False

    print('Welcome to execution!')
 
    while wrong < len(stages):
        print('\n')
        char = input('Enter a character: ')

        if char.lower() in letters:
            for letter in letters:
                if letter == char:
                   letter_index = letters.index(letter)
                   board[letter_index] = letter
                   letters[letter_index] = '+'
        else:
            wrong += 1
        print(f'Your word: {" ".join(board)}')
        for i in range(0, wrong):
            print(stages[i])
            
        print(f'Attempts remainning: {len(stages) - wrong}')
        
        if '_' not in board:
            win = True
            print('You Win!!!')
            return

    if win == False:
        print(f'You lose. Hidden word is {word}')

hangman('hello')

