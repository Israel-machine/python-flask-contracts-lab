#!/usr/bin/env python3
import os
from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]

app = Flask(__name__)

#/contract/<id>
#   If the ID of the contract is found in the given array, return the contract information with a 200 response.
#   If the ID of the contract is not found, return a 404 response.
@app.route('/contract/<int:id>')
def get_contract(id):
    for contract in contracts:
        if contract["id"] == id:
            return f'{contract['contract_information']}', 200
    return "<h2>Error: Contract Not Found</h2>", 404

# /customer/<customer_name>
#   If the ID of the customer is found, return a 204 response and an empty response body.   
#   If the ID of the customer is not found, return a 404 response.

@app.route('/customer/<string:customer_name>')
def find_customer(customer_name):
    if customer_name in customers:
        return "", 204
    
    return "<h2>Error: Person not found</h2>", 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
