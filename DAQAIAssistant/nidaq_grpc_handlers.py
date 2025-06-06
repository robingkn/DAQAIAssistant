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

MEASUREMENT_TYPE_MAP = {
    10322: "Voltage",
    10350: "Voltage RMS",
    10134: "Current",
    10351: "Current RMS",
    15908: "Bridge",
    10181: "Frequency Voltage",
    10278: "Resistance",
    10303: "Temperature (Thermocouple)",
    10302: "Temperature (Thermistor)",
    10301: "Temperature (RTD)",
    10311: "Temperature (Built-in Sensor)",
    10300: "Strain Gage",
    15980: "Rosette Strain Gage",
    10352: "Position (LVDT)",
    10353: "Position (RVDT)",
    14835: "Position (Eddy Current Proximity)",
    10356: "Accelerometer",
    16104: "Acceleration (Charge)",
    16106: "Acceleration (4-Wire DC Voltage)",
    15966: "Velocity (IEPE Sensor)",
    15899: "Force (Bridge)",
    15895: "Force (IEPE Sensor)",
    15902: "Pressure (Bridge)",
    10354: "Sound Pressure (Microphone)",
    15905: "Torque (Bridge)",
    12531: "TEDS Sensor",
    16105: "Charge",
    16201: "Power",
    16204: "Calculated Power"
}

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
        readable = [MEASUREMENT_TYPE_MAP.get(val, f"Unknown ({val})") for val in response.value_raw]
        print(f"Supported AI Measurement Types for {device}:", readable)

def print_product_info():
    devices = list_nidaq_devices()
    for device in devices:
        product_type_response = client.GetDeviceAttributeString(
            nidaqmx_types.GetDeviceAttributeStringRequest(
                device_name=device,
                attribute=nidaqmx_types.DeviceStringAttribute.DEVICE_ATTRIBUTE_PRODUCT_TYPE
            )
        )
        serial_num_response = client.GetDeviceAttributeUInt32(
            nidaqmx_types.GetDeviceAttributeUInt32Request(
                device_name=device,
                attribute=nidaqmx_types.DeviceUInt32Attribute.DEVICE_ATTRIBUTE_SERIAL_NUM
            )
        )
        print(f"Product Type for {device}:", product_type_response.value)
        print(f"Serial Number for {device}:", serial_num_response.value)

# # Example usage
# if __name__ == "__main__":
#     print_all_ai_channels()
#     print_all_ao_channels()
#     print_all_di_channels()
#     print_all_do_channels()
#     print_all_ci_channels()
#     print_all_co_channels()
#     print_supported_measurement_types()
#     print_product_info()

