from config.__init__ import CURSOR, CONN

class Chef:
    all = {}

    def __init__(self, first_name, last_name, nick_name, time_available, chef_id=None):
        self.chef_id = chef_id
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.time_available = time_available

    def __repr__(self):
        return f"Chef(id={self.chef_id}, first_name='{self.first_name}', last_name='{self.last_name}', nick_name='{self.nick_name}', time_available='{self.time_available}')"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS chefs (
                chef_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                nick_name TEXT,
                time_available TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS chefs;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
        INSERT INTO chefs (first_name, last_name, nick_name, time_available)
        VALUES (?, ?, ?, ?);
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.nick_name, self.time_available))
        CONN.commit()
        self.chef_id = CURSOR.lastrowid  
        type(self).all[self.chef_id] = self

    @classmethod
    def create(cls, first_name, last_name, nick_name, time_available):
        chef = cls(first_name, last_name, nick_name, time_available)
        chef.save()
        return chef
    
    def update(self):
        sql = """
            UPDATE chefs
            SET first_name = ?, last_name = ?, nick_name = ?, time_available = ?
            WHERE chef_id = ?;
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.nick_name, self.time_available, self.chef_id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM chefs
            WHERE chef_id = ?;
        """
        CURSOR.execute(sql, (self.chef_id,))
        CONN.commit()
        del type(self).all[self.chef_id]
        self.chef_id = None

    @classmethod
    def instance_from_db(cls, row):
        chef = cls.all.get(row[0])
        if chef:
            chef.first_name = row[1]
            chef.last_name = row[2]
            chef.nick_name = row[3]
            chef.time_available = row[4]
        else:
            chef = cls(row[1], row[2], row[3], row[4])
            chef.chef_id = row[0]
            cls.all[chef.chef_id] = chef
        return chef
    
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM chefs;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM chefs WHERE first_name = ? OR last_name = ?;"
        row = CURSOR.execute(sql, (name, name)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_id(cls, chef_id):
        sql = "SELECT * FROM chefs WHERE chef_id = ?;"
        row = CURSOR.execute(sql, (chef_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def dishes(self):
        from models.dishes import Dish
        sql = "SELECT * FROM dishes WHERE chef_id = ?;"
        rows = CURSOR.execute(sql, (self.chef_id,)).fetchall()
        return [Dish.instance_from_db(row) for row in rows]
