# coding: utf-8

"""
    Data registration service

    API for Data registration service. © 2024, O-RAN ALLIANCE. All rights reserved. 

    The version of the OpenAPI document: 2.0.0-alpha.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from fastapi import FastAPI

from openapi_server.apis.individual_registered_dme_type_production_capability_api import router as IndividualRegisteredDMETypeProductionCapabilityApiRouter
from openapi_server.apis.registered_dme_type_production_capabilities_api import router as RegisteredDMETypeProductionCapabilitiesApiRouter

app = FastAPI(
    title="Data registration service",
    description="API for Data registration service. © 2024, O-RAN ALLIANCE. All rights reserved. ",
    version="2.0.0-alpha.1",
)

app.include_router(IndividualRegisteredDMETypeProductionCapabilityApiRouter)
app.include_router(RegisteredDMETypeProductionCapabilitiesApiRouter)
