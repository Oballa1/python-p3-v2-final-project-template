from config.__init__ import CURSOR, CONN

class Meal:
    all = {}

    def __init__(self, name, preparation_time, days_prepared, chef_id, meal_id=None):
        self.meal_id = meal_id
        self.name = name
        self.preparation_time = preparation_time
        self.days_prepared = days_prepared
        self.chef_id = chef_id

    def __repr__(self):
        return f"Meal(id={self.meal_id}, name='{self.name}', preparation_time='{self.preparation_time}', days_prepared='{self.days_prepared}', chef_id={self.chef_id}')"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS meals (
                meal_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                preparation_time TEXT,
                days_prepared TEXT,
                chef_id INTEGER,
                FOREIGN KEY(chef_id) REFERENCES chefs(chef_id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS meals;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
        INSERT INTO meals (name, preparation_time, days_prepared, chef_id)
        VALUES (?, ?, ?, ?);
        """
        CURSOR.execute(sql, (self.name, self.preparation_time, self.days_prepared, self.chef_id))
        CONN.commit()
        self.meal_id = CURSOR.lastrowid
        type(self).all[self.meal_id] = self

    @classmethod
    def create(cls, name, preparation_time, days_prepared, chef_id):
        meal = cls(name, preparation_time, days_prepared, chef_id)
        meal.save()
        return meal

    def update(self):
        sql = """
            UPDATE meals
            SET name = ?, preparation_time = ?, days_prepared = ?, chef_id = ?
            WHERE meal_id = ?;
        """
        CURSOR.execute(sql, (self.name, self.preparation_time, self.days_prepared, self.chef_id, self.meal_id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM meals
            WHERE meal_id = ?;
        """
        CURSOR.execute(sql, (self.meal_id,))
        CONN.commit()
        del type(self).all[self.meal_id]
        self.meal_id = None

    @classmethod
    def instance_from_db(cls, row):
        meal = cls.all.get(row[0])
        if meal:
            meal.name = row[1]
            meal.preparation_time = row[2]
            meal.days_prepared = row[3]
            meal.chef_id = row[4]
        else:
            meal = cls(row[1], row[2], row[3], row[4])
            meal.meal_id = row[0]
            cls.all[meal.meal_id] = meal
        return meal
    
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM meals;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM meals WHERE name = ?;"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_id(cls, meal_id):
        sql = "SELECT * FROM meals WHERE meal_id = ?;"
        row = CURSOR.execute(sql, (meal_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def chef(self):
        from models.chef import Chef
        return Chef.find_by_id(self.chef_id)
