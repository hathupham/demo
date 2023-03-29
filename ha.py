from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/plus", methods=['GET'])
def plus():
    a = 1
    b = 1 
    c = a + b
    print(c)
    return {"Tong":c}
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
