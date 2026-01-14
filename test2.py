import sqlite3
import pandas as pd


def view_database(db_path):
    # 连接数据库
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 获取所有表名
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("数据库中的表:", [table[0] for table in tables])

    # 查看每个表的结构和数据
    for table in tables:
        table_name = table[0]
        print(f"\n=== 表: {table_name} ===")

        # 获取表结构
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        print("表结构:")
        for col in columns:
            print(f"  {col[1]} ({col[2]})")

        # 查看前几行数据
        df = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 5", conn)
        print(f"前5行数据:")
        print(df)

    conn.close()


# 使用示例
view_database('example.db')