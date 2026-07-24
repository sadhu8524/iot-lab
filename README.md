#  IoT Coffee Machine Fleet Monitoring Platform

A Python-based IoT simulator and monitoring platform that simulates a fleet of **100 connected coffee machines** and demonstrates an end-to-end telemetry pipeline using MQTT, Telegraf, InfluxDB, and Grafana.

The project represents how real-world edge devices such as **Raspberry Pi, ESP32, or industrial IoT gateways** can publish telemetry data and be monitored through a centralized observability platform.

---

##  Architecture

```
+---------------------------+
|  Coffee Machine Simulator |
|        Python             |
|                           |
|  100 Simulated Devices    |
+-------------+-------------+
              |
              | MQTT Telemetry
              |
              v
+---------------------------+
| Eclipse Mosquitto MQTT    |
| Broker                    |
+-------------+-------------+
              |
              |
              v
+---------------------------+
| Telegraf MQTT Collector   |
| Telemetry Ingestion       |
+-------------+-------------+
              |
              |
              v
+---------------------------+
| InfluxDB 2.x              |
| Time-Series Database      |
+-------------+-------------+
              |
              |
              v
+---------------------------+
| Grafana Dashboards        |
| Fleet Monitoring          |
+---------------------------+
```

---

#  Features

## Device Simulation

The Python simulator creates **100 coffee machines** and continuously publishes telemetry data.

Each simulated device generates:

- Device ID
- Temperature
- Humidity
- Water level
- Coffee level
- WiFi signal strength
- Heartbeat status

Example telemetry message:

```json
{
  "device": "coffee-machine-042",
  "temperature": 24.6,
  "humidity": 55,
  "waterLevel": 78,
  "coffeeLevel": 65,
  "wifi": -52,
  "heartbeat": 1
}
```

---

#  MQTT Communication

The devices communicate using MQTT through Eclipse Mosquitto.

MQTT Topic:

```
coffee/telemetry
```

Example:

```
coffee/telemetry

{
 "device":"coffee-machine-001",
 "temperature":25.4,
 "humidity":60,
 "heartbeat":1
}
```

MQTT provides a lightweight communication protocol suitable for IoT devices with limited resources and unreliable network conditions.

---

#  Telemetry Collection

Telegraf consumes MQTT messages and transforms the incoming device telemetry into time-series metrics.

Responsibilities:

- MQTT subscription
- JSON parsing
- Metric extraction
- Forwarding data to InfluxDB

---

#  Data Storage

InfluxDB 2.x stores the telemetry data as time-series measurements.

Stored metrics include:

```
temperature
humidity
waterLevel
coffeeLevel
wifi
heartbeat
```

---

#  Grafana Dashboards

## Fleet Health Dashboard

Monitors device operational health:

- Temperature trends
- Humidity levels
- WiFi connectivity
- Device heartbeat
- Sensor telemetry

## Fleet Inventory Dashboard

Provides fleet visibility:

- Number of coffee machines
- Device availability
- Inventory levels
- Sensor status

---

#  Running Locally

## Requirements

- Docker Desktop
- Python 3.x
- MQTT client libraries

Install Python dependencies:

```bash
pip install paho-mqtt
```

---

## Start Infrastructure

Start the IoT monitoring stack:

```bash
docker compose up -d
```

Services:

| Service | Port |
|---|---|
| MQTT Broker | 1883 |
| InfluxDB | 8086 |
| Grafana | 3000 |

---

## Start Device Simulator

Run:

```bash
python simulator.py
```

You should see telemetry from multiple coffee machines:

```
{
'device': 'coffee-machine-023',
'temperature': 26.4,
'humidity': 55,
'waterLevel': 80,
'coffeeLevel': 72,
'wifi': -50,
'heartbeat': 1
}
```

---

#  Technology Stack

| Component | Technology |
|-|-|
| Device Simulation | Python |
| Messaging Protocol | MQTT |
| MQTT Broker | Eclipse Mosquitto |
| Telemetry Collector | Telegraf |
| Time-Series Database | InfluxDB 2.x |
| Visualization | Grafana |
| Container Platform | Docker |

---

#  Engineering Concepts Demonstrated

- IoT device telemetry pipelines
- MQTT communication patterns
- Edge device monitoring
- Fleet management concepts
- Time-series data processing
- Observability architecture
- Sensor health monitoring
- Device heartbeat tracking

---


