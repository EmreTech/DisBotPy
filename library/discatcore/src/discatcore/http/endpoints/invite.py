# SPDX-License-Identifier: MIT

# this file was auto-generated by scripts/generate_endpoints.py

import typing as t

import discord_typings as dt

from ...types import Unset, UnsetOr
from ..route import Route
from .core import EndpointMixin

__all__ = ("InviteEndpoints",)


class InviteEndpoints(EndpointMixin):
    def get_invite(
        self,
        invite_code: dt.Snowflake,
        *,
        with_counts: UnsetOr[bool] = Unset,
        with_expiration: UnsetOr[bool] = Unset,
        guild_scheduled_event_id: UnsetOr[dt.Snowflake] = Unset,
    ):
        return self.request(
            Route("GET", "/invites/{invite_code}", invite_code=invite_code),
            query_params={
                "with_counts": with_counts,
                "with_expiration": with_expiration,
                "guild_scheduled_event_id": guild_scheduled_event_id,
            },
        )

    def delete_invite(self, invite_code: dt.Snowflake, reason: t.Optional[str] = None):
        return self.request(
            Route("DELETE", "/invites/{invite_code}", invite_code=invite_code),
            reason=reason,
        )
