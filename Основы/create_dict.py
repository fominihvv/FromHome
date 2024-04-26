import random
chars = 'йфяцычувскамепинртгоьшлбщдюзжхэъ'
end = ['','ея']
count = 1_000_000

with open('word_1kk.txt', 'w', encoding='utf-8') as fi:
    for _ in range(count):
        print(''.join(random.choice(chars) for _ in range(random.randint(3,20)))+random.choice(end), file = fi)