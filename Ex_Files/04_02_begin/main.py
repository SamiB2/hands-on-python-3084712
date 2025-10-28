from flask import Flask

app = Flask(__name__) #this is how you start the Flask object in Flask. 

@app.route("/")
def hello(): 
  return "Hello, World!"

app.run(debug=True)
