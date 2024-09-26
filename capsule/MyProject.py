import subprocess
import psutil
import subprocess
import customtkinter as ctk
import sys
from PIL import Image, ImageTk
import pynvml

pynvml.nvmlInit()
handle = pynvml.nvmlDeviceGetHandleByIndex(0)

def get_nvidia_gpu_temperature():
    try:
        result = subprocess.run(['nvidia-smi', '--query-gpu=temperature.gpu', '--format=csv,noheader,nounits'],
                                stdout=subprocess.PIPE, text=True)
        temperature = result.stdout.strip()
        return f"{temperature}"
    except FileNotFoundError:
        return "nvidia-smi not found. Make sure NVIDIA drivers are installed."

def get_nvidia_gpu_usage():
    try:
        result = subprocess.run(['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv,noheader,nounits'],
                                stdout=subprocess.PIPE, text=True)
        temperature = result.stdout.strip()
        return f"{temperature}"
    except FileNotFoundError:
        return "nvidia-smi not found. Make sure NVIDIA drivers are installed."

def switch_to_system():
    subprocess.Popen(['python3', '/home/naturalcapsule/.config/capsule/app.py'])
    sys.exit()

def get_ram_gb():
    memory_info = psutil.virtual_memory()
    total_ram_gb = memory_info.total / (1024 ** 3)
    return f'{total_ram_gb:.2f}'

def get_used_ram():
    memory_info = psutil.virtual_memory()
    used_ram_gb = memory_info.used / (1024 ** 3)
    return f'{used_ram_gb:.2f}'

def get_tot_vram():
    vram_total = pynvml.nvmlDeviceGetMemoryInfo(handle).total
    vram_total_gb = vram_total / (1024 ** 3)
    return vram_total_gb

def get_used_vram():
    vram_used = pynvml.nvmlDeviceGetMemoryInfo(handle).used
    vram_used_gb = vram_used / (1024 ** 3)
    return f'{vram_used_gb:.2f}'

def get_cpu_freq():
    cpu_freq = psutil.cpu_freq()

    if cpu_freq:
        return f"(C)CPU Frquency: {cpu_freq.current:.1f}MHz"
    else:
        return "Could not retrieve CPU frequency information."

def get_cpu_max_freq():
    cpu_freq = psutil.cpu_freq()

    if cpu_freq:
        return f"MinCPU Frequency: {int(cpu_freq.min)}MHz"
    else:
        return "Could not retrieve Max CPU frequency information."

def get_cpu_min_freq():
    cpu_freq = psutil.cpu_freq()

    if cpu_freq:
        return f"MaxCPU Frequency: {int(cpu_freq.max)}MHz"
    else:
        return "Could not retrieve Max CPU frequency information."

app = ctk.CTk()
app.geometry('1000x600')
app.title('Linux')
app.wm_iconname('rocket.ico')
app.overrideredirect(True)

custom_font = ("Arial", 24)

app.configure(fg_color = 'black', bg_color = '#E6E6FA')

def start_move(event):
    app.x = event.x
    app.y = event.y

def stop_move(event):
    app.x = None
    app.y = None

def on_motion(event):
    x = event.x_root - app.x
    y = event.y_root - app.y
    app.geometry(f"+{x}+{y}")

app.bind('<Button-1>', start_move)
app.bind('<ButtonRelease-1>', stop_move)
app.bind('<B1-Motion>', on_motion)

app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)

def update_cpu_label():
    cpu_usage = psutil.cpu_percent(0)
    cpu_label_info.configure(text=f"CPU usage: {cpu_usage}%")
    app.after(1000, update_cpu_label)

def cpu_temp():
    cpu = psutil.sensors_temperatures()['k10temp'][0][1]
    cpu_label_info1.configure(text=f"CPU Temp: {cpu}°C")
    app.after(1000, cpu_temp)

def cpu_freq():
    cpu_freqs = get_cpu_freq()
    cpu_label_info2.configure(text = cpu_freqs)
    app.after(1000, cpu_freq)

def max_cpu_freq():
    max_cpu = get_cpu_max_freq()
    cpu_label_info3.configure(text = max_cpu)
    app.after(1000, max_cpu_freq)

def min_cpu_freq():
    min_cpu = get_cpu_min_freq()
    cpu_label_info4.configure(text = min_cpu)
    app.after(1000, min_cpu_freq)

def ram_usage():
    ram_usg = psutil.virtual_memory()[2]
    ram_label_info.configure(text = f"RAM Usage: {ram_usg}%")
    app.after(1000, ram_usage)

def gpu_usage():
    gpu_usg = get_nvidia_gpu_usage()
    gpu_label_info.configure(text = f"GPU Usage: {gpu_usg}%")
    app.after(1000, gpu_usage)

def gpu_temp():
    gpu_tmp = get_nvidia_gpu_temperature()
    gpu_label_info1.configure(text = f"GPU Temp: {gpu_tmp}°C")
    app.after(1000, gpu_temp)

def tot_vram():
    vram_tot = get_tot_vram()
    gpu_label_info2.configure(text = f'Total VRAM: {vram_tot}GB')
    app.after(1000, tot_vram)


def ram_info():
    ram_inf = get_ram_gb()
    ram_label_info1.configure(text = f"Total RAM: {ram_inf}GB")
    app.after(1000, ram_info)

def ram_info_used():
    ram_inf = get_used_ram()
    ram_label_info2.configure(text = f'Used RAM: {ram_inf}GB')
    app.after(1000, ram_info_used)
    
def used_vram():
    vram_used = get_used_vram()
    gpu_label_info3.configure(text = f'Used VRAM: {vram_used}GB')
    app.after(1000, used_vram)   

def button_callback():
    sys.exit()

cpu_image = Image.open("/home/naturalcapsule/.config/capsule/cpu.png").convert("RGBA")
background_image_cpu = ImageTk.PhotoImage(cpu_image.resize((200, 200)))

gpu_image = Image.open("/home/naturalcapsule/.config/capsule/graphics-card.png").convert("RGBA")
background_image_gpu = ImageTk.PhotoImage(gpu_image.resize((200, 200)))

ram_image = Image.open("/home/naturalcapsule/.config/capsule/ram.png").convert("RGBA")
background_image_ram = ImageTk.PhotoImage(ram_image.resize((200, 200)))

cpu_img = ctk.CTkLabel(app, text='', image=background_image_cpu, bg_color='black')
cpu_img.grid(row=1, column=0, padx=20, pady=20)

cpu_label_info = ctk.CTkLabel(app, text="CPU usage: %", text_color = '#884494', font = custom_font)
cpu_label_info.grid(row=2, column=0, padx=20)

cpu_label_info1 = ctk.CTkLabel(app, text = 'CPU Temp: ', text_color = '#884494', font = custom_font)
cpu_label_info1.grid(row = 3, column = 0, padx = 20)

cpu_label_info2 = ctk.CTkLabel(app, text = 'CPU Freq:', text_color = '#884494', font = ("Arial", 20))
cpu_label_info2.grid(row = 4, column = 0)

cpu_label_info3 = ctk.CTkLabel(app, text = 'CPU Freq:', text_color = '#884494', font = ("Arial", 20))
cpu_label_info3.grid(row = 5, column = 0)

cpu_label_info4 = ctk.CTkLabel(app, text = 'CPU Freq:', text_color = '#884494', font = ("Arial", 20))
cpu_label_info4.grid(row = 6, column = 0)

gpu_img = ctk.CTkLabel(app, text='', image=background_image_gpu, bg_color='#2E2E2E', fg_color = 'black')
gpu_img.grid(row=1, column=1, padx=20, pady=20)

gpu_label_info = ctk.CTkLabel(app, text = 'GPU Usage: %', text_color = '#884494', font = custom_font)
gpu_label_info.grid(row = 2, column = 1, padx = 20)#, pady = 20)

gpu_label_info1 = ctk.CTkLabel(app, text = 'GPU Temp: %', text_color = '#884494', font = custom_font)
gpu_label_info1.grid(row = 3, column = 1, padx = 20)#, pady = 20)

gpu_label_info2 = ctk.CTkLabel(app, text = 'Total VRAM: GB', text_color = '#884494', font = custom_font)
gpu_label_info2.grid(row = 4, column = 1, padx = 20)#, pady = 20)

gpu_label_info3 = ctk.CTkLabel(app, text = 'Used VRAM: GB', text_color = '#884494', font = custom_font)
gpu_label_info3.grid(row = 5, column = 1)#, padx = 20)#, pady = 20)

ram_img = ctk.CTkLabel(app, text='', image=background_image_ram, bg_color='#2E2E2E', fg_color = 'black')
ram_img.grid(row=1, column=2, padx=20, pady=20)

ram_label_info = ctk.CTkLabel(app, text = 'RAM Usage: %', text_color = '#884494', font = custom_font)
ram_label_info.grid(row = 4, column = 2, padx = 20)

ram_label_info1 = ctk.CTkLabel(app, text = 'Total RAM: GB', text_color = '#884494', font = custom_font)
ram_label_info1.grid(row = 2, column = 2, padx = 20)

ram_label_info2 = ctk.CTkLabel(app, text = 'Used RAM: GB', text_color = '#884494', font = custom_font)
ram_label_info2.grid(row = 3, column = 2)#, padx = 20)

button_tab1 = ctk.CTkButton(app, text = 'System', width = 100, command = switch_to_system, bg_color = 'black')
button_tab1.grid(row = 0, column = 1, columnspan = 2)

button_tab2 = ctk.CTkButton(app, text = 'Monitoring', width = 100, bg_color = 'black', fg_color = '#6F42C1', hover_color = '#6C757D')
button_tab2.grid(row = 0, column = 0, columnspan = 2)

exit_button = ctk.CTkButton(app, text = 'Exit Program', command = button_callback, bg_color='black', fg_color = 'purple', hover_color = 'darkred')
exit_button.grid(row=0, column=0, columnspan=3, pady=20)

update_cpu_label()
cpu_temp()
ram_usage()
gpu_usage()
gpu_temp()
ram_info()
ram_info_used()
tot_vram()
used_vram()
cpu_freq()
max_cpu_freq()
min_cpu_freq()

app.mainloop()