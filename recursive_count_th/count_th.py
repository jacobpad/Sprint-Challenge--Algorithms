'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # Because I cant use loops, I'll use recursion and it'll need a base case & some sort of counter
    count = 0

    # Make the word a list of letters
    word = list(word)

    # If word contains less than 2 letters, it's not going to pass
    if len(word) < 2:
        return 0

    # Check the first two indexes
    elif word[0] == 't' and word[1] == 'h':
        # Increment the counter by 1 to check the next two indexes
        count += 1

    # Continue where we left off using the updated index location starting place by slicing off any
    # prior letters and overwriting our list (word)
    return count + count_th(word[1:])




# Should return 2 occurrences of the following strin≈g
print('\n')
print(count_th('apthlrthwe'))
print('\n')










