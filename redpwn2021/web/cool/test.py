#from random import SystemRandom
import random
#rand=random

allowed_characters = set(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
)
print(allowed_characters)

def generate_token():
    return ''.join(
        random.choice(list(allowed_characters)) for _ in range(32)
    )
    
print(generate_token())

