#!/bin/bash

# Directory containing wallpapers
WALLPAPER_DIR="/home/naturalcapsule/.config/wallpapers"

# File to keep track of the current wallpaper index
INDEX_FILE="$HOME/.config/current_wallpaper_index.txt"

# Read the current index
if [ ! -f "$INDEX_FILE" ]; then
    echo 0 > "$INDEX_FILE"
fi

CURRENT_INDEX=$(cat "$INDEX_FILE")

# Get the list of wallpapers
WALLPAPER_LIST=($(find "$WALLPAPER_DIR" -type f | sort))

# Get the total number of wallpapers
TOTAL_WALLPAPERS=${#WALLPAPER_LIST[@]}

# Select the next wallpaper
NEXT_INDEX=$(( (CURRENT_INDEX + 1) % TOTAL_WALLPAPERS ))
WALLPAPER_PATH=${WALLPAPER_LIST[$NEXT_INDEX]}

# Update the index file
echo $NEXT_INDEX > "$INDEX_FILE"

# Change the wallpaper
swww img "$WALLPAPER_PATH"

# Apply pywal colors
wal -i "$WALLPAPER_PATH"

# Reload Kitty configuration
kitty @ set-colors --all --reload

# Stop any existing Waybar instances
pkill waybar

# Start a new Waybar instance
waybar &
