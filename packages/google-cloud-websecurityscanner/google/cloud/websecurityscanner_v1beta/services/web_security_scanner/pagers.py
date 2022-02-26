# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Sequence,
    Tuple,
    Optional,
    Iterator,
)

from google.cloud.websecurityscanner_v1beta.types import crawled_url
from google.cloud.websecurityscanner_v1beta.types import finding
from google.cloud.websecurityscanner_v1beta.types import scan_config
from google.cloud.websecurityscanner_v1beta.types import scan_run
from google.cloud.websecurityscanner_v1beta.types import web_security_scanner


class ListScanConfigsPager:
    """A pager for iterating through ``list_scan_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.websecurityscanner_v1beta.types.ListScanConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``scan_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListScanConfigs`` requests and continue to iterate
    through the ``scan_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.websecurityscanner_v1beta.types.ListScanConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., web_security_scanner.ListScanConfigsResponse],
        request: web_security_scanner.ListScanConfigsRequest,
        response: web_security_scanner.ListScanConfigsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.websecurityscanner_v1beta.types.ListScanConfigsRequest):
                The initial request object.
            response (google.cloud.websecurityscanner_v1beta.types.ListScanConfigsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = web_security_scanner.ListScanConfigsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[web_security_scanner.ListScanConfigsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[scan_config.ScanConfig]:
        for page in self.pages:
            yield from page.scan_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListScanConfigsAsyncPager:
    """A pager for iterating through ``list_scan_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.websecurityscanner_v1beta.types.ListScanConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``scan_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListScanConfigs`` requests and continue to iterate
    through the ``scan_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.websecurityscanner_v1beta.types.ListScanConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[web_security_scanner.ListScanConfigsResponse]],
        request: web_security_scanner.ListScanConfigsRequest,
        response: web_security_scanner.ListScanConfigsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.websecurityscanner_v1beta.types.ListScanConfigsRequest):
                The initial request object.
            response (google.cloud.websecurityscanner_v1beta.types.ListScanConfigsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = web_security_scanner.ListScanConfigsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[web_security_scanner.ListScanConfigsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[scan_config.ScanConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.scan_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListScanRunsPager:
    """A pager for iterating through ``list_scan_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.websecurityscanner_v1beta.types.ListScanRunsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``scan_runs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListScanRuns`` requests and continue to iterate
    through the ``scan_runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.websecurityscanner_v1beta.types.ListScanRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., web_security_scanner.ListScanRunsResponse],
        request: web_security_scanner.ListScanRunsRequest,
        response: web_security_scanner.ListScanRunsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.websecurityscanner_v1beta.types.ListScanRunsRequest):
                The initial request object.
            response (google.cloud.websecurityscanner_v1beta.types.ListScanRunsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = web_security_scanner.ListScanRunsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[web_security_scanner.ListScanRunsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[scan_run.ScanRun]:
        for page in self.pages:
            yield from page.scan_runs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListScanRunsAsyncPager:
    """A pager for iterating through ``list_scan_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.websecurityscanner_v1beta.types.ListScanRunsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``scan_runs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListScanRuns`` requests and continue to iterate
    through the ``scan_runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.websecurityscanner_v1beta.types.ListScanRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[web_security_scanner.ListScanRunsResponse]],
        request: web_security_scanner.ListScanRunsRequest,
        response: web_security_scanner.ListScanRunsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.websecurityscanner_v1beta.types.ListScanRunsRequest):
                The initial request object.
            response (google.cloud.websecurityscanner_v1beta.types.ListScanRunsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = web_security_scanner.ListScanRunsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[web_security_scanner.ListScanRunsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[scan_run.ScanRun]:
        async def async_generator():
            async for page in self.pages:
                for response in page.scan_runs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCrawledUrlsPager:
    """A pager for iterating through ``list_crawled_urls`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.websecurityscanner_v1beta.types.ListCrawledUrlsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``crawled_urls`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCrawledUrls`` requests and continue to iterate
    through the ``crawled_urls`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.websecurityscanner_v1beta.types.ListCrawledUrlsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., web_security_scanner.ListCrawledUrlsResponse],
        request: web_security_scanner.ListCrawledUrlsRequest,
        response: web_security_scanner.ListCrawledUrlsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.websecurityscanner_v1beta.types.ListCrawledUrlsRequest):
                The initial request object.
            response (google.cloud.websecurityscanner_v1beta.types.ListCrawledUrlsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = web_security_scanner.ListCrawledUrlsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[web_security_scanner.ListCrawledUrlsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[crawled_url.CrawledUrl]:
        for page in self.pages:
            yield from page.crawled_urls

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCrawledUrlsAsyncPager:
    """A pager for iterating through ``list_crawled_urls`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.websecurityscanner_v1beta.types.ListCrawledUrlsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``crawled_urls`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCrawledUrls`` requests and continue to iterate
    through the ``crawled_urls`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.websecurityscanner_v1beta.types.ListCrawledUrlsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[web_security_scanner.ListCrawledUrlsResponse]],
        request: web_security_scanner.ListCrawledUrlsRequest,
        response: web_security_scanner.ListCrawledUrlsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.websecurityscanner_v1beta.types.ListCrawledUrlsRequest):
                The initial request object.
            response (google.cloud.websecurityscanner_v1beta.types.ListCrawledUrlsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = web_security_scanner.ListCrawledUrlsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[web_security_scanner.ListCrawledUrlsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[crawled_url.CrawledUrl]:
        async def async_generator():
            async for page in self.pages:
                for response in page.crawled_urls:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFindingsPager:
    """A pager for iterating through ``list_findings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.websecurityscanner_v1beta.types.ListFindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``findings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFindings`` requests and continue to iterate
    through the ``findings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.websecurityscanner_v1beta.types.ListFindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., web_security_scanner.ListFindingsResponse],
        request: web_security_scanner.ListFindingsRequest,
        response: web_security_scanner.ListFindingsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.websecurityscanner_v1beta.types.ListFindingsRequest):
                The initial request object.
            response (google.cloud.websecurityscanner_v1beta.types.ListFindingsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = web_security_scanner.ListFindingsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[web_security_scanner.ListFindingsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[finding.Finding]:
        for page in self.pages:
            yield from page.findings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFindingsAsyncPager:
    """A pager for iterating through ``list_findings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.websecurityscanner_v1beta.types.ListFindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``findings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFindings`` requests and continue to iterate
    through the ``findings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.websecurityscanner_v1beta.types.ListFindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[web_security_scanner.ListFindingsResponse]],
        request: web_security_scanner.ListFindingsRequest,
        response: web_security_scanner.ListFindingsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.websecurityscanner_v1beta.types.ListFindingsRequest):
                The initial request object.
            response (google.cloud.websecurityscanner_v1beta.types.ListFindingsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = web_security_scanner.ListFindingsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[web_security_scanner.ListFindingsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[finding.Finding]:
        async def async_generator():
            async for page in self.pages:
                for response in page.findings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
