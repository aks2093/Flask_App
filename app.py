from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'abcd'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt  = JWT(app,authenticate,identity) #create new end point /auth

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/item/chair
api.add_resource(UserRegister, '/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5001, debug = True)
    
# items = []
#
# class Item(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('price',
#         type = float,
#         required = True,
#         help = "This field can not be left blank!"
#     )
#     @jwt_required()
#     def get(self,name):
#         item = next(filter(lambda x: x['name']==name,items), None) #next will give the first item found in return filter function
#         # for item in items:
#         #     if item['name'] == name:
#         #         return item
#         return {'item':item}, 200 if item else 404
#
#     def post(self,name):
#         if next(filter(lambda x: x['name'] == name,items),None):
#             return {'message':"An Item with name '{}' already exists.".format(name)},400 #400: bad request
#         #data = request.get_json()
#         data = Item.parser.parse_args()
#         item = {'name':name,'price':data['price']}
#         items.append(item)
#         return item, 201
#
#     def delete(self,name):
#         global items
#         items = list(filter(lambda x: x['name'] != name,items))
#         return {'message':'Item deleted'}
#
#     def put(self,name):
#         #data = request.get_json()
#         data = Item.parser.parse_args()
#         item = next(filter(lambda x:x['name']==name,items),None)
#
#         if item:
#             item.update(data)
#         else:
#             item = {'name':name,'price':data['price']}
#             items.append(item)
#
#         return item
#
# class ItemList(Resource):
#     def get(self):
#         return {'items':items}
