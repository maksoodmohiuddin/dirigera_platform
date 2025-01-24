# IKEA Dirigera Hub Integration

This custom component helps integrate HomeAssistant with the new IKEA Dirigera hub. This integration is a scaffolding on the great work done by Nicolas Hilberg at https://github.com/Leggin/dirigera.

## Supports

- Lights
- Outlets
- Open/Close Sensors
- Motion Sensor
- Environment Sensor
- FYRTUR Blinds
- STYRBAR Remotes
- AirPurifier
- STARKVIND AirPurifier
- VALLHORN Motion Sensors
- Scenes
- BADRING Water Leak sensor
- SOMRIG Controllers - Included Events for Automation

## Pre-requisite

1. Identify the IP of the gateway - Usually looking at the client list in your home router interface will give that.

## Installing

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=sanjoyg&repository=dirigera_platform&category=integration)

- Like all add-on installations, go to the "HACS" option in the left menu bar in Home Assistant.
- Select Integration and add a custom repository and enter this repository.

## Using the Integration

1. Once you get to add integration and get to the configuration screen, the IP of the gateway will be requested.
   **IMPORTANT** Before hitting enter, be near the IKEA Dirigera hub as post entering IP a request to press the action button on the hub.
2. Once you get the screen requesting to press the action button, physically press the button once and then click on submit.
3. If the IP is right and the action button has been pressed, then the integration will be added and all devices registered will be shown. At this time the following device types are supported.

In addition, you'll find the scenes added as individual entities. Go to the "Entities" to find them as they're not part of any device. Use the "Activate" button to trigger a scene.

## Testing Installation with Mock

1. If you enter the IP as "mock" then mock bulbs and outlets will be added.
2. Once you verify that the bulbs and outlets are added, feel free to delete the integration.

Here is how it looks:

1. After you have downloaded the integration from HACS and go to Setting -> Integration -> ADD INTEGRATION to add the dirigera integration, the following screen will come up:

![Config IP Details](https://github.com/sanjoyg/dirigera_platform/blob/main/screenshots/config-ip-details.png)

To test the integration, enter the IP as "mock". The check-box indicates if the bulbs/lights associated with a device-set should be visible as entities or not:

![Config Mock](https://github.com/sanjoyg/dirigera_platform/blob/main/screenshots/config-mock.png)

The integration would prompt to press the action button on the hub:

![Config Press Action](https://github.com/sanjoyg/dirigera_platform/blob/main/screenshots/config-press-action.png)

Since this is mock, we would get a success message:

![Hub Setup Complete Mock](https://github.com/sanjoyg/dirigera_platform/blob/main/screenshots/config-hub-setup-complete-mock.png)

Once this is complete, you would see two bulbs and two outlets appearing:

![Mock Lights](https://github.com/sanjoyg/dirigera_platform/blob/main/screenshots/mock-lights.png)
![Mock Outlets](https://github.com/sanjoyg/dirigera_platform/blob/main/screenshots/mock-outlets.png)

## Raising Issues

Now I don't have access to all sensors, hence what will be useful is when you raise an issue also supply the JSON that the hub returns. To get the JSON do the following:

- Go to Developer -> Service and invoke `dirigera_platform.dump_data` without any parameters.
- Look at the HASS log which would have the JSON.
- If you see any platform errors, include that as well.

[Detailed Instructions](https://github.com/sanjoyg/dirigera_platform/wiki/Calling-dump_data-to-dump-the-JSON)

## Components

### `custom_components/dirigera_platform/ikea_gateway.py`

This file contains the `ikea_gateway` class which is responsible for interacting with the IKEA Dirigera hub. It includes methods for making devices, getting devices, and various properties for different types of devices like scenes, lights, blinds, etc.

### `custom_components/dirigera_platform/base_classes.py`

This file contains base classes for different IKEA devices and sensors. It includes classes like `ikea_base_device`, `ikea_base_device_sensor`, and specific device classes like `ikea_starkvind_air_purifier_device`, `ikea_vindstyrka_temperature`, etc.

### `custom_components/dirigera_platform/mocks`

This directory contains mock classes for different IKEA devices. These mocks are used for testing purposes. Examples include `ikea_vindstyrka_device_mock`, `ikea_open_close_mock`, and `ikea_starkvind_air_purifier_mock_device`.

### `custom_components/dirigera_platform/sensor.py`

This file contains functions to add sensors for different devices. For example, `add_air_purifier_sensors` adds sensors for air purifiers.

### `custom_components/dirigera_platform/config_flow.py`

This file contains functions to handle the configuration flow for the integration. It includes steps to get the token from the IKEA Dirigera hub.

### `custom_components/dirigera_platform/dirigera_lib_patch.py`

This file contains patches and extensions for the Dirigera library. It includes classes like `HubX` and `HackScene` to handle specific functionalities.

### `custom_components/dirigera_platform/fan.py`

This file contains the setup for the fan (air purifier) entities. It includes the `async_setup_entry` function to add air purifier fan sensors to Home Assistant.

### `custom_components/dirigera_platform/icons.py`

This file contains mappings for different icons used in the integration.

### `README.md`

This file provides an overview of the project, installation instructions, usage, and testing information.

### `LICENSE`

This file contains the MIT License for the project.

### `.github/pull_request_template.md`

This file contains a template for pull requests, including a checklist for contributors and reviewers.

### `.gitignore`

This file specifies files and directories to be ignored by Git.

### `hacs.json`

This file contains metadata for the Home Assistant Community Store (HACS) integration.

## Donation

Donation to above will go to [Samriddhi Foundation](https://www.samriddhifoundation.net/), an initiative by my teenage daughter to help the less fortunate.

<a href="https://www.buymeacoffee.com/sanjoyg" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## Setup
```ython3 -m venv venv```
```source venv/bin/activate```  

On Windows use
```venv\Scripts\activate```

```pip install -r custom_components/dirigera_platform/requirements.txt```

```pip install homeassistant```

```hass --open-ui```

http://localhost:8123


## test 
Run `pytest` from dirigera_platform directory
e.g., 
```pytest -p no:warnings -s```

## sample prompt 
```Using the guidelines listed on #file: prompt-library-unit-testing-
python.md
Create unit tests for ikea_outlet_lock using pytest```