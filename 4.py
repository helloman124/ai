import os

def draw(b):
    for i in range(6, -1, -3): print(' '.join(b[i:i+3]))

def take_input(b, t):
    while True:
        try:
            p = int(input(f"{t}'s turn: Pick position 1-9: "))
            if 1 <= p <= 9 and b[p-1] == ' ': return p
        except (ValueError, IndexError): pass
        print("Enter a valid position.")

def check_win(b):
    for i in range(0, 3):
        if b[i] == b[i+3] == b[i+6] != ' ' or b[i*3] == b[i*3+1] == b[i*3+2] != ' ': return b[i] if b[i] != ' ' else 0
    return b[4] if b[0] == b[4] == b[8] != ' ' or b[2] == b[4] == b[6] != ' ' else 0

b, t, s = [' ']*9, 'X', 9

while s:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw(b)
    p = take_input(b, t)
    b[p-1], s, t = t, s-1, 'O' if t == 'X' else 'X'
    w = check_win(b)
    if w or not s: break

print("Draw" if not w else f'{w} wins')
input()
