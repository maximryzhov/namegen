# -*- coding: utf8 -*-
import random


vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v',]
clusters = ['bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'sc', 'sk', 'sl', 'sm', 'sn', 'sp', 'squ',
            'st', 'str', 'scr', 'spl', 'spr', ]


def _generate_random_model(min, max):
    length = random.randint(min, max)
    model = []
    unit = None
    for x in range(length):
        if unit is None:
            unit = random.choice(('v', 'u', 'c'))
            model.append(unit)
        elif unit == 'v':
            unit = random.choice(('u', 'c'))
            model.append(unit)
        elif unit == 'c' or unit == 'u':
            unit = 'v'
            model.append(unit)
    return model


def _get_random_variant(model):
    word = []
    for unit in model:
        if unit == 'v':
            word.append(random.choice(vowels))
        elif unit == 'u':
            word.append(random.choice(consonants))
        elif unit == 'c':
            word.append(random.choice(clusters))
    return ''.join(word)


def generate_name(first_name_min, first_name_max, last_name_min, last_name_max, gender):
    if gender == 'm':
        suffix = 'us'
    elif gender == 'f':
        suffix = 'a'
    elif gender == 'n':
        suffix = 'um'
    elif gender == 'r':
        suffix = random.choice(('us', 'a', 'um'))
    else:
        return 'Wrong gender, use "f", "m", "n" or "r" for random'

    first_name_model = _generate_random_model(first_name_min, first_name_max)
    last_name_model = _generate_random_model(last_name_min, last_name_max)
    first_name = '{0}{1}'.format(_get_random_variant(first_name_model), suffix).capitalize()
    last_name = '{0}{1}'.format(_get_random_variant(last_name_model), suffix).capitalize()

    return '{0} {1}'.format(first_name, last_name)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('quantity', type=int, help='Number of names to generate', nargs='?', default=1)
    parser.add_argument('gender', type=str, help='Grammatical gender: f, m, n, r(random)', nargs='?', default='r')
    parser.add_argument('--f_min', type=int, help='First name root minimum length',  default=2)
    parser.add_argument('--f_max', type=int, help='First name root maximum length',  default=4)
    parser.add_argument('--l_min', type=int, help='Last name root minimum length',  default=2)
    parser.add_argument('--l_max', type=int, help='Last name root maximum length',  default=4)
    args = parser.parse_args()

    for _ in range(0, args.quantity):
        print(generate_name(args.f_min, args.f_max, args.l_min, args.l_max, args.gender))

    