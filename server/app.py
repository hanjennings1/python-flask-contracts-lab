#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

# SEARCH BY CONTRACT ID
@app.route('/contract/<int:id>')
def contract(id):
    for contract in contracts:                  # loop through each contract dict
        if contract["id"] == id:                # match found by id
            return contract["contract_information"] # 200 by default
    return make_response("", 404)               # no match: empty body & 404

# CHECK IF CUSTOMER EXISTS BY NAME
@app.route('/customer/<customer_name>')
def customer(customer_name):
    for name in customers:              # loop through each customer name
        if name == customer_name:       # match found
            return make_response("", 204)   # found, no data (sensitive)
    return make_response("", 404)           # no match: empty body & 404



if __name__ == '__main__':
    app.run(port=5555, debug=True)
