import sqlite3

DB_NAME = "translations.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_language TEXT NOT NULL,
            target_language TEXT NOT NULL,
            user_input TEXT NOT NULL,
            translated_output TEXT NOT NULL,
            date_created TEXT DEFAULT (datetime('now', 'localtime'))
        )
    ''')
    conn.commit()
    conn.close()

def insert_translation(src, tgt, user_input, translated_output):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO history (source_language, target_language, user_input, translated_output)
        VALUES (?, ?, ?, ?)
    ''', (src, tgt, user_input, translated_output))
    conn.commit()
    conn.close()

def get_last_translations(n=5):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        SELECT source_language, target_language, user_input, translated_output, date_created
        FROM history
        ORDER BY date_created DESC
        LIMIT ?
    ''', (n,))
    rows = c.fetchall()
    conn.close()
    return rows
