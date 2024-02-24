def main():


    original_str = "Python Programming"
    sub1 = original_str[:6]
    sub2 = original_str[6:]
    merged_str = sub1 + sub2

    print(sub1)
    print(sub2)
    print(merged_str)
    return sub1, sub2, merged_str


if __name__ == '__main__':
    main()
