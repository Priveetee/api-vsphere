# vSphere Data API & Visualization Tool

A RESTful API built with Python (FastAPI) and PyVmomi to collect, process, and serve data from your VMware vSphere infrastructure. It provides endpoints for accessing structured information about virtual machines, hosts, clusters, datastores, and networks, and includes features to generate data for 3D visualizations and technical documentation (DAT).

## Features

-   **Comprehensive Data Collection**: Connects to vCenter Server to gather detailed information about your vSphere environment.
-   **RESTful API Endpoints**: Access structured JSON data for:
    -   vCenter details
    -   Datacenter, Cluster, and Host configurations (including hardware, network, and storage)
    -   Datastore information
    -   Network summaries (Standard and Distributed Port Groups)
    -   Virtual Machine details (including hardware, disks, NICs, resource allocations, and custom attributes)
    -   Resource Pool configurations
    -   Distributed Virtual Switch (DVS) details
-   **Data Caching**: Collected data is cached in memory for quick API responses.
-   **On-Demand Refresh**: Trigger a manual refresh of the vSphere data.
-   **3D Visualization Support**: Endpoint to generate a scene graph (nodes and edges) for visualizing relationships between infrastructure components (e.g., a VM and its host, datastores, networks).
-   **Technical Documentation (DAT)**: Endpoint to generate a structured JSON "Document d'Architecture Technique" for a specified Virtual Machine.
-   **Containerized**: Easy to deploy using Docker and Docker Compose.

## Technologies

-   Python 3.11+
-   FastAPI (for the REST API)
-   PyVmomi (VMware vSphere API Python Bindings)
-   Uvicorn (ASGI server)
-   Docker & Docker Compose

## Prerequisites

-   **Docker and Docker Compose**: Ensure they are installed on your system.
    -   Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
    -   Docker Compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)
-   **VMware vSphere Environment**: Access to a vCenter Server (tested with vCenter 6.7 and newer, but should work with 6.5+).
-   **vCenter Credentials**: A user account with at least read-only permissions on the vCenter objects you wish to query.

## Setup & Configuration

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/api-vsphere.git # Replace with your actual repo URL
    cd api-vsphere
    ```

2.  **Configure Environment Variables:**
    The application requires vCenter connection details, which are loaded from an `.env` file.
    *   Copy the example environment file:
        ```bash
        cp .env.example .env
        ```
    *   Edit the newly created `.env` file with your vCenter server details:
        ```plaintext
        VCENTER_HOST=your-vcenter.yourdomain.com
        VCENTER_USER=your_user@vsphere.local
        VCENTER_PASSWORD=your_secret_password
        ```
        **Replace the placeholder values with your actual vCenter FQDN/IP, username, and password.**

    **Important Note on `VCENTER_HOST` and Docker DNS Resolution:**
    The Docker container running this application must be able to resolve the hostname specified for `VCENTER_HOST`.
    *   **Publicly Resolvable FQDN:** If your `VCENTER_HOST` is a Fully Qualified Domain Name (FQDN) resolvable via public DNS (e.g., `vcenter.mycompany.com`), Docker should resolve it without issues.
    *   **Private/Local Hostname:** If `VCENTER_HOST` is an internal hostname (e.g., `vcsa01.internal.lab`) only resolvable by your local DNS servers:
        1.  **Try Default First:** Docker often inherits DNS settings from the host. It might work.
        2.  **Use IP Address:** The simplest solution is often to use the direct IP address of your vCenter server for `VCENTER_HOST` in the `.env` file.
        3.  **Configure Custom DNS for the Container (Advanced):** If you must use a local hostname and Docker's default DNS isn't working, you can configure custom DNS servers for the container. Edit the `docker-compose.yml` file and add/uncomment a `dns` section under the `api-vsphere` service:
            ```yaml
            services:
              api-vsphere:
                # ... other settings ...
                dns:
                  - <ip_of_your_local_dns_server_1>  # Replace with your DNS server's IP
                  - <ip_of_your_local_dns_server_2>  # Optional secondary DNS
                  - 8.8.8.8                          # A public DNS as a fallback (optional)
            ```
            Replace `<ip_of_your_local_dns_server_...>` with the actual IP addresses.

    *   **Firewall:** Ensure that your Docker host (and thus the container) can reach the `VCENTER_HOST` on port 443 (HTTPS).

3.  **Build and Run with Docker Compose:**
    From the project's root directory (`api-vsphere`):
    ```bash
    docker compose up -d --build
    ```
    This command will build the Docker image (if it doesn't exist or if files have changed) and start the application in detached mode.

4.  **Accessing the API:**
    Once the container is running, the API will be available at `http://localhost:8000`.
    *   Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
    *   Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## API Endpoints

The API provides several endpoints to access vSphere data. Visit `http://localhost:8000/docs` for a full interactive list. Key endpoints include:

*   `GET /api/v1/status`: Get the current status of the data collection process (last run time, success/failure).
*   `POST /api/v1/vsphere/refresh`: Trigger a new data collection from vSphere. (Status code 202 Accepted)
*   `POST /api/v1/visualization/scene-graph`: Generate a scene graph (nodes and edges) for 3D visualization.
    *   **Request Body Example:**
        ```json
        {
          "start_object_identifier": "Name-Or-InstanceUUID-Of-VM",
          "start_object_type": "VM",
          "vm_inclusions": {
            "include_host": true,
            "include_cluster_of_host": true,
            "include_datastores": true,
            "include_networks": true
          },
          "host_depth2_inclusions": {
            "include_vms_on_host": true
          },
          "depth": 1
        }
        ```
*   `POST /api/v1/dat/generate/vm`: Generate a structured JSON Document d'Architecture Technique (DAT) for a specified VM.
    *   **Request Body Example:**
        ```json
        {
          "vm_identifier": "Name-Or-InstanceUUID-Of-VM"
        }
        ```
*   *(You can add more specific GET endpoints here later if you implement them, e.g., `/api/v1/vms`, `/api/v1/hosts`)*

## Stopping the Application

To stop the application:
```bash
docker compose down
```
To stop and remove volumes (if any were explicitly defined and you want to clear them):
```bash
docker compose down --volumes
```

## Development

For local development without Docker:

1.  **Create a Python Virtual Environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Linux/macOS
    # .venv\Scripts\activate   # On Windows
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Environment Variables:**
    Ensure your `.env` file is created and configured as described in the "Setup & Configuration" section. The script will load it.

4.  **Run the API Server:**
    ```bash
    uvicorn api_server:app --reload --host 0.0.0.0 --port 8000
    ```
    The `--reload` flag enables auto-reloading when code changes.

## Troubleshooting

*   **Connection Errors to vCenter:**
    *   Verify `VCENTER_HOST`, `VCENTER_USER`, and `VCENTER_PASSWORD` in your `.env` file are correct.
    *   Ensure the `VCENTER_HOST` is resolvable from where you're running the application (or from within the Docker container). See the note on DNS resolution above.
    *   Check firewall rules: the application needs to reach vCenter on port 443 (HTTPS).
    *   Test basic connectivity from the Docker host: `curl -kv https://<VCENTER_HOST>`
*   **`socket.gaierror: [Errno -2] Name or service not known` (inside Docker):** This means the container cannot resolve the `VCENTER_HOST`. Refer to the "Important Note on `VCENTER_HOST` and Docker DNS Resolution" section above.
*   **API returning 503 or "Data cache not initialized":** This usually means the initial data collection from vSphere failed or hasn't completed. Check the container logs for errors from `vsphere_collector.py`:
    ```bash
    docker logs api-vsphere-api-vsphere-1 # Or the actual container name/ID
    ```
    You can trigger a new collection via the `POST /api/v1/vsphere/refresh` endpoint.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.
*(Add more specific contribution guidelines if you wish)*

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
