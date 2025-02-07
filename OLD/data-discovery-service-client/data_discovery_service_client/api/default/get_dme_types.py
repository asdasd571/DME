from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identity_namespace: Union[Unset, str] = UNSET,
    identity_name: Union[Unset, str] = UNSET,
    data_category: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["identity-namespace"] = identity_namespace

    params["identity-name"] = identity_name

    json_data_category: Union[Unset, list[str]] = UNSET
    if not isinstance(data_category, Unset):
        json_data_category = data_category

    params["data-category"] = json_data_category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dme-types",
        "params": params,
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
    *,
    client: Union[AuthenticatedClient, Client],
    identity_namespace: Union[Unset, str] = UNSET,
    identity_name: Union[Unset, str] = UNSET,
    data_category: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    """To discover the available DME types

    Args:
        identity_namespace (Union[Unset, str]):
        identity_name (Union[Unset, str]):
        data_category (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identity_namespace=identity_namespace,
        identity_name=identity_name,
        data_category=data_category,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    identity_namespace: Union[Unset, str] = UNSET,
    identity_name: Union[Unset, str] = UNSET,
    data_category: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    """To discover the available DME types

    Args:
        identity_namespace (Union[Unset, str]):
        identity_name (Union[Unset, str]):
        data_category (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identity_namespace=identity_namespace,
        identity_name=identity_name,
        data_category=data_category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
