from flask import Flask, abort, request, render_template
from data import data
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# dictionary
me = {
    "name": "Andrew",
    "last": "Reynolds",
    "email": "andyreynolds998@gmail.com",
}

# list
products = data


@app.route("/")
@app.route("/home")
def index():
    return "Hello from Flask"


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/about/name")
def aboutName():
    return me["name"]


@app.route("/about/fullname")
def aboutFullName():
    return me["name"] + " " + me["last"]


@app.route("/api/catalog")
def getCatalog():
    return json.dumps(products)

# create a POST endpoint
# to register new products


@app.route("/api/catalog", methods=['POST'])
def saveProd():
    prod = request.get_json()
    products.append(prod)
    return json.dumps(prod)


@app.route("/api/catalog/<category>")
def getProdByCategory(category):
    # find the products with a specific category
    results = []
    for prod in products:
        if(prod["category"] == category):
            results.append(prod)
    return json.dumps(results)


@app.route("/api/catalog/id/<id>")
def getProdById(id):
    for prod in products:
        if(prod["id"] == id):
            return json.dumps(prod)

    abort(404)


@app.route("/api/catalog/products/price/cheapest")
def getProdByPrice():
    cheapest = products[0]
    for prod in products:
        if(prod["price"] < cheapest["price"]):
            cheapest = prod
    return json.dumps(cheapest)


""""
@app.route("/api/catalog/products/price/threeCheapestProducts")
def cheapestProdList():
    threeCheap = products[0]
    for prod in products:
"""


@app.route("/api/categories")
def getCategories():

    categories = []
    for prod in products:
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)

    return json.dumps(categories)


@app.route("/api/test")
def test():
    # add
    products.append("strawberry")
    products.append("Dragon fruit")

    # length
    # print("You have: " + str(len(products)))
    print(f"You have: {len(products)} products in your catalog")

    # iterate
    for fruit in products:
        print(fruit)

    # print an string 10 times
    for i in range(0, 10, 1):
        print(me)

    # remove apple from products
    products.remove("Apple")
    # print the list
    print(products)

    return "Check your terminal"


# if __name__ == '__main__':
#  app.run(debug=True)  # dont deliver to client with debugger on
