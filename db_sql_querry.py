from shop import app, db
from shop.models import User

# with app.app_context():
#     users = User.query.all()
#     for user in users:
#         print(user.username, user.email_address)

with app.app_context():
    db.create_all()