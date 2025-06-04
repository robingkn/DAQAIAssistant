import grpc
from nidaqmx_pb2 import ListDevicesRequest, GetPhysicalChannelsRequest
from nidaqmx_pb2_grpc import DeviceServiceStub

# Map channel type enum
CHANNEL_TYPE_AI = 0
CHANNEL_TYPE_AO = 1
CHANNEL_TYPE_DI = 2
CHANNEL_TYPE_DO = 3

# Create a gRPC channel to the NI gRPC Device Server
def get_device_stub(server_address="localhost:31763"):
    channel = grpc.insecure_channel(server_address)
    return DeviceServiceStub(channel)

def list_nidaq_devices(server_address="localhost:31763"):
    stub = get_device_stub(server_address)
    response = stub.ListDevices(ListDevicesRequest())
    return list(response.device_names)

def get_ai_channels(device_name, server_address="localhost:31763"):
    return _get_channels(device_name, CHANNEL_TYPE_AI, server_address)

def get_ao_channels(device_name, server_address="localhost:31763"):
    return _get_channels(device_name, CHANNEL_TYPE_AO, server_address)

def get_di_channels(device_name, server_address="localhost:31763"):
    return _get_channels(device_name, CHANNEL_TYPE_DI, server_address)

def get_do_channels(device_name, server_address="localhost:31763"):
    return _get_channels(device_name, CHANNEL_TYPE_DO, server_address)

def _get_channels(device_name, channel_type, server_address):
    stub = get_device_stub(server_address)
    request = GetPhysicalChannelsRequest(device_name=device_name, channel_type=channel_type)
    response = stub.GetPhysicalChannels(request)
    return list(response.physical_channels)
