"""AtemSourcesEntity class."""

from __future__ import annotations

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import ATTRIBUTION
from .coordinator import AtemSourcesDataUpdateCoordinator


class AtemSourcesEntity(CoordinatorEntity[AtemSourcesDataUpdateCoordinator]):
    """AtemSourcesEntity class."""

    _attr_attribution = ATTRIBUTION

    def __init__(self, coordinator: AtemSourcesDataUpdateCoordinator) -> None:
        """Initialize."""
        super().__init__(coordinator)
        self._attr_unique_id = coordinator.config_entry.entry_id
        self._attr_device_info = DeviceInfo(
            identifiers={
                (
                    coordinator.config_entry.domain,
                    coordinator.config_entry.entry_id,
                ),
            },
        )
