import sys
import grpc
import nidaqmx_pb2 as nidaqmx_types
import nidaqmx_pb2_grpc as grpc_nidaqmx

# Default values
SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"

# Override defaults from command-line arguments
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]

# Create a gRPC channel and client
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nidaqmx.NiDAQmxStub(channel)

def list_nidaq_devices():
    response = client.GetSystemInfoAttributeString(
        nidaqmx_types.GetSystemInfoAttributeStringRequest(
            attribute=nidaqmx_types.SystemStringAttribute.SYSTEM_ATTRIBUTE_DEV_NAMES
        )
    )
    devices = response.value.split(',')
    print("Devices:", devices)
    return devices

def print_all_ai_channels():
    devices = list_nidaq_devices()
    for device in devices:
        response = client.GetDeviceAttributeString(
            nidaqmx_types.GetDeviceAttributeStringRequest(
                device_name=device,
                attribute=nidaqmx_types.DeviceStringAttribute.DEVICE_ATTRIBUTE_AI_PHYSICAL_CHANS
            )
        )
        print(f"AI Channels for {device}:", response.value.split(','))

def print_all_ao_channels():
    devices = list_nidaq_devices()
    for device in devices:
        response = client.GetDeviceAttributeString(
            nidaqmx_types.GetDeviceAttributeStringRequest(
                device_name=device,
                attribute=nidaqmx_types.DeviceStringAttribute.DEVICE_ATTRIBUTE_AO_PHYSICAL_CHANS
            )
        )
        print(f"AO Channels for {device}:", response.value.split(','))

def print_all_di_channels():
    devices = list_nidaq_devices()
    for device in devices:
        response = client.GetDeviceAttributeString(
            nidaqmx_types.GetDeviceAttributeStringRequest(
                device_name=device,
                attribute=nidaqmx_types.DeviceStringAttribute.DEVICE_ATTRIBUTE_DI_LINES
            )
        )
        print(f"DI Channels for {device}:", response.value.split(','))

def print_all_do_channels():
    devices = list_nidaq_devices()
    for device in devices:
        response = client.GetDeviceAttributeString(
            nidaqmx_types.GetDeviceAttributeStringRequest(
                device_name=device,
                attribute=nidaqmx_types.DeviceStringAttribute.DEVICE_ATTRIBUTE_DO_LINES
            )
        )
        print(f"DO Channels for {device}:", response.value.split(','))

def print_all_ci_channels():
    devices = list_nidaq_devices()
    for device in devices:
        response = client.GetDeviceAttributeString(
            nidaqmx_types.GetDeviceAttributeStringRequest(
                device_name=device,
                attribute=nidaqmx_types.DeviceStringAttribute.DEVICE_ATTRIBUTE_CI_PHYSICAL_CHANS
            )
        )
        print(f"CI Channels for {device}:", response.value.split(','))

def print_all_co_channels():
    devices = list_nidaq_devices()
    for device in devices:
        response = client.GetDeviceAttributeString(
            nidaqmx_types.GetDeviceAttributeStringRequest(
                device_name=device,
                attribute=nidaqmx_types.DeviceStringAttribute.DEVICE_ATTRIBUTE_CO_PHYSICAL_CHANS
            )
        )
        print(f"CO Channels for {device}:", response.value.split(','))

def print_supported_measurement_types():
    devices = list_nidaq_devices()
    for device in devices:
        response = client.GetDeviceAttributeInt32Array(
            nidaqmx_types.GetDeviceAttributeInt32ArrayRequest(
                device_name=device,
                attribute=nidaqmx_types.DeviceInt32ArrayAttribute.DEVICE_ATTRIBUTE_AI_SUPPORTED_MEAS_TYPES
            )
        )
        print(f"Supported AI Measurement Types for {device}:", response.value_raw)

def print_product_info():
    devices = list_nidaq_devices()
    for device in devices:
        response = client.GetDeviceAttributeString(
            nidaqmx_types.GetDeviceAttributeStringRequest(
                device_name=device,
                attribute=nidaqmx_types.DeviceStringAttribute.DEVICE_ATTRIBUTE_PRODUCT_TYPE
            )
        )
        print(f"Product Type for {device}:", response.value)

        response = client.GetDeviceAttributeUInt32(
            nidaqmx_types.GetDeviceAttributeUInt32Request(
                device_name=device,
                attribute=nidaqmx_types.DeviceUInt32Attribute.DEVICE_ATTRIBUTE_SERIAL_NUM
            )
        )
        print(f"Serial Number for {device}:", response.value)

# # Example usage
# if __name__ == "__main__":
#     print("Listing all devices:")
#     list_nidaq_devices()

#     print("\nListing all AI channels:")
#     print_all_ai_channels()

#     print("\nListing all AO channels:")
#     print_all_ao_channels()

#     print("\nListing all DI channels:")
#     print_all_di_channels()

#     print("\nListing all DO channels:")
#     print_all_do_channels()

#     print("\nListing all CI channels:")
#     print_all_ci_channels()

#     print("\nListing all CO channels:")
#     print_all_co_channels()

#     print("\nListing supported measurement types:")
#     print_supported_measurement_types()

#     print("\nListing product info:")
#     print_product_info()

