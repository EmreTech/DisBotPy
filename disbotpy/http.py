"""
The MIT License (MIT)

Copyright (c) 2022-present EmreTech

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from typing import Optional
from urllib.parse import quote as urlquote
import sys
import asyncio
import aiohttp

from . import __version__

__all__ = (
    "Route",
    "HTTPClient"
)

class Route:
    BASE_URL = "https://discord.com/api/v{0}"

    def __init__(self, method: str, path: str, api_ver: int) -> None:
        # Currently, DisBotPy only supports Discord API v9 and v10. 
        # Anything older is depecrated and anything newer has not been release yet.
        # Setting api_ver to 0 means that it will be set to the default (v9)

        if api_ver > 10:
            raise RuntimeError(f"Discord API Version {api_ver} is too new to be used.")
        elif api_ver < 9 and api_ver != 0:
            raise RuntimeError(f"Discord API Version {api_ver} is now discontinued. Use a newer version.")
        else:
            api_ver = 9

        self.method: str = method
        self.path: str = urlquote(path)
        self.api_version: int = api_ver
        self.url: str = self.BASE_URL.format(self.api_version) + self.path

class HTTPClient:
    def __init__(
        self, 
        connector: Optional[aiohttp.BaseConnector] = None
    ):
        self.connector = connector
        self._session = None # initalized by client

        user_agent = "DiscordBot (https://github.com/EmreTech/DisBotPy.git, {0}) Python/{1.major}.{1.minor}.{1.micro} aiohttp/{2}"
        self.user_agent = user_agent.format(__version__, sys.version_info, aiohttp.__version__)

    def recreate_session(self):
        if self._session.closed:
            self._session = aiohttp.ClientSession(
                connector=self.connector
            )

    async def request(self, route: Route, **kwargs):
        headers = {
            "User-Agent": self.user_agent
        }

        token = kwargs.get("token")
        if token is not None:
            headers["Authorization"] = f"Bot {token}"

        json = kwargs.get("json")
        if json is not None:
            headers["Content-Type"] = "application/json"
            # TODO: Convert dict to str
            kwargs["data"] = kwargs.pop("json")

        kwargs["headers"] = headers

        async with self._session.request(route.method, route.url, **kwargs) as response:
            # TODO: Type checking
            data = await response.json()
            resp_code = response.status

            return (data, resp_code)

        