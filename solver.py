def readtest():
    tosolve = []
    wordlist = []
    with open('testsearch.txt', 'r') as f:
        lines = f.readlines()
        i = 0
        while lines[i].strip() != 'wordlist':
            tosolve.append(lines[i].strip().split())  # add the list of characters to the tosolve list, creating a 2D list
            i += 1
        i += 1
        while i < len(lines):
            wordlist.append(lines[i].strip())
            i += 1
    return tosolve, wordlist

def scanadjacent(x, y, tosolve, word):
    assert tosolve[x][y] == word[0]
    if len(word) == 1:
        return True

    # directions: (1, 1) = down-right, (-1, -1) = up-left, etc.
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]  
    for direction in directions:
        dx, dy = direction
        if 0 <= x + dx < len(tosolve) and 0 <= y + dy < len(tosolve[0]):
            if tosolve[x + dx][y + dy] == word[1]:
                if scandirection(x + dx, y + dy, tosolve, word, direction):
                    return True
    return False

def scandirection(x, y, tosolve, word, direction):
    dx, dy = direction
    for i in range(1, len(word)):
        if not (0 <= x < len(tosolve) and 0 <= y < len(tosolve[0])):
            return False
        if tosolve[x][y] != word[i]:
            return False
        x += dx
        y += dy
    return True

def solve(quiz):
    tosolve, wordlist = quiz
    for x in range(len(tosolve)): # iterate through rows 
        for y in range(len(tosolve[x])): # iterate through each letter in the row
            for word in wordlist: 
                if tosolve[x][y] == word[0]: # if the first letter of the word is found
                    if scanadjacent(x, y, tosolve, word): # scan the adjacent letters to see if the word is found
                        print(f'found {word}')

solve(readtest())