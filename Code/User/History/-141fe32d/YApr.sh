#!/bin/bash

# Function to install a package using Pacman
install_package() {
    package="$1"
    
    # Check if Pacman is available
    if ! command -v pacman &> /dev/null; then
        echo "Error: Pacman is not available."
        exit 1
    fi

    # Update package database and install the package
    sudo pacman -Sy --noconfirm
    sudo pacman -S --noconfirm "$package"
}

# Example usage: install a package
install_package "neofetch"
