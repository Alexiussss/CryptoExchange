import aiosqlite

async def add_user(user_id):
    async with aiosqlite.connect('db.db') as db:
        await db.execute('INSERT INTO users (user_id) VALUE (?)', (user_id))
        await db.commit()