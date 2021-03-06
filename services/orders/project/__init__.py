# services/orders/project/__init__.py

import os  # nuevo
from flask import Flask, jsonify, request  # nuevo
from flask_sqlalchemy import SQLAlchemy  # nuevo


# instanciando la app
app = Flask(__name__)

# estableciendo configuración
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


# instanciado la db
db = SQLAlchemy(app)  # nuevo

# model
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)

    def get_url(self):
        return url_for('get_customer', id=self.id, _external=True)

    def export_data(self):
        return {
            'self_url': self.get_url(),
            'name': self.name
        }

    def import_data(self, data):
        try:
            self.name = data['name']
        except KeyError as e:
            raise ValidationError('Invalid customer: missing ' + e.args[0])
        return self


@app.route('/customers/', methods=['GET'])
def get_customers():
    return jsonify({'customers': [customer.get_url() for customer in
                     Customer.query.all()]})

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    return jsonify(Customer.query.get_or_404(id).export_data())

@app.route('/customers/', methods=['POST'])
def new_customer():
    customer = Customer()
    customer.import_data(request.json)
    db.session.add(customer)
    db.session.commit()
    return jsonify({}), 201, {'Location': customer.get_url()}

@app.route('/customers/<int:id>', methods=['PUT'])
def edit_customer(id):
    customer = Customer.query.get_or_404(id)
    customer.import_data(request.json)
    db.session.add(customer)
    db.session.commit()
    return jsonify({})


@app.route('/orders/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
