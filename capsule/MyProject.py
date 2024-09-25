import subprocess
import psutil
import subprocess
import customtkinter as ctk
import sys
from PIL import Image, ImageTk

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

app = ctk.CTk()
app.geometry('1000x600')
app.title('Linux')
app.wm_iconname('/home/naturalcapsule/.config/rocket.ico')
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

gpu_img = ctk.CTkLabel(app, text='', image=background_image_gpu, bg_color='#2E2E2E', fg_color = 'black')
gpu_img.grid(row=1, column=1, padx=20, pady=20)

gpu_label_info = ctk.CTkLabel(app, text = 'GPU Usage: %', text_color = '#884494', font = custom_font)
gpu_label_info.grid(row = 2, column = 1, padx = 20)#, pady = 20)

gpu_label_info1 = ctk.CTkLabel(app, text = 'GPU Temp: %', text_color = '#884494', font = custom_font)
gpu_label_info1.grid(row = 3, column = 1, padx = 20)#, pady = 20)

ram_img = ctk.CTkLabel(app, text='', image=background_image_ram, bg_color='#2E2E2E', fg_color = 'black')
ram_img.grid(row=1, column=2, padx=20, pady=20)

ram_label_info = ctk.CTkLabel(app, text = 'RAM Usage: %', text_color = '#884494', font = custom_font)
ram_label_info.grid(row = 2, column = 2, padx = 20)

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

app.mainloop()