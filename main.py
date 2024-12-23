from fastapi import FastAPI

from database.connect import engine, Base
from routers.items import router as items_router


Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")

app.include_router(items_router)
