# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import StrictStr  # noqa: F401
from typing import Any  # noqa: F401
from openapi_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401


def test_production_capabilities_registration_id_delete(client: TestClient):
    """Test case for production_capabilities_registration_id_delete

    
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/production-capabilities/{registrationId}".format(registrationId='registration_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_production_capabilities_registration_id_get(client: TestClient):
    """Test case for production_capabilities_registration_id_get

    
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/production-capabilities/{registrationId}".format(registrationId='registration_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_production_capabilities_registration_id_put(client: TestClient):
    """Test case for production_capabilities_registration_id_put

    
    """
    dme_type_related_capabilities = {"dme_type_definition":{"metadata":{"rat":["rat","rat"],"data_category":["dataCategory","dataCategory"]},"dme_type_id":{"namespace":"namespace","name":"name","version":"version"},"data_delivery_mechanisms":[{"data_delivery_method":"","kafka_delivery_configuration":{"retention_ms":1,"retention_bytes":6,"clean_up_policy":"cleanUpPolicy","num_partitions":0,"compression_type":"compressionType"}},{"data_delivery_method":"","kafka_delivery_configuration":{"retention_ms":1,"retention_bytes":6,"clean_up_policy":"cleanUpPolicy","num_partitions":0,"compression_type":"compressionType"}}],"data_production_schema":"{}","data_delivery_schemas":[{"schema":"schema","delivery_schema_id":"deliverySchemaId","type":"JSON_SCHEMA"},{"schema":"schema","delivery_schema_id":"deliverySchemaId","type":"JSON_SCHEMA"}]},"data_delivery_modes":["ONE_TIME","ONE_TIME"],"data_access_endpoint":{"ipv6_addr":"ipv6Addr","grant_types":["CLIENT_CREDENTIALS","CLIENT_CREDENTIALS"],"security_methods":["PSK","PSK"],"fqdn":"fqdn","port":39072,"api_prefix":"apiPrefix","ipv4_addr":"ipv4Addr"},"constraints":"{}"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/production-capabilities/{registrationId}".format(registrationId='registration_id_example'),
    #    headers=headers,
    #    json=dme_type_related_capabilities,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

