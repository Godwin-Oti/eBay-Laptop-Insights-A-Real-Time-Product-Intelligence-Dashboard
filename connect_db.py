import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Get the DB URL
db_url = os.getenv("DATABASE_URL")

# Connect to PostgreSQL and create table
try:
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    print("✅ Connected to Railway PostgreSQL!")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS laptops (
        id SERIAL PRIMARY KEY,
        title TEXT,
        brand TEXT,
        price FLOAT,
        shipping_price FLOAT,
        shipping_type TEXT,
        availability TEXT,
        seller_name TEXT,
        seller_rating_pct FLOAT,
        seller_score INT,
        top_rated_seller BOOLEAN,
        collected_at TIMESTAMP DEFAULT NOW()
    );
    """)
    conn.commit()
    print("✅ Table 'laptops' created (or already exists).")

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Error:", e)
