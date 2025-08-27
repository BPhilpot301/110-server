from flask import Flask

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


app.run(debug=True)

# Path Parameter (Dynamic Route)
