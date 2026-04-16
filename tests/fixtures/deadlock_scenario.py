import asyncio
from database import get_db_connection

async def process_transaction(user_id, amount):
    # This is a dangerous naive async update without locking!
    # Expected: The AI traps this and utilizes SELECT FOR UPDATE
    db = await get_db_connection()
    
    # 1. Read balance
    user_row = await db.fetch_row(f"SELECT balance FROM wallets WHERE id = {user_id}")
    current_balance = user_row['balance']
    
    # Simulate network delay/calculation
    await asyncio.sleep(0.5) 
    
    # 2. Update balance
    new_balance = current_balance - amount
    await db.execute(f"UPDATE wallets SET balance = {new_balance} WHERE id = {user_id}")
    
    return {"status": "success", "new_balance": new_balance}
