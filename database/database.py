import sqlite3

from config import DATABASE_PATH


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)

    async def _read(self, query):
        c = self.connection.cursor()
        c.execute(query)

        return c.fetchall()

    async def _write(self, query):
        c = self.connection.cursor()
        c.execute(query)

        c.close()
        self.connection.commit()


class UserDatabase(Database):
    async def add_user(self, user_id):
        if await self.user_exists(user_id):
            return

        await self._write(f"INSERT INTO users (user_id) VALUES ('{user_id}', 0)")

    async def get_user(self, user_id):
        return await self._read(f'SELECT * FROM users WHERE user_id = {user_id}')

    async def get_count_of_users(self):
        return await self._read('SELECT COUNT() FROM users')

    async def user_exists(self, user_id):
        return await self.get_user(user_id)

    async def update_user_lang(self, user_id, lang):
        await self._write(f"UPDATE users SET lang = '{lang}' WHERE user_id = {user_id}")
