"""Custom types for atem-switcher."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import AtemSourcesApiClient
    from .coordinator import AtemSourcesDataUpdateCoordinator


type AtemSourcesConfigEntry = ConfigEntry[AtemSourcesData]


@dataclass
class AtemSourcesData:
    """Data for the AtemSources integration."""

    client: AtemSourcesApiClient
    coordinator: AtemSourcesDataUpdateCoordinator
    integration: Integration
