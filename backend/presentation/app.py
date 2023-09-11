from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from presentation.users_router import router as users_router
from presentation.teams_router import router as teams_router
from presentation.hacks_router import router as hacks_router
from presentation.publications_router import router as publications_router

def create_app() -> FastAPI:
    fastapi_app = FastAPI()

    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    fastapi_app.include_router(users_router)
    fastapi_app.include_router(teams_router)
    fastapi_app.include_router(hacks_router)
    fastapi_app.include_router(publications_router)

    return fastapi_app

