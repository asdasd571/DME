from enum import Enum


class SchemaTypes(str, Enum):
    JSON_SCHEMA = "JSON_SCHEMA"
    XML_SCHEMA = "XML_SCHEMA"

    def __str__(self) -> str:
        return str(self.value)
