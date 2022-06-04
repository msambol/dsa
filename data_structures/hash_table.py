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

main()
