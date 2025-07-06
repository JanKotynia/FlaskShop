from shop import app, db
from shop.models import User, Item

# with app.app_context():
#     users = Item.query.all()
#     for user in users:
#         print(user.name, user.img)

with app.app_context():
    db.create_all()
    item = Item("Coconut shell", 5, "barcode", "desc", 40)
    item2 = Item("Coconut shell", 5, "barcode", "desc", 40)
    item3 = Item("Coconut shell", 5, "barcode", "desc", 40)
    item4 = Item("Coconut shell", 5, "barcode", "desc", 40)
    db.session.add(item)
    db.session.add(item2)
    db.session.add(item3)
    db.session.add(item4)
    db.session.commit()