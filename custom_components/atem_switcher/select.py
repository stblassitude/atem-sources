"""Select platform for atem-switcher."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

from homeassistant.components.select import SelectEntity, SelectEntityDescription

from .const import LOGGER
from .entity import AtemSwitcherEntity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import AtemSwitcherDataUpdateCoordinator
    from .data import AtemSwitcherConfigEntry

ENTITY_DESCRIPTIONS = (
    SelectEntityDescription(
        key="atem-switcher",
        name="ATEM Sources",
        icon="mdi:gender-transgender",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: AtemSwitcherConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the switch platform."""
    async_add_entities(
        AtemSwitcherSwitch(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
            options=entry.runtime_data.client.get_inputs(),
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )
    await asyncio.sleep(1)


class AtemSwitcherSwitch(AtemSwitcherEntity, SelectEntity):
    """atem-switcher select class."""

    def __init__(
        self,
        coordinator: AtemSwitcherDataUpdateCoordinator,
        entity_description: SelectEntityDescription,
        options: list[str],
    ) -> None:
        """Initialize the switch class."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._options = options
        self._current_option = None

    def _handle_coordinator_update(self) -> None:
        """Process updates from coordinator."""
        LOGGER.info("Coordinator update: %s", self.coordinator.data)
        self._current_option = self.coordinator.data["source"]
        self._options = self.coordinator.data["inputs"]

    def select_option(self, option: str) -> None:
        """Switch to selected option."""
        LOGGER.info("Setting current option: %s", option)
        self.coordinator.config_entry.runtime_data.client.set_source(option)

    @property
    def options(self) -> list[str]:
        """Return the list of options available."""
        LOGGER.debug("Getting options: %s", self.coordinator.data["inputs"])
        return self._options

    @property
    def current_option(self) -> str | None:
        """Currently selected input."""
        self._current_option = (
            self.coordinator.config_entry.runtime_data.client.get_source()
        )
        LOGGER.info("Getting current option: %s", self._current_option)
        return self._current_option
