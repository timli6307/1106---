star_count = int(input("請輸入星星數量："))

if star_count % 2 == 0:
    print("給予的星星數請輸入單數")
else:
    for i in range(1, star_count // 2 + 2):
        spaces = " " * (star_count // 2 + 1 - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    for i in range(star_count // 2, 0, -1):
        spaces = " " * (star_count // 2 + 1 - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
