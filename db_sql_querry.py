from pydoc import describe

from shop import app, db
from shop.models import User, Item

# with app.app_context():
#     users = Item.query.all()
#     for user in users:
#         print(user.name, user.img)

with app.app_context():
    db.create_all()
    item = Item(name = "Coconut shell", price = 5, barcode = "barcode", description = "desc", amount = 40)
    item2 = Item(name = "Coconut shell2", price = 15, barcode = "barcode2", description = "desc2", amount = 40)
    item3 = Item(name = "Coconut shell3", price = 25, barcode = "barcode3", description = "desc3", amount = 40)
    item4 = Item(name = "Coconut shell4", price = 35, barcode = "barcode4", description = "desc4", amount = 40)
    db.session.add(item)
    db.session.add(item2)
    db.session.add(item3)
    db.session.add(item4)
    db.session.commit()