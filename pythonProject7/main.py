def jadual_drab():
    start = 1
    end = 12

    length = 94
    star = "*" * length
    print(star)

    text = "JADUAL DARAB"
    width = 84
    centered_text = text.center(width)
    print(centered_text)

    print(star)

    print("", end="")
    for i in range(1, 13):
        print(f"\t{i}\t", end="")
    print()

    for i in range(start, end + 1):
        for j in range(1):
            print(f"{i}", end="")
        for j in range(start, end + 1):
            result = i * j
            print(f"\t{result}", end="\t")
        print()


if __name__ == '__main__':
    jadual_drab()
