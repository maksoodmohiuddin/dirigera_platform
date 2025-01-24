import sys
import os
import pytest

# Add the custom_components directory to the Python path
custom_components_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
print(f"Adding {custom_components_path} to sys.path")
sys.path.append(custom_components_path)

try:
    from custom_components.dirigera_platform.mocks.ikea_outlet_mock import ikea_outlet_mock
    print("Module imported successfully")
except ModuleNotFoundError as e:
    print(f"Error importing module: {e}")
    raise

@pytest.fixture
def mock_hub():
    return None  # Replace with actual hub object if available

@pytest.fixture
def mock_hub_outlet():
    return None  # Replace with actual hub outlet object if available

def test_ikea_outlet_initialization(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    assert outlet is not None

def test_ikea_outlet_turn_on(mock_hub, mock_hub_outlet):
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    outlet.turn_on()
    assert outlet.is_on is True

def test_ikea_outlet_turn_off(mock_hub, mock_hub_outlet):
    print("Running test_ikea_outlet_turn_off")
    outlet = ikea_outlet_mock(mock_hub, mock_hub_outlet)
    outlet.turn_off()
    assert outlet.is_on is False