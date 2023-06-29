"""
Creating the FastAPI application
"""
from fastapi import FastAPI
from app.routers.wrapper import router as dome_router
from app import __version__


def create_app():
    """
    Create the FastAPI app and include a DOME 4.0 router.

    Returns:
        A FastAPI app with a DOME 4.0 router included.
    """
    app = FastAPI(
        title="{{cookiecutter.project_name}} connector",
        version=__version__,
        description="This is the connector for {{cookiecutter.project_name}}",
    )

    app.include_router(dome_router)
    return app


APP = create_app()
