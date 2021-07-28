from urllib import parse
from flask import Flask, abort, request, render_template
from data import data
import json
from flask_cors import CORS
from config import db, parse_json


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
    cursor = db.products.find({})
    # establish an empty list for the catalog to exist, add all items in the cursor to a list. curser cant be parsed, a list can
    catalog = [item for item in cursor]
    return parse_json(catalog)

# create a POST endpoint to register new products


@app.route("/api/catalog", methods=['POST'])
def saveProd():
    prod = request.get_json()
    db.products.insert(prod)
    return parse_json(prod)


@app.route("/api/categories")
def getCategories():
    data = db.products.find({})
    categories = []
    for prod in data:
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)

    return json.dumps(categories)


@app.route("/api/catalog/<category>")
def getProdByCategory(category):
    data = db.products.find({"category": category})
    results = [item for item in data]
    return json.dumps(results)
    # find the products with a specific category


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


# test function
@app.route("/api/test")
def test():
    test_data = db.test.find({})
    print(test_data)

    return parse_json(test_data[0])

# discount code logic


@app.route("/test/populatecodes")
def test_populate_codes():
    db.couponCodes.insert({"code": "qwerty", "discount": 10})
    db.couponCodes.insert({"code": "yeehaw", "discount": 15})
    db.couponCodes.insert({"code": "stinger", "discount": 20})
    db.couponCodes.insert({"code": "hogwarts", "discount": 50})

    return "Codes registered"


@app.route("/api/discountcode/<code>")
def validate_discount(code):
    data = db.couponCodes.find({"code": code})
    for code in data:
        return parse_json(code)

    return parse_json({"error": True, "reason": "invalid code"})

# if __name__ == '__main__':
#  app.run(debug=True)  # dont deliver to client with debugger on
