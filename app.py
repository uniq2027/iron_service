from flask import Flask, jsonify

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 750},
    {"id": 2, "name": "Smartphone", "price": 500},
    {"id": 3, "name": "Tablet", "price": 300},
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


if __name__ == "__main__":
    # Run Flask on all interfaces so Java can connect
    app.run(host="0.0.0.0", port=5000, debug=True)


        

#                     language      
# india==>tamil    ==ஒன்று  ==>india==>understand
# Landon==>english ==one     ==>india==>not understand 
# china==>chinese  ==yī      ==>india==>not understand 

#                  language    json
# india==>tamil    ==ஒன்று   ==>1  ==>india=understand
# Landon==>english ==one      ==>1  ==>india=understand
# china==>chinese  ==yī       ==>1  ==>india=understand











#JWT - JSON Web Token

#Install The JWT
# pip install PyJWT

# import jwt
# import datetime

# SECRET_KEY = 'my_secret_key'

# payload={
#     'user_id':123,
#     'username':'John',
#     'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
# }

# token = jwt.encode(payload,SECRET_KEY,algorithm='HS256')

# print("Generated JWT Token :",token) 

# # #Decoded the JWT Token:
# decoded = jwt.decode(token,SECRET_KEY,algorithms='HS256')

# print("Decoded Text: ",decoded)


