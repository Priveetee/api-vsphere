# vSphere Data API & Visualization Tool

A RESTful API built with Python (FastAPI) and PyVmomi to collect, process, and serve data from your VMware vSphere infrastructure. It provides endpoints for accessing structured information about virtual machines, hosts, clusters, datastores, and networks, and includes features to generate data for 3D visualizations and technical documentation (DAT).

## Features

-   **Comprehensive Data Collection**: Connects to vCenter Server to gather detailed information about your vSphere environment.
-   **RESTful API Endpoints**: Access structured JSON data for various vSphere components.
-   **Data Caching**: Collected data is cached in memory for quick API responses.
-   **On-Demand Refresh**: Trigger a manual refresh of the vSphere data.
-   **3D Visualization Support**: Endpoint to generate a scene graph for visualizing infrastructure relationships.
-   **Technical Documentation (DAT)**: Endpoint to generate a structured JSON "Document d'Architecture Technique" for VMs.
-   **Containerized**: Easy to deploy using Docker and Docker Compose by building from source.

## Technologies

-   Python 3.11+
-   FastAPI
-   PyVmomi
-   Uvicorn
-   Docker & Docker Compose

## Prerequisites

-   **Docker and Docker Compose**: Ensure they are installed on your system.
    -   Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
    -   Docker Compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)
-   **Git**: For cloning the repository.
-   **VMware vSphere Environment**: Access to a vCenter Server (tested with vCenter 6.7+, should work with 6.5+).
-   **vCenter Credentials**: A user account with at least read-only permissions.

## Setup & Running (Building from Source)

This is the primary way to run the application if you have cloned this repository.

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Priveetee/api-vsphere.git
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

3.  **Build and Run with Docker Compose:**
    From the project's root directory (`api-vsphere`), run:
    ```bash
    docker compose up -d --build
    ```
    This command will build the Docker image from the `Dockerfile` in this repository using the provided `docker-compose.yml` and then start the application in detached mode.

4.  **Accessing the API:**
    Once the container is running, the API will be available at `http://localhost:8000`.
    *   Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
    *   Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

### Important Note on `VCENTER_HOST` and Docker DNS Resolution

The Docker container (built locally) needs to be able to resolve the hostname you provide for `VCENTER_HOST` in your `.env` file.
*   **Publicly Resolvable FQDN:** If your `VCENTER_HOST` is a Fully Qualified Domain Name (FQDN) resolvable via public DNS, Docker should resolve it without issues.
*   **Private/Local Hostname:** If `VCENTER_HOST` is an internal hostname only resolvable by your local DNS servers:
    1.  **Try Default First:** Docker often inherits DNS settings from the host. It might work.
    2.  **Use IP Address:** The simplest solution is often to use the direct IP address of your vCenter server for `VCENTER_HOST` in the `.env` file.
    3.  **Configure Custom DNS for the Container (Advanced):** If you must use a local hostname and Docker's default DNS isn't working, edit the `docker-compose.yml` file (provided in this repository) and add/uncomment the `dns` section under the `api-vsphere` service:
        ```yaml
        services:
          api-vsphere:
            build: 
              context: .
              dockerfile: Dockerfile
            dns:
              - <ip_of_your_local_dns_server_1> 
              - <ip_of_your_local_dns_server_2> 
              - 8.8.8.8                          
        ```
        Replace `<ip_of_your_local_dns_server_...>` with the actual IP addresses.
*   **Firewall:** Ensure that your Docker host (and thus the container) can reach the `VCENTER_HOST` on port 443 (HTTPS).

## Using Pre-built Docker Image from Docker Hub (Alternative)

For users who prefer not to build from source, a pre-built image is available on Docker Hub.

1.  **Ensure Docker and Docker Compose are installed.**
2.  **Create an Environment File (`.env`):**
    Follow step 2 from the "Setup & Running (Building from Source)" section to create and configure your `.env` file with vCenter credentials. Place this `.env` file in a directory where you will also create the `docker-compose.yml` below.
3.  **Create a `docker-compose.yml` file:**
    In the same directory as your `.env` file, create a *new* `docker-compose.yml` with the following content:
    ```yaml
    services:
      api-vsphere:
        image: lynear/api-explore:latest
        ports:
          - "8000:8000"
        env_file:
          - .env
        restart: unless-stopped
        # --- Optional DNS Configuration ---
        # (See "Important Note on VCENTER_HOST" above if you have connection issues)
        # dns:
        #   - <ip_of_your_local_dns_server_1>
        #   - 8.8.8.8
    ```
4.  **Run the Application:**
    From the directory containing your `.env` and this new `docker-compose.yml`:
    ```bash
    docker compose up -d
    ```
    The API will be available at `http://localhost:8000`.

## API Endpoints

Visit `http://localhost:8000/docs` for a full interactive list. Key endpoints include:

*   `GET /api/v1/status`: Get the current status of the data collection process.
*   `POST /api/v1/vsphere/refresh`: Trigger a new data collection from vSphere.
*   `POST /api/v1/visualization/scene-graph`: Generate a scene graph for 3D visualization.
*   `POST /api/v1/dat/generate/vm`: Generate a structured JSON DAT for a specified VM.

## Stopping the Application

```bash
docker compose down
```
To stop and remove volumes (if any were explicitly defined and you want to clear them):
```bash
docker compose down --volumes
```

## Development (Local Python Environment without Docker)

1.  Clone the repository.
2.  Create and activate a Python virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Linux/macOS
    # .venv\Scripts\activate   # On Windows (Why are u on this shitty OS are u out of ure freaking mind ?!)
    ```
3.  Install dependencies: `pip install -r requirements.txt`
4.  Ensure your `.env` file is created and configured.
5.  Run: `uvicorn api_server:app --reload --host 0.0.0.0 --port 8000`

## Troubleshooting

*   **Connection Errors to vCenter:** Verify credentials in `.env`, hostname resolvability (see DNS note), and firewall (port 443).
*   **`socket.gaierror: [Errno -2] Name or service not known` (inside Docker):** Refer to the "Important Note on `VCENTER_HOST`" section.
*   **API returning 503 or "Data cache not initialized":** Check container logs (`docker logs <container_name_or_id>`) for errors from `vsphere_collector.py`. Trigger a refresh via `POST /api/v1/vsphere/refresh`.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
