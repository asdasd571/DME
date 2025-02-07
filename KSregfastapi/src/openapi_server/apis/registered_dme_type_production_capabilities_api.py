# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.registered_dme_type_production_capabilities_api_base import BaseRegisteredDMETypeProductionCapabilitiesApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities
from openapi_server.models.problem_details import ProblemDetails


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/production-capabilities",
    responses={
        201: {"model": DmeTypeRelatedCapabilities, "description": "Success case 201 created"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        401: {"model": ProblemDetails, "description": "Unauthorized"},
        403: {"model": ProblemDetails, "description": "Forbidden"},
        404: {"model": ProblemDetails, "description": "Not Found"},
        405: {"model": ProblemDetails, "description": "Method Not Allowed"},
        409: {"model": ProblemDetails, "description": "Conflict"},
        413: {"model": ProblemDetails, "description": "Payload Too Large"},
        415: {"model": ProblemDetails, "description": "Unsupported Media Type"},
        429: {"model": ProblemDetails, "description": "Too Many Requests"},
        500: {"model": ProblemDetails, "description": "Internal Server Error"},
        502: {"model": ProblemDetails, "description": "Bad Gateway"},
        503: {"model": ProblemDetails, "description": "Service Unavailable"},
    },
    tags=["Registered DME type production capabilities"],
    response_model_by_alias=True,
)
async def production_capabilities_post(
    dme_type_related_capabilities: DmeTypeRelatedCapabilities = Body(None, description=""),
) -> DmeTypeRelatedCapabilities:
    """To register DME type production capabilities"""
    if not BaseRegisteredDMETypeProductionCapabilitiesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseRegisteredDMETypeProductionCapabilitiesApi.subclasses[0]().production_capabilities_post(dme_type_related_capabilities)
