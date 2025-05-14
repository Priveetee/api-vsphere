# vSphere API Visualization Tool

A RESTful API that collects, processes, and visualizes VMware vSphere infrastructure data, providing insights into virtual machines, hosts, datastores, networks, and their relationships.

## Features

- **Real-time Data Collection**: Connect to vSphere environments and collect comprehensive infrastructure data
- **API Endpoints**: Access structured information about virtual machines, hosts, clusters, and datastores
- **3D Visualization Support**: Generate scene graphs for visualizing relationships between infrastructure components
- **Technical Documentation**: Generate structured documentation for virtual machines

## Technologies

- Python 3.11
- FastAPI
- PyVmomi (vSphere Python SDK)
- Docker & Docker Compose

## Prerequisites

- Docker and Docker Compose (for containerized deployment)
- VMware vSphere environment (vCenter Server 6.5+)
- Environment variables for vCenter authentication

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd api-vsphere
   ```

2. Create a `.env` file with your vCenter credentials:
   ```
   VCENTER_HOST=your-vcenter-server.domain
   VCENTER_USER=your-account@vsphere.local
   VCENTER_PASSWORD=your-password
   ```

3. Build and run using Docker Compose:
   ```
   docker compose up -d
   ```

   The API will be available at http://localhost:8000

## API Endpoints

- `GET /api/v1/status`: Get the current data collection status
- `POST /api/v1/vsphere/refresh`: Trigger a new data collection
- `POST /api/v1/visualization/scene-graph`: Generate visualization data for infrastructure components
- `POST /api/v1/dat/generate/vm`: Generate technical documentation for a virtual machine

## Docker Commands

- Build and start the services:
  ```
  docker compose up -d
  ```

## Development

For local development without Docker:

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the API server:
   ```
   uvicorn api_server:app --reload --host 0.0.0.0 --port 8000
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
