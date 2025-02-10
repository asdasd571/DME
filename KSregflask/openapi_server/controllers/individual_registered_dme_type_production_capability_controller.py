import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities  # noqa: E501
from openapi_server.models.problem_details import ProblemDetails  # noqa: E501
from openapi_server import util


import connexion
from typing import Union, Tuple, Dict
from openapi_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities
from openapi_server.models.problem_details import ProblemDetails

# 가상의 DB (실제 환경에서는 SQLAlchemy 또는 MongoDB 등 사용)
DATABASE = {}

def production_capabilities_registration_id_delete(registration_id):  # noqa: E501
    """production_capabilities_registration_id_delete

    To deregister DME type production capabilities

    :param registration_id: 
    :type registration_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]]
    """
    if registration_id not in DATABASE:
        return ProblemDetails(
            title="Not Found",
            detail=f"Registration ID {registration_id} not found.",
            status=404
        ), 404
    
    del DATABASE[registration_id]  # 데이터 삭제
    return None, 204  # 204 No Content (삭제 성공)


def production_capabilities_registration_id_get(registration_id):  # noqa: E501
    """production_capabilities_registration_id_get

    To query DME type production capabilities that it has previously registered

    :param registration_id: 
    :type registration_id: str

    :rtype: Union[DmeTypeRelatedCapabilities, Tuple[DmeTypeRelatedCapabilities, int], Tuple[DmeTypeRelatedCapabilities, int, Dict[str, str]]]
    """
    if registration_id not in DATABASE:
        return ProblemDetails(
            title="Not Found",
            detail=f"Registration ID {registration_id} not found.",
            status=404
        ), 404

    return DATABASE[registration_id], 200  # 200 OK (데이터 반환)


def production_capabilities_registration_id_put(registration_id, body):  # noqa: E501
    """production_capabilities_registration_id_put

    To update DME type production capabilities that it has previously registered

    :param registration_id: 
    :type registration_id: str
    :param dme_type_related_capabilities: 
    :type dme_type_related_capabilities: dict | bytes

    :rtype: Union[DmeTypeRelatedCapabilities, Tuple[DmeTypeRelatedCapabilities, int], Tuple[DmeTypeRelatedCapabilities, int, Dict[str, str]]]
    """
    dme_type_related_capabilities = body
    if connexion.request.is_json:
        dme_type_related_capabilities = DmeTypeRelatedCapabilities.from_dict(connexion.request.get_json())  # noqa: E501

    if registration_id not in DATABASE:
        return ProblemDetails(
            title="Not Found",
            detail=f"Registration ID {registration_id} not found.",
            status=404
        ), 404

    DATABASE[registration_id] = dme_type_related_capabilities  # 데이터 업데이트
    return dme_type_related_capabilities, 200  # 200 OK (업데이트 성공)
