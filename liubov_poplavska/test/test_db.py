from liubov_poplavska.db.db import Db


def test_select_aircrafts():
    db = Db(host="127.0.0.1", database="demo", user="postgres", password="postgres")
    db.select_aircrafts()
    db.update_arrival_airport('PG0406', 'OVB')