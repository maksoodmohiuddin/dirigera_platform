import sys
import os
import pytest

# Add the custom_components directory to the Python path
custom_components_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(custom_components_path)

from custom_components.dirigera_platform.mocks.ikea_outlet_mock import ikea_outlet_mock

@pytest.fixture
def mock_hub():
    return None  # Replace with actual hub object if available

@pytest.fixture
def mock_hub_outlet():
    return None  # Replace with actual hub outlet object if available

def test_ikea_outlet_initialization(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    assert outlet.name == "Mock Outlet 1"
    assert outlet.unique_id == "O1907151129080101_1"

def test_ikea_outlet_turn_on(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    outlet.turn_on()
    assert outlet.is_on is True

def test_ikea_outlet_turn_off(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    outlet.turn_on()
    outlet.turn_off()
    assert outlet.is_on is False

def test_ikea_outlet_unique_id_generation(mock_hub, mock_hub_outlet):
    outlet1 = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    outlet2 = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    assert outlet1.unique_id != outlet2.unique_id

def test_ikea_outlet_name_generation(mock_hub, mock_hub_outlet):
    outlet1 = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    outlet2 = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    assert outlet1.name != outlet2.name

def test_ikea_outlet_manufacturer_info(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    assert outlet._manufacturer == "IKEA of Sweden"

def test_ikea_outlet_model_info(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    assert outlet._model == "mock outlet"

def test_ikea_outlet_sw_version_info(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    assert outlet._sw_version == "mock sw"

def test_ikea_outlet_initial_state(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    assert outlet.is_on is False

def test_ikea_outlet_state_persistence(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    outlet.turn_on()
    assert outlet.is_on is True
    outlet.turn_off()
    assert outlet.is_on is False

def test_ikea_outlet_state_no_change_without_calls(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    assert outlet.is_on is False

def test_ikea_outlet_multiple_turn_on_calls(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    outlet.turn_on()
    outlet.turn_on()
    assert outlet.is_on is True

def test_ikea_outlet_multiple_turn_off_calls(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    outlet.turn_off()
    outlet.turn_off()
    assert outlet.is_on is False

def test_ikea_outlet_interleaved_turn_on_off_calls(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    outlet.turn_on()
    assert outlet.is_on is True
    outlet.turn_off()
    assert outlet.is_on is False
    outlet.turn_on()
    assert outlet.is_on is True

def test_ikea_outlet_state_after_reinitialization(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    outlet.turn_on()
    assert outlet.is_on is True
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    assert outlet.is_on is False