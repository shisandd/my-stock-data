# app.py
from fastapi import FastAPI
from a_stock_data import your_modules  # 根据 a-stock-data 结构引用核心功能

app = FastAPI()

@app.get("/stock/{code}")
def stock_info(code: str):
    # 调用 a-stock-data 提供的函数获取股票数据
    data = your_modules.get_stock_info(code)  # 示例
    return data
