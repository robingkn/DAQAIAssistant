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
        chans = [chan.name for chan in device.ai_physical_chans]
        print(f"{device.name} AI Channels: {chans}")

def print_all_ao_channels():
    for device in System.local().devices:
        chans = [chan.name for chan in device.ao_physical_chans]
        print(f"{device.name} AO Channels: {chans}")

def print_all_di_channels():
    for device in System.local().devices:
        chans = [chan.name for chan in device.di_lines]
        print(f"{device.name} DI Channels: {chans}")

def print_all_do_channels():
    for device in System.local().devices:
        chans = [chan.name for chan in device.do_lines]
        print(f"{device.name} DO Channels: {chans}")

def print_all_ci_channels():
    for device in System.local().devices:
        chans = [chan.name for chan in device.ci_physical_chans]
        print(f"{device.name} CI Channels: {chans}")

def print_all_co_channels():
    for device in System.local().devices:
        chans = [chan.name for chan in device.co_physical_chans]
        print(f"{device.name} CO Channels: {chans}")

        
def print_supported_measurement_types():
    print("This feature is only available via the NI-DAQmx gRPC API.")

def print_product_info():
    for device in System.local().devices:
        print(f"Device: {device.name}")
        print(f"  Product Type: {device.product_type}")
        print(f"  Serial Number: {device.serial_num}")


# # Example usage
# if __name__ == "__main__":
#     print_all_ai_channels()
#     print_all_ao_channels()
#     print_all_di_channels()
#     print_all_do_channels()
#     print_all_ci_channels()
#     print_all_co_channels()
#     print_product_info()