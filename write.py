def main():
    with open(file='user.txt', mode='a', encoding='utf-8') as f:
        f.write('Bob,79\n')
        f.write('Tom,59\n')
        print(f.closed)

    print(f.closed)


if __name__ == '__main__':
    main()
