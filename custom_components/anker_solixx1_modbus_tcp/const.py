# Integration domain name
DOMAIN = "solixx1_modbus"

# Manufacturer and model information for the SolixX1 Venus battery
MANUFACTURER = "Anker"
MODEL = "Solix X1"

# Default network configuration for Modbus connection
DEFAULT_PORT = 502
DEFAULT_MESSAGE_WAIT_MS = 80  # Default wait time for Modbus messages in milliseconds
DEFAULT_UNIT_ID = 1  # Default Modbus Unit ID (unit ID)

# General scan intervals (in seconds)
DEFAULT_SCAN_INTERVALS = {
    "high": 10,       # fast-changing sensors, e.g., power, alarms
    "medium": 30,     # moderately changing sensors, e.g., voltage, current
    "low": 60,        # slow-changing sensors, e.g., cumulative energy counters
    "very_low": 180   # rarely changing info, e.g., device info, firmware versions
}

# Supported device versions
SUPPORTED_VERSIONS = [    
    "X1"]

# Note: register loading logic (get_registers_for_version) was moved to
# `register_loader.py` to keep `const.py` focused on constants only.