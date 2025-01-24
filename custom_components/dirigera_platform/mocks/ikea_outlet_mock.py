import logging

from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.entity import DeviceInfo

logger = logging.getLogger("custom_components.dirigera_platform")


class ikea_outlet_mock(SwitchEntity):
    counter = 0

    def __init__(self, hub, hub_outlet):
        self._hub = hub
        self._hub_outlet = hub_outlet
        ikea_outlet_mock.counter = ikea_outlet_mock.counter + 1

        self._manufacturer = "IKEA of Sweden"
        self._unique_id = "O1907151129080101_" + str(ikea_outlet_mock.counter)
        self._model = "mock outlet"
        self._sw_version = "mock sw"
        self._name = "mock"

        self._name = "Mock Outlet {}".format(ikea_outlet_mock.counter)
        self._is_on = False

    @property
    def unique_id(self):
        return self._unique_id

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._is_on

    def turn_on(self, **kwargs):
        self._is_on = True

    def turn_off(self, **kwargs):
        self._is_on = False

# Test block to run the file directly
if __name__ == "__main__":
    mock_hub = None  # Replace with actual hub object if available
    mock_hub_outlet = None  # Replace with actual hub outlet object if available
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    print(f"Outlet Name: {outlet.name}")
    print(f"Outlet Unique ID: {outlet.unique_id}")
    print(f"Is Outlet On? {outlet.is_on}")
    outlet.turn_on()
    print(f"Is Outlet On after turning on? {outlet.is_on}")
    outlet.turn_off()
    print(f"Is Outlet On after turning off? {outlet.is_on}")