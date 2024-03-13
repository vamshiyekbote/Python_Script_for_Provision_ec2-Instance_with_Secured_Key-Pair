import subprocess
import importlib

def install_module(module_name):
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(f"Installing {module_name} module...")
        subprocess.run([sys.executable, "-m", "pip", "install", module_name], check=True)

# Check and install 'requests' module if needed
install_module('requests')

import requests

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode(), error.decode()

# Update package manager repositories
update_repositories_command = "sudo apt-get update"
run_command(update_repositories_command)

# Install necessary dependencies
install_dependencies_command = "sudo apt-get install -y ca-certificates curl"
run_command(install_dependencies_command)

# Create directory for Docker GPG key
create_key_directory_command = "sudo install -m 0755 -d /etc/apt/keyrings"
run_command(create_key_directory_command)

# Download Docker's GPG key
docker_key_url = "https://download.docker.com/linux/ubuntu/gpg"
docker_key_download_command = f"sudo curl -fsSL {docker_key_url} -o /etc/apt/keyrings/docker.asc"
run_command(docker_key_download_command)

# Ensure proper permissions for the key
chmod_key_permissions_command = "sudo chmod a+r /etc/apt/keyrings/docker.asc"
run_command(chmod_key_permissions_command)

# Add Docker repository to Apt sources
docker_repo_command = (
    "echo \"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] "
    f"https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo \"$VERSION_CODENAME\") stable\" | "
    "sudo tee /etc/apt/sources.list.d/docker.list > /dev/null"
)
run_command(docker_repo_command)

# Update package manager repositories
update_repositories_command = "sudo apt-get update"
run_command(update_repositories_command)

# Install Docker
install_docker_command = (
    "sudo apt-get install -y docker-ce docker-ce-cli containerd.io "
    "docker-buildx-plugin docker-compose"
)
run_command(install_docker_command)

