def main():
    with open(file='user.txt', mode='r', encoding='utf-8') as f:
        # text = f.read()
        # text = f.readlines()
        text = f.read().split('\n')

    print(text)


if __name__ == '__main__':
    main()
