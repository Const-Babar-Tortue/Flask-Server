from flask_jwt import jwt_required
from flask_restful import Resource

from Application import db
from Application.models.BillTable import Bill
from Application.models.ClientTable import Client


class SingleClient(Resource):
    method_decorators = [jwt_required()]

    def delete(self, client_id):
        exists = Client.query.filter(Client.id == client_id).first()

        if exists is None:
            return {"message": "Client does not exists"}, 404

        # delete all bills related to this client
        Bill.query.filter(Bill.client_id == client_id).delete()

        Client.query.filter(Client.id == client_id).delete()
        db.session.commit()

        return {"message": "Deleted"}

    def get(self, client_id):
        client = Client.query.filter(Client.id == client_id).first()

        if client is None:
            return {"message": "Client does not exists"}, 404

        client_dict = {
            "id": client.id,
            "name": client.name,
            "street": client.street,
            "streetNumber": client.street_number,
            "postalCode": client.postal_code,
            "city": client.city,
            "firm": client.firm,
            "vatNumber": client.vat_number,
        }

        return client_dict

