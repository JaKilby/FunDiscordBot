import psycopg2
import os


class CreditManager(object):
    def __init__(self):
        self.conn = psycopg2.connect(os.environ["DATABASE_URL"], sslmode="require")

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS credits
                            (player text, credits integer)''')
        # c.execute("INSERT INTO credits VALUES ('kilbo', 20)")
        self.conn.commit()

    def check_credits(self, player_name):
        c = self.conn.cursor()
        c.execute("SELECT credits FROM credits WHERE player = ?", (player_name,))
        credit_statement = c.fetchone()
        if credit_statement is None:
            c.execute("INSERT INTO credits VALUES (?, 0)", (player_name,))
            self.conn.commit()
            return self.check_credits(player_name)
        return credit_statement[0]

    def give_credits(self, player_name, credits):
        c = self.conn.cursor()
        current_credits = self.check_credits(player_name)
        total_credits = credits + current_credits
        if total_credits < 0:
            total_credits = 0
        c.execute("UPDATE credits SET credits = ? WHERE player = ?", (total_credits, player_name))
        self.conn.commit()

if __name__ == "__main__":
    manager = CreditManager()
    manager.create_table()
    print(manager.check_credits("Scetched"))
    manager.give_credits("kilbo", 20)
    print(manager.check_credits("kilbo"))