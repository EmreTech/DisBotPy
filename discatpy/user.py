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

from typing import Any, Dict, Optional

from .types.snowflake import *
from .types.user import *
from .abs import APIType
from .asset import Asset
from .mixins import SnowflakeMixin

__all__ = (
    "User",
)

class User(APIType, SnowflakeMixin):
    """
    Represents a User type. This shouldn't be initalized manually, the rest of the API
    should take care of that for you.

    Attributes
    ----------
    id: :type:`Snowflake`
        The id of this user
    name: :type:`str`
        The name of this user
    discriminator: :type:`str`
        The 4 digit tag for this user, also called a discriminator
    avatar: :type:`UserAvatar`
        The avatar for this user
    bot: :type:`bool`
        If this user is a bot or not
    tfa_enabled: :type:`bool`
        If this user has two-factor authentication or not
    banner: :type:`UserBanner`
        The banner for this user
    flags: :type:`int`
        The flags for this user
    premium_type: :type:`int`
        If the user has Nitro, Nitro Classic, or none
    public_flags: :type:`int`
        The public flags for this user
    """
    def __init__(
        self, 
        d: Dict[str, Any],
        client,
        id: Snowflake,
        name: str,
        discrim: str,
        avatar_hash: Optional[str],
        bot: bool,
        tfa_enabled: bool,
        banner_hash: Optional[str],
        accent_color: Optional[int],
        flags: int,
        premium_type: int,
        public_flags: int
    ) -> None:
        super().__init__(d, client)

        self.raw_id = id
        self.name = name
        self.discriminator = discrim
        self.avatar = Asset.from_user_avatar(client, self.raw_id, avatar_hash) if avatar_hash else Asset.from_default_user_avatar(client, int(self.discriminator))
        self.bot = bot
        self.tfa_enabled = tfa_enabled
        self.banner = Asset.from_user_banner(client, self.raw_id, banner_hash) if banner_hash else None
        self.accent_color = accent_color
        # TODO: Locales
        self.flags = flags
        self.premium_type = premium_type
        self.public_flags = public_flags

    @classmethod
    def from_dict(cls, client, d: Dict[str, Any]):
        id: Snowflake = d.get("id")
        name: str = d.get("username")
        discriminator: str = d.get("discriminator")
        avatar_hash: Optional[str] = d.get("avatar")
        bot: bool = d.get("bot", False)
        tfa_enabled: bool = d.get("mfa_enabled", False)
        accent_color: Optional[int] = int(d.get("accent_color")) if d.get("accent_color") is not None else None
        banner_hash: Optional[str] = d.get("banner")
        # TODO: Locales
        flags: int = d.get("flags", UserFlags.NONE)
        premium_type: int = d.get("premium_type", PremiumTypes.NONE)
        public_flags: int = d.get("public_flags", UserFlags.NONE)

        return cls(
            d, 
            client, 
            id, 
            name, 
            discriminator, 
            avatar_hash, 
            bot, 
            tfa_enabled, 
            banner_hash, 
            accent_color,
            flags, 
            premium_type, 
            public_flags
        )

    @property
    def mention(self) -> str:
        """
        Returns a string that can mention this user.
        """
        return f"<@{self.id}>"