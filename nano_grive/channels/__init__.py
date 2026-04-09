"""Chat channels module with plugin architecture."""

from nano_grive.channels.base import BaseChannel
from nano_grive.channels.manager import ChannelManager

__all__ = ["BaseChannel", "ChannelManager"]
