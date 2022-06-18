def hashing_by_division(k, m):
    return k % m


def main():
    dictionary = {
        'a': 1,
        'b': 9,
        'c': 'nebraska',
        'd': True
    }

    print(dictionary)

    # insert 
    dictionary['e'] = False
    print(dictionary)

    # delete 
    del dictionary['a']
    print(dictionary)

    # search
    print(dictionary['c'])

    # key = 50, table size = 13
    k = 50
    m = 13
    print(f'hash of 50: {hashing_by_division(k, m)}')

main()
