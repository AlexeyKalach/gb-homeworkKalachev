# Задание 1-2
dictary_rus_eng = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def translate_words(eng_word):
    if eng_word[0].isupper():
        eng_word = eng_word.lower()
        return dictary_rus_eng[eng_word].capitalize()
    else:
        return dictary_rus_eng[eng_word]
print(translate_words('Three'))
print(translate_words('three'))

# Задание 3
def thesaurus(*workers):
    out_dict = dict()
    for worker_name in workers:
        out_dict.setdefault(worker_name[0], [])
        out_dict[worker_name[0]].append(worker_name)
    return out_dict
print(thesaurus("Гоша", "Мария", "Мината", "Гена"))

# Задание 5

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    """Функция для генерации шутки, где numbers - целое(!) число, значащее количество шуток"""
    jokes = []
    for i in range(num):
        cur_nouns = random.choice(nouns)
        cur_adverbs = random.choice(adverbs)
        cur_adjectives = random.choice(adjectives)
        jokes.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
    return jokes

print(get_jokes(3))
