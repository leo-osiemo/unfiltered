from app import app, db
from models import Farms, Coffee

with app.app_context():
    print('loading...')
    Coffee.query.delete()
    Farms.query.delete()

    from app import db

    db.session.add(Coffee(name="capucino", description="creamy"))
    db.session.add(Coffee(name="latte", description="sour"))

    db.session.add(Farms(name="leoville", farm="capetown"))
    db.session.add(Farms(name="Homeville", farm="abuja"))

    db.session.commit()

    print(".....Done")