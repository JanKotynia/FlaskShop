from pydoc import describe

from shop import app, db
from shop.models import User, Item

# with app.app_context():
#     users = Item.query.all()
#     for user in users:
#         print(user.name, user.img)

with app.app_context():
    db.create_all()
    if not Item.query.first():
        items = [
            Item(name="Coconut shell", price=5, barcode="barcode", description="desc", amount=40),
            Item(name="Coconut shell2", price=15, barcode="barcode2", description="desc2", amount=40),
            Item(name="Coconut shell3", price=25, barcode="barcode3", description="desc3", amount=40),
            Item(name="Coconut shell4", price=35, barcode="barcode4", description="desc4", amount=40),
        ]
        db.session.add_all(items)
        db.session.commit()
    db.session.commit()