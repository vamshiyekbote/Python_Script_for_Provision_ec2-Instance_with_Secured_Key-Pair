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

# Install OpenJDK 17 JRE Headless
openjdk_install_command = "sudo apt install openjdk-17-jre-headless -y"
run_command(openjdk_install_command)

# Download Jenkins GPG key
jenkins_key_url = "https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key"
jenkins_key_download_command = f"sudo wget -O /usr/share/keyrings/jenkins-keyring.asc {jenkins_key_url}"
run_command(jenkins_key_download_command)

# Add Jenkins repository to package manager sources
jenkins_repo_command = (
    "echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] "
    f"{jenkins_key_url} binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null"
)
run_command(jenkins_repo_command)

# Update package manager repositories
apt_update_command = "sudo apt-get update"
run_command(apt_update_command)

# Install Jenkins
jenkins_install_command = "sudo apt-get install jenkins -y"
run_command(jenkins_install_command)

