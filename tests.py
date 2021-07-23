from data import data

products = data


def test1():
    print("***Print each product title")

    for prod in products:
        title = prod["title"]
        print(title)


def test2():
    print("sum of all prices")

    sum = 0
    for prod in products:
        price = prod["price"]
        sum += price

    print(f"the sum is: {sum}")


def test3():
    print("all products that cost more than 12 dollars")

    for prod in products:
        if(prod["price"] > 12):
            print(prod["title"])


def test4():
    print("price of entire stocked inventory")

    sum = 0
    for prod in products:
        value = prod["price"] * prod["stock"]
        sum += value

    print(f"the value of the stock is: ${sum}")


def test5():
    print("***list of categories")

    categories = []
    for prod in products:
        cat = prod["category "]
        # how to check if an element exists inside a list in python
        if cat not in categories:
            categories.append(cat)
            print(cat)


def runTests():
    print("***Starting tests")

    test1()
    test2()
    test3()
    test4()
    test5()


runTests()
