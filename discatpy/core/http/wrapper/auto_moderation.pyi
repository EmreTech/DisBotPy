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

from typing import List

from discord_typings import AutoModerationActionData, AutoModerationTriggerMetadataData

from ...types import MISSING, MissingOr, Snowflake

class AutoModerationEndpointMixin:
    async def get_auto_moderation_rule(
        self, guild_id: Snowflake, auto_moderation_rule_id: Snowflake
    ): ...
    async def list_auto_moderation_rules_for_guild(self, guild_id: Snowflake): ...
    async def create_auto_moderation_rule(
        self,
        guild_id: Snowflake,
        *,
        name: str,
        event_type: int,
        trigger_type: int,
        trigger_metadata: MissingOr[AutoModerationTriggerMetadataData] = MISSING,
        actions: List[AutoModerationActionData],
        enabled: MissingOr[bool] = MISSING,
        exempt_roles: MissingOr[List[Snowflake]] = MISSING,
        exempt_channels: MissingOr[List[Snowflake]] = MISSING,
    ): ...
    async def modify_auto_moderation_rule(
        self,
        guild_id: Snowflake,
        *,
        name: MissingOr[str] = MISSING,
        event_type: MissingOr[int] = MISSING,
        trigger_type: MissingOr[int] = MISSING,
        trigger_metadata: MissingOr[AutoModerationTriggerMetadataData] = MISSING,
        actions: MissingOr[List[AutoModerationActionData]] = MISSING,
        enabled: MissingOr[bool] = MISSING,
        exempt_roles: MissingOr[List[Snowflake]] = MISSING,
        exempt_channels: MissingOr[List[Snowflake]] = MISSING,
    ): ...
    async def delete_auto_moderation_rule(
        self, guild_id: Snowflake, auto_moderation_rule_id: Snowflake
    ): ...
