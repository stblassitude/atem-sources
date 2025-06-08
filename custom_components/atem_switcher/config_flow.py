"""Adds config flow for AtemSwitcher."""

from __future__ import annotations

import logging

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST
from homeassistant.helpers import selector

from .const import DOMAIN, LOGGER

LOGGER.info("Initializing config flow for ATEM")


class AtemSwitcherFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for AtemSwitcher."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict | None = None,
    ) -> config_entries.ConfigFlowResult:
        """Handle a flow initialized by the user."""
        LOGGER.info("Starting user flow")
        _errors = {}
        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_HOST],
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_HOST,
                        default=(user_input or {}).get(CONF_HOST, vol.UNDEFINED),
                    ): selector.TextSelector(
                        selector.TextSelectorConfig(
                            type=selector.TextSelectorType.TEXT,
                        ),
                    ),
                },
            ),
            errors=_errors,
        )
