import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities  # noqa: E501
from openapi_server.models.problem_details import ProblemDetails  # noqa: E501
from openapi_server import util


def production_capabilities_post(body):  # noqa: E501
    """production_capabilities_post

    To register DME type production capabilities # noqa: E501

    :param dme_type_related_capabilities: 
    :type dme_type_related_capabilities: dict | bytes

    :rtype: Union[DmeTypeRelatedCapabilities, Tuple[DmeTypeRelatedCapabilities, int], Tuple[DmeTypeRelatedCapabilities, int, Dict[str, str]]
    """
    dme_type_related_capabilities = body
    if connexion.request.is_json:
        dme_type_related_capabilities = DmeTypeRelatedCapabilities.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
