import nidaqmx
from nidaqmx.system import System

# Shared state
task = None

def list_nidaq_devices():
    system = System.local()
    print("Connected Devices:")
    for device in system.devices:
        print(f"  {device.name}")

def get_ai_channels():
    for device in System.local().devices:
        print(f"{device.name} AI Channels: {device.ai_physical_chans.channel_names}")

def get_ao_channels():
    for device in System.local().devices:
        print(f"{device.name} AO Channels: {device.ao_physical_chans.channel_names}")

def get_di_channels():
    for device in System.local().devices:
        print(f"{device.name} DI Channels: {device.di_lines.channel_names}")

def get_do_channels():
    for device in System.local().devices:
        print(f"{device.name} DO Channels: {device.do_lines.channel_names}")

def start_ai_task():
    global task
    device = list(System.local().devices)[0].name
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan(f"{device}/ai0")
    task.start()
    print(f"Started AI task on {device}/ai0")

def stop_task():
    global task
    if task:
        task.stop()
        task.close()
        print("Task stopped and closed.")
    else:
        print("No active task.")
