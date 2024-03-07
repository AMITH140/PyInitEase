# install_packages.py
import os
import subprocess

def install_packages():
    try:
        current_directory = os.path.dirname(os.path.realpath(__file__))
        requirements_path = os.path.join(current_directory, 'requirements.txt')
        with open(requirements_path, 'r') as file:
            packages = [line.strip() for line in file if line.strip()]
        if packages:
            subprocess.run(['pip', 'install', *packages])
            print("Packages installed successfully.")
        else:
            print("No packages to install.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    install_packages()
