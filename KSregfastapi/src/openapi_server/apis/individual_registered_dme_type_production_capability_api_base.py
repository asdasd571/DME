# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictStr
from typing import Any
from openapi_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities
from openapi_server.models.problem_details import ProblemDetails


class BaseIndividualRegisteredDMETypeProductionCapabilityApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseIndividualRegisteredDMETypeProductionCapabilityApi.subclasses = BaseIndividualRegisteredDMETypeProductionCapabilityApi.subclasses + (cls,)
    async def production_capabilities_registration_id_delete(
        self,
        registrationId: StrictStr,
    ) -> None:
        """To deregister DME type production capabilities"""
        ...


    async def production_capabilities_registration_id_get(
        self,
        registrationId: StrictStr,
    ) -> DmeTypeRelatedCapabilities:
        """To query DME type production capabilities that it has previously registered"""
        ...


    async def production_capabilities_registration_id_put(
        self,
        registrationId: StrictStr,
        dme_type_related_capabilities: DmeTypeRelatedCapabilities,
    ) -> DmeTypeRelatedCapabilities:
        """To update DME type production capabilities that it has previously registered"""
        ...
