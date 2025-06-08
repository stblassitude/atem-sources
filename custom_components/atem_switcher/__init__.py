"""Custom integration to integrate atem_switcher with Home Assistant."""

from __future__ import annotations

from datetime import timedelta
from typing import TYPE_CHECKING

from homeassistant.const import CONF_HOST, Platform
from homeassistant.loader import async_get_loaded_integration

from .api import AtemSwitcherApiClient
from .const import DOMAIN, LOGGER
from .coordinator import AtemSwitcherDataUpdateCoordinator
from .data import AtemSwitcherData

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant

    from .data import AtemSwitcherConfigEntry

PLATFORMS: list[Platform] = [
    Platform.SELECT,
]

LOGGER.info("__init__.py for ATEM")


# https://developers.home-assistant.io/docs/config_entries_index/#setting-up-an-entry
async def async_setup_entry(
    hass: HomeAssistant,
    entry: AtemSwitcherConfigEntry,
) -> bool:
    """Set up this integration using UI."""
    LOGGER.info("Setting up ATEM Switcher")
    coordinator = AtemSwitcherDataUpdateCoordinator(
        hass=hass,
        logger=LOGGER,
        name=DOMAIN,
        update_interval=timedelta(seconds=1),
        always_update=False,
    )
    entry.runtime_data = AtemSwitcherData(
        client=AtemSwitcherApiClient(
            hostname=entry.data[CONF_HOST],
        ),
        integration=async_get_loaded_integration(hass, entry.domain),
        coordinator=coordinator,
    )
    await entry.runtime_data.client.wait_for_connection()

    # https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
    await coordinator.async_config_entry_first_refresh()

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: AtemSwitcherConfigEntry,
) -> bool:
    """Handle removal of an entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


async def async_reload_entry(
    hass: HomeAssistant,
    entry: AtemSwitcherConfigEntry,
) -> None:
    """Reload config entry."""
    await hass.config_entries.async_reload(entry.entry_id)
