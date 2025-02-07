from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    dme_type_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/dme-types/{dme_type_id}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 400:
        return None
    if response.status_code == 401:
        return None
    if response.status_code == 403:
        return None
    if response.status_code == 404:
        return None
    if response.status_code == 406:
        return None
    if response.status_code == 414:
        return None
    if response.status_code == 429:
        return None
    if response.status_code == 500:
        return None
    if response.status_code == 502:
        return None
    if response.status_code == 503:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dme_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """To obtain information about an individual DME type.

    Args:
        dme_type_id (str): The DmeTypeId is constructed based on the three parts separated by “:“
            (colon) {dmeTypeId} = {namespace}:{name}:{version}. See
            O-RAN.WG2.R1AP_DataRegistration.yaml#/components/schemas/DmeTypeIdStruct for the
            definition of “namespace“, “name“ and “version“.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dme_type_id=dme_type_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    dme_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """To obtain information about an individual DME type.

    Args:
        dme_type_id (str): The DmeTypeId is constructed based on the three parts separated by “:“
            (colon) {dmeTypeId} = {namespace}:{name}:{version}. See
            O-RAN.WG2.R1AP_DataRegistration.yaml#/components/schemas/DmeTypeIdStruct for the
            definition of “namespace“, “name“ and “version“.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dme_type_id=dme_type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
