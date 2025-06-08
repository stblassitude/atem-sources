"""Custom types for atem-switcher."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import AtemSwitcherApiClient
    from .coordinator import AtemSwitcherDataUpdateCoordinator


type AtemSwitcherConfigEntry = ConfigEntry[AtemSwitcherData]


@dataclass
class AtemSwitcherData:
    """Data for the AtemSwitcher integration."""

    client: AtemSwitcherApiClient
    coordinator: AtemSwitcherDataUpdateCoordinator
    integration: Integration
