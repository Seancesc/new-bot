import random

def gen_pass(digit):
    letter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(digit):
        password += random.choice(letter)

    return password

def flip_coin():
    coin = random.randint(1, 2)
    if coin == 1:
        return 'tail!'
    else:
        return 'head!'
    

# uji coba
if __name__ == '__main__':
    coin = flip_coin()
    print(coin)