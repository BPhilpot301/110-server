from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello World, CH59!</p>"

@app.route("/cohort59")
def hi():
    return "<h1>Hello Cohort#59</h1>"

@app.get("/home")
def home():
    print("Home endpoint accessed")
    return "Welcome to the home page!"


@app.get("/api/students")
def students():
    print("Students endpoint accessed")
    student_names = ["Britney", "Etc", "Etc", "Etc"]
    return student_names



@app.get("/greet/<string:name>")
def greet(name):
    return f"Hello {name}"

@app.get("/contact")
def contact_api():
    print("Contact API endpoint accessed")
    user = {"name": "Britney", "age": 36}#dictionary
    return user


@app.get("/about")
def about_me():
    return "<h1> About me page</h1>"

products = ["Laptop", "Mouse", "Monitor"]

@app.get("/api/product")
def get_products():
    return products


@app.get("/api/product/count")
def get_products_count():
    return {"count": len(products)}


#Assignment#2

coupons = [
    {"name": "save10", "discount": 0.10},
    {"name": "save50", "discount": 0.50},
]

@app.get("/coupons")
def get_coupons():
    return coupons

#Add endpoint to save coupon codes
@app.post("/coupons")
def save_coupons():
    coupon = request.json
    coupons.append(coupons)
    return "OK", 201

#add endpoint to search coupon codes by its name
@app.get("/coupons/<coupon_name>")
def get_coupon_by_name(coupon_name):
    for coupon in coupons:
        if coupon["name"] == coupon_name:
            return coupon
        
    return "Coupon not found", 404

#add products_list
products_list = [
  {"id": 1, "title": "Laptop", "category": "Electronics", "price": 899.99},
  {"id": 2, "title": "Headphones", "category": "Electronics", "price": 199.99},
  {"id": 3, "title": "Coffee Mug", "category": "Kitchen", "price": 12.50},
  {"id": 4, "title": "Notebook", "category": "Stationery", "price": 5.99}
]


@app.get("/products")
def get_all_prpducts():
    return products_list
    
@app.post("/products")
def save_product():
    data = request.json
    products_list.append(data)
    return "New product added", 201


app.run(debug=True)
#app.run(debug=True, port=5500)


# Path Parameter (Dynamic Route)
