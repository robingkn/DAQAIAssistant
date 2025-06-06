import nidaqmx
from nidaqmx.system import System

# Shared state
task = None

def list_nidaq_devices():
    system = System.local()
    print("Connected Devices:")
    for device in system.devices:
        print(f"  {device.name}")

def print_all_ai_channels():
    for device in System.local().devices:
        print(f"{device.name} AI Channels: {device.ai_physical_chans.channel_names}")

def print_all_ao_channels():
    for device in System.local().devices:
        print(f"{device.name} AO Channels: {device.ao_physical_chans.channel_names}")

def print_all_di_channels():
    for device in System.local().devices:
        print(f"{device.name} DI Channels: {device.di_lines.channel_names}")

def print_all_do_channels():
    for device in System.local().devices:
        print(f"{device.name} DO Channels: {device.do_lines.channel_names}")