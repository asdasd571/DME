import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities  # noqa: E501
from openapi_server.models.problem_details import ProblemDetails  # noqa: E501
from openapi_server import util


def production_capabilities_registration_id_delete(registration_id):  # noqa: E501
    """production_capabilities_registration_id_delete

    To deregister DME type production capabilities # noqa: E501

    :param registration_id: 
    :type registration_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def production_capabilities_registration_id_get(registration_id):  # noqa: E501
    """production_capabilities_registration_id_get

    To query DME type production capabilities that it has previously registered # noqa: E501

    :param registration_id: 
    :type registration_id: str

    :rtype: Union[DmeTypeRelatedCapabilities, Tuple[DmeTypeRelatedCapabilities, int], Tuple[DmeTypeRelatedCapabilities, int, Dict[str, str]]
    """
    return 'do some magic!'


def production_capabilities_registration_id_put(registration_id, body):  # noqa: E501
    """production_capabilities_registration_id_put

    To update DME type production capabilities that it has previously registered # noqa: E501

    :param registration_id: 
    :type registration_id: str
    :param dme_type_related_capabilities: 
    :type dme_type_related_capabilities: dict | bytes

    :rtype: Union[DmeTypeRelatedCapabilities, Tuple[DmeTypeRelatedCapabilities, int], Tuple[DmeTypeRelatedCapabilities, int, Dict[str, str]]
    """
    dme_type_related_capabilities = body
    if connexion.request.is_json:
        dme_type_related_capabilities = DmeTypeRelatedCapabilities.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
