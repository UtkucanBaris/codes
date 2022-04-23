# def filtered(x, y):
#     for i in x:
#         return lambda a: i % y


# number = []
# for i in range(1, 101):
#     number.append(i)
# one = filtered(number, 1)
# two = filtered(number, 2)
# three = filtered(number, 3)

# if __name__ == "__main__":
#     one = filtered(number, 1)
#     two = filtered(number, 2)
#     three = filtered(number, 3)
#     print(one(3))
#     print(two(5))
#     print(three(15))

def filtered(items, myfilter):
    return list(filter(myfilter, items))


if __name__ == '__main__':
    print(*filtered(list(range(0, 101)), lambda x: x % 3 == 0), sep=', ')
    print(*filtered(list(range(0, 101)), lambda x: x % 5 == 0), sep=', ')
    print(*filtered(list(range(0, 101)), lambda x: x % 15 == 0), sep=', ')
