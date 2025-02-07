import unittest

from flask import json

from openapi_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities  # noqa: E501
from openapi_server.models.problem_details import ProblemDetails  # noqa: E501
from openapi_server.test import BaseTestCase


class TestIndividualRegisteredDMETypeProductionCapabilityController(BaseTestCase):
    """IndividualRegisteredDMETypeProductionCapabilityController integration test stubs"""

    def test_production_capabilities_registration_id_delete(self):
        """Test case for production_capabilities_registration_id_delete

        
        """
        headers = { 
            'Accept': 'application/problem+json',
        }
        response = self.client.open(
            '/data-registration/v2/production-capabilities/{registration_id}'.format(registration_id='registration_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_production_capabilities_registration_id_get(self):
        """Test case for production_capabilities_registration_id_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/data-registration/v2/production-capabilities/{registration_id}'.format(registration_id='registration_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_production_capabilities_registration_id_put(self):
        """Test case for production_capabilities_registration_id_put

        
        """
        dme_type_related_capabilities = {"dmeTypeDefinition":{"metadata":{"rat":["rat","rat"],"dataCategory":["dataCategory","dataCategory"]},"dmeTypeId":{"namespace":"namespace","name":"name","version":"version"},"dataDeliveryMechanisms":[{"dataDeliveryMethod":"","kafkaDeliveryConfiguration":{"retentionMs":1,"retentionBytes":6,"cleanUpPolicy":"cleanUpPolicy","numPartitions":0,"compressionType":"compressionType"}},{"dataDeliveryMethod":"","kafkaDeliveryConfiguration":{"retentionMs":1,"retentionBytes":6,"cleanUpPolicy":"cleanUpPolicy","numPartitions":0,"compressionType":"compressionType"}}],"dataProductionSchema":"{}","dataDeliverySchemas":[{"schema":"schema","deliverySchemaId":"deliverySchemaId","type":"JSON_SCHEMA"},{"schema":"schema","deliverySchemaId":"deliverySchemaId","type":"JSON_SCHEMA"}]},"dataDeliveryModes":["ONE_TIME","ONE_TIME"],"dataAccessEndpoint":{"ipv6Addr":"ipv6Addr","grantTypes":["CLIENT_CREDENTIALS","CLIENT_CREDENTIALS"],"securityMethods":["PSK","PSK"],"fqdn":"fqdn","port":39072,"apiPrefix":"apiPrefix","ipv4Addr":"ipv4Addr"},"constraints":"{}"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/data-registration/v2/production-capabilities/{registration_id}'.format(registration_id='registration_id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(dme_type_related_capabilities),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
