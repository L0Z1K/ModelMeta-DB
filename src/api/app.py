from logging import getLogger

from fastapi import FastAPI
from src.api.routers import api
from src.configurations import APIConfigurations
from src.db.initialize import initialize_table
from src.db.database import engine

logger = getLogger(__name__)

initialize_table(engine=engine, checkfirst=True)

app = FastAPI(
    title=APIConfigurations.title,
    description=APIConfigurations.description,
    version=APIConfigurations.version,
)
app.include_router(
    api.router, prefix=f"/v{APIConfigurations.version}/api", tags=["api"]
)
