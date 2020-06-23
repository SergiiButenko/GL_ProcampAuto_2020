import psycopg2

class Db:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = psycopg2.connect(host=host, database=database, user=user, password=password)
        self.cur = self.connection.cursor()

    def destroy(self):
        self.cur.close()
        self.connection.close()

    def select_aircrafts(self):
        self.cur.execute("select * from bookings.aircrafts;")
        self.connection.commit()

    def update_arrival_airport(self, flight_no, arrival_airport):
        self.cur.execute(f"UPDATE flights SET arrival_airport = '{arrival_airport}' where flight_no = '{flight_no}';")
        self.connection.commit()