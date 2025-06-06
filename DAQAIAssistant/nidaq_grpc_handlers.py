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

def get_ai_channels(device_name):
    response = client.GetDeviceAttributeString(
        nidaqmx_types.GetDeviceAttributeStringRequest(
            device_name=device_name,
            attribute=nidaqmx_types.DeviceStringAttribute.DEVICE_ATTRIBUTE_AI_PHYSICAL_CHANS
        )
    )
    print(f"AI Channels for {device_name}:", response.value.split(','))

def get_ao_channels(device_name):
    response = client.GetDeviceAttributeString(
        nidaqmx_types.GetDeviceAttributeStringRequest(
            device_name=device_name,
            attribute=nidaqmx_types.DeviceStringAttribute.DEVICE_ATTRIBUTE_AO_PHYSICAL_CHANS
        )
    )
    print(f"AO Channels for {device_name}:", response.value.split(','))

def get_di_channels(device_name):
    response = client.GetDeviceAttributeString(
        nidaqmx_types.GetDeviceAttributeStringRequest(
            device_name=device_name,
            attribute=nidaqmx_types.DeviceStringAttribute.DEVICE_ATTRIBUTE_DI_LINES
        )
    )
    print(f"DI Channels for {device_name}:", response.value.split(','))

def get_do_channels(device_name):
    response = client.GetDeviceAttributeString(
        nidaqmx_types.GetDeviceAttributeStringRequest(
            device_name=device_name,
            attribute=nidaqmx_types.DeviceStringAttribute.DEVICE_ATTRIBUTE_DO_LINES
        )
    )
    print(f"DO Channels for {device_name}:", response.value.split(','))


# # Example usage
# if __name__ == "__main__":
#     devices = list_nidaq_devices()
#     print("NI-DAQmx Devices:", devices)

#     for device in devices:
#         print(f"AI Channels for {device}:", get_ai_channels(device))
#         print(f"AO Channels for {device}:", get_ao_channels(device))
#         print(f"DI Channels for {device}:", get_di_channels(device))
#         print(f"DO Channels for {device}:", get_do_channels(device))
