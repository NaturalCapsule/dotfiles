import json
import os

# Paths
pywal_colors_path = os.path.expanduser("~/.cache/wal/colors.json")
cava_config_path = os.path.expanduser("~/.config/cava/config")

# Load pywal colors
with open(pywal_colors_path, 'r') as f:
    colors = json.load(f)

# Extract colors
foreground_color = colors['colors']['color7']  # Use pywal's color7 for foreground
background_color = colors['special']['background']  # Use pywal's background color

# Ensure colors are in the correct format (with # prefix and within single quotes)
foreground_color = f"'{foreground_color}'"
background_color = f"'{background_color}'"

# Update Cava config
with open(cava_config_path, 'r') as f:
    config_lines = f.readlines()

# Modify the configuration lines
new_config_lines = []
for line in config_lines:
    if line.strip().startswith("foreground ="):
        new_config_lines.append(f'foreground = {foreground_color}\n')
    elif line.strip().startswith("background ="):
        new_config_lines.append(f'background = {background_color}\n')
    else:
        new_config_lines.append(line)

# Write updated config back to file
with open(cava_config_path, 'w') as f:
    f.writelines(new_config_lines)

print("Cava configuration updated with pywal colors.")
