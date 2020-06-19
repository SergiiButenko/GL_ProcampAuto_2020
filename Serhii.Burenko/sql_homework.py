import psycopg2


class DBConnection:

    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        try:
            self.connection = psycopg2.connect(host=host, port=port, user=user, password=password, database=db)
            self.cursor = self.connection.cursor()
        except psycopg2.Error as ex:
            print('Cannot connect to te DB. {0:s}'.format(ex))
            raise

    def destroy_connection(self):
        self.cursor.close()
        self.connection.close()

    def select(self, table, names, items):
        # Prepare SQL query to SELECT required records
        tmp = ''
        if names is not None:
            for name in names:
                tmp += '{0:s}, '.format(name)
            tmp = tmp[:len(tmp) - 2]  # -2 for remove in last element ', '
        else:
            tmp = '*'
        sql_query = 'SELECT {0:s} FROM {1:s} WHERE '.format(tmp, table)
        where = ''
        for key, value in items.iteritems():
            where += '{0:}=\'{1:}\' and '.format(key, value)
        sql_query += where[:len(where) - 4]  # for remove in last element 'and '

        try:
            self.cursor.execute(sql_query)
            return self.cursor.fetchall()
        except psycopg2.Error as ex:
            print('Error while selecting. {0:s}'.format(ex))
            raise

    def update(self, table, old_value, new_value):
        # Prepare SQL query to UPDATE required records
        sql_query = 'UPDATE {0} SET '.format(table)
        name = list()
        where = list()
        for key, value in new_value.items():
            name.append('{0:}=\'{1:}\''.format(key, value))
        for key, value in old_value.items():
            where.append('{0:}=\'{1:}\''.format(key, value))
        sql_query = "{0:} {1:} WHERE {2:}".format(sql_query, ', '.join(name), ' and '.join(where))

        try:
            self.cursor.execute(sql_query)
            return self.connection.commit()
        except psycopg2.Error as ex:
            print('Error while updating. {0:s}'.format(ex))
            raise
