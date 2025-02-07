# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.individual_registered_dme_type_production_capability_api_base import BaseIndividualRegisteredDMETypeProductionCapabilityApi
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
from pydantic import StrictStr
from typing import Any
from openapi_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities
from openapi_server.models.problem_details import ProblemDetails


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.delete(
    "/production-capabilities/{registrationId}",
    responses={
        204: {"description": "The registration was deleted"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        401: {"model": ProblemDetails, "description": "Unauthorized"},
        403: {"model": ProblemDetails, "description": "Forbidden"},
        404: {"model": ProblemDetails, "description": "Not Found"},
        429: {"model": ProblemDetails, "description": "Too Many Requests"},
        500: {"model": ProblemDetails, "description": "Internal Server Error"},
        502: {"model": ProblemDetails, "description": "Bad Gateway"},
        503: {"model": ProblemDetails, "description": "Service Unavailable"},
    },
    tags=["Individual registered DME type production capability"],
    response_model_by_alias=True,
)
async def production_capabilities_registration_id_delete(
    registrationId: StrictStr = Path(..., description=""),
) -> None:
    """To deregister DME type production capabilities"""
    if not BaseIndividualRegisteredDMETypeProductionCapabilityApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseIndividualRegisteredDMETypeProductionCapabilityApi.subclasses[0]().production_capabilities_registration_id_delete(registrationId)


@router.get(
    "/production-capabilities/{registrationId}",
    responses={
        200: {"model": DmeTypeRelatedCapabilities, "description": "Success case 200 with queried information"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        401: {"model": ProblemDetails, "description": "Unauthorized"},
        403: {"model": ProblemDetails, "description": "Forbidden"},
        404: {"model": ProblemDetails, "description": "Not Found"},
        406: {"model": ProblemDetails, "description": "Not Acceptable"},
        429: {"model": ProblemDetails, "description": "Too Many Requests"},
        500: {"model": ProblemDetails, "description": "Internal Server Error"},
        502: {"model": ProblemDetails, "description": "Bad Gateway"},
        503: {"model": ProblemDetails, "description": "Service Unavailable"},
    },
    tags=["Individual registered DME type production capability"],
    response_model_by_alias=True,
)
async def production_capabilities_registration_id_get(
    registrationId: StrictStr = Path(..., description=""),
) -> DmeTypeRelatedCapabilities:
    """To query DME type production capabilities that it has previously registered"""
    if not BaseIndividualRegisteredDMETypeProductionCapabilityApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseIndividualRegisteredDMETypeProductionCapabilityApi.subclasses[0]().production_capabilities_registration_id_get(registrationId)


@router.put(
    "/production-capabilities/{registrationId}",
    responses={
        200: {"model": DmeTypeRelatedCapabilities, "description": "Success case 200 with updated information"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        401: {"model": ProblemDetails, "description": "Unauthorized"},
        403: {"model": ProblemDetails, "description": "Forbidden"},
        404: {"model": ProblemDetails, "description": "Not Found"},
        406: {"model": ProblemDetails, "description": "Not Acceptable"},
        411: {"model": ProblemDetails, "description": "Length Required"},
        413: {"model": ProblemDetails, "description": "Payload Too Large"},
        415: {"model": ProblemDetails, "description": "Unsupported Media Type"},
        429: {"model": ProblemDetails, "description": "Too Many Requests"},
        500: {"model": ProblemDetails, "description": "Internal Server Error"},
        502: {"model": ProblemDetails, "description": "Bad Gateway"},
        503: {"model": ProblemDetails, "description": "Service Unavailable"},
    },
    tags=["Individual registered DME type production capability"],
    response_model_by_alias=True,
)
async def production_capabilities_registration_id_put(
    registrationId: StrictStr = Path(..., description=""),
    dme_type_related_capabilities: DmeTypeRelatedCapabilities = Body(None, description=""),
) -> DmeTypeRelatedCapabilities:
    """To update DME type production capabilities that it has previously registered"""
    if not BaseIndividualRegisteredDMETypeProductionCapabilityApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseIndividualRegisteredDMETypeProductionCapabilityApi.subclasses[0]().production_capabilities_registration_id_put(registrationId, dme_type_related_capabilities)
