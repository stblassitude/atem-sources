# ATEM video switcher integration for Home Assistant

The line of Black Magic Design ATEM video mixers can be used as an HDMI video switcher with network control. This integration allows you to easily switch between the four inputs on the ATEM mini line.

The list of available inputs is fixed at HDMI 1 to 4, plus the color bars and the black screen.

## Installation

This integrations uses [Home Assistant Community Store](https://hacs.xyz) to help you install it in your Home Assistant. This integration has not been added to the HACS repository, so you will need to [add a custom repository](https://hacs.xyz/docs/faq/custom_repositories/), using this repo's URL https://github.com/stblassitude/atem-switcher.

## References

This integration makes use of [PyATEMMax](https://clvlabs.github.io/PyATEMMax/).

The code for this integration is based on the [integration blueprint](https://github.com/ludeeus/integration_blueprint/tree/main).
