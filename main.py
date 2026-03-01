from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "省市區API"}
@app.get("/ provinces")
def provinces():
    return {"success": True, "data": [{"code": "110000", "name": "北京市"}]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
