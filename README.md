# Anker Solix X1 Modbus TCP - Home Assistant Integration

This is a custom HACS-compatible integration for the Anker Solix X1, using **Modbus TCP** provided by the Anker Solix X1 itself. No YAML required. The integration provides sensors to monitor the battery directly from Home Assistant.

## Status & next steps

- implement the use of the scale setting. Currenlty values are available and seem to be correct. Just their scale is wrong (for most int32 and uint32 values)
- I want to separate the sensor into sections for better overview/visibility or separate the sensors in different devices. The X1 consists of 1 ore more batteries, smartmeter, PCS (Power Conversion System, etc.)

## Thanks to ViperRNMC

I built this Home Assistant integration on top of ViperRNMC’s marstek_venus_modbus integration because it allowed me to test quickly and achieve initial results with minimal effort.

Since my integration is intended exclusively for the Anker Solix X1 system and will not work with the Marstek Venus, I decided not to fork ViperRNMC’s integration. Instead, I created my own copy, which I then adapted and rewrote where necessary.
There are still a few references to the Marstek Venus system in some places. I’ll update those once I’ve brought the integration to a level where I can reliably use it with my own Anker Solix X1 setup.


I truly value and deeply appreciate the work ViperRNMC has put into this.
https://github.com/ViperRNMC/marstek_venus_modbus


## Requirements

- ModbusTCP enabled on the Anker Solix X1 (possible in the 'professional' app)
- As far as I know, ModbusTCP only works with LAN cabling. Not via Wifi.
- The IP address
- Home Assistant Core 2025.9 or later
- HACS installed


## Disclaimer:

🚨 **This custom component is an independent project and is not affiliated with Anker. It has been developed to provide Home Assistant users with tools to integrate the devices of Anker Solix power systems into their smart home. Any trademarks or product names mentioned are the property of their respective owners.** 🚨


## Usage terms and conditions:

This integration utilizes an unofficial Python library to communicate with the Anker Power cloud server Api, which is used by the official Anker mobile app. The cloud server Api access or communication may change or break any time without notice and therefore also change or break the integration functionality. Furthermore, the usage for the unofficial Api library may impose risks, such as device damage by improper settings or loss of manufacturer's warranty, whether is caused by improper usage, library failures, Api changes or other reasons.

🚨 **The user bears the sole risk for a possible loss of the manufacturer's warranty or any damage that may have been caused by use of this integration or the underlying Api python library. Users must accept these conditions prior integration usage. A consent automatically includes future integration or Api library updates, which can extend the integration functionality for additional device settings or monitoring capabilities.** 🚨


### 🔧 Features

- Native Modbus TCP polling via `pymodbus`


## 🚀 Installation

1. Add this repository to HACS **Integrations → Custom repositories**
[![Add repository to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=SasMei&repository=AnkerSolixX1ModbusTCP&category=integration)
2. Install the “Anker Solix X1 Modbus TCP” integration
3. Restart Home Assistant
4. Add the integration via **Settings → Devices & Services**
5. Enter the connection details:
   - IP address of your Anker Solix X1

## ⚙️ Configuration

### Polling Intervals

The integration uses intelligent polling with configurable intervals per entity type to balance responsiveness and network load.

**Configurable via Options UI:**
- **High priority** (default: 5 seconds) - Critical sensors like power, voltage, current, SOC
- **Medium priority** (default: 30 seconds) - Temperature sensors, state sensors
- **Low priority** (default: 60 seconds) - Energy totals, efficiency calculations
- **Very low priority** (default: 300 seconds) - Device information, firmware versions


## ✅ Tested Devices for Modbus TCP

The Anker Solix X1 ModbusTCP  integration has been tested with the following hardware:
- Anker Solix X1

