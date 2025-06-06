# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: data_moniker.proto
# Protobuf Python Version: 6.30.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    0,
    '',
    'data_moniker.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x64\x61ta_moniker.proto\x12\x10ni.data_monikers\x1a\x19google/protobuf/any.proto\"\x8a\x01\n!BeginMonikerSidebandStreamRequest\x12\x34\n\x08strategy\x18\x01 \x01(\x0e\x32\".ni.data_monikers.SidebandStrategy\x12/\n\x08monikers\x18\x02 \x01(\x0b\x32\x1d.ni.data_monikers.MonikerList\"\xa4\x01\n\"BeginMonikerSidebandStreamResponse\x12\x34\n\x08strategy\x18\x01 \x01(\x0e\x32\".ni.data_monikers.SidebandStrategy\x12\x16\n\x0e\x63onnection_url\x18\x02 \x01(\t\x12\x1b\n\x13sideband_identifier\x18\x03 \x01(\t\x12\x13\n\x0b\x62uffer_size\x18\x04 \x01(\x12\"O\n\x07Moniker\x12\x18\n\x10service_location\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x61ta_source\x18\x02 \x01(\t\x12\x15\n\rdata_instance\x18\x03 \x01(\x03\"\x87\x01\n\x13MonikerWriteRequest\x12\x31\n\x08monikers\x18\x01 \x01(\x0b\x32\x1d.ni.data_monikers.MonikerListH\x00\x12/\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1f.ni.data_monikers.MonikerValuesH\x00\x42\x0c\n\nwrite_data\"D\n\x13MonikerReadResponse\x12-\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1f.ni.data_monikers.MonikerValues\"r\n\x0bMonikerList\x12\x30\n\rread_monikers\x18\x02 \x03(\x0b\x32\x19.ni.data_monikers.Moniker\x12\x31\n\x0ewrite_monikers\x18\x03 \x03(\x0b\x32\x19.ni.data_monikers.Moniker\"5\n\rMonikerValues\x12$\n\x06values\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\"W\n\x14SidebandWriteRequest\x12\x0e\n\x06\x63\x61ncel\x18\x01 \x01(\x08\x12/\n\x06values\x18\x02 \x01(\x0b\x32\x1f.ni.data_monikers.MonikerValues\"W\n\x14SidebandReadResponse\x12\x0e\n\x06\x63\x61ncel\x18\x01 \x01(\x08\x12/\n\x06values\x18\x02 \x01(\x0b\x32\x1f.ni.data_monikers.MonikerValues\"\x15\n\x13StreamWriteResponse*\xbd\x01\n\x10SidebandStrategy\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04GRPC\x10\x01\x12\x11\n\rSHARED_MEMORY\x10\x02\x12!\n\x1d\x44OUBLE_BUFFERED_SHARED_MEMORY\x10\x03\x12\x0b\n\x07SOCKETS\x10\x04\x12\x17\n\x13SOCKETS_LOW_LATENCY\x10\x05\x12\x16\n\x12HYPERVISOR_SOCKETS\x10\x06\x12\x08\n\x04RDMA\x10\x07\x12\x14\n\x10RDMA_LOW_LATENCY\x10\x08\x32\xb4\x03\n\x0b\x44\x61taMoniker\x12\x82\x01\n\x13\x42\x65ginSidebandStream\x12\x33.ni.data_monikers.BeginMonikerSidebandStreamRequest\x1a\x34.ni.data_monikers.BeginMonikerSidebandStreamResponse\"\x00\x12\x65\n\x0fStreamReadWrite\x12%.ni.data_monikers.MonikerWriteRequest\x1a%.ni.data_monikers.MonikerReadResponse\"\x00(\x01\x30\x01\x12V\n\nStreamRead\x12\x1d.ni.data_monikers.MonikerList\x1a%.ni.data_monikers.MonikerReadResponse\"\x00\x30\x01\x12\x61\n\x0bStreamWrite\x12%.ni.data_monikers.MonikerWriteRequest\x1a%.ni.data_monikers.StreamWriteResponse\"\x00(\x01\x30\x01\x42&\xf8\x01\x01\xaa\x02 NationalInstruments.DataMonikersb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data_moniker_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001\252\002 NationalInstruments.DataMonikers'
  _globals['_SIDEBANDSTRATEGY']._serialized_start=1037
  _globals['_SIDEBANDSTRATEGY']._serialized_end=1226
  _globals['_BEGINMONIKERSIDEBANDSTREAMREQUEST']._serialized_start=68
  _globals['_BEGINMONIKERSIDEBANDSTREAMREQUEST']._serialized_end=206
  _globals['_BEGINMONIKERSIDEBANDSTREAMRESPONSE']._serialized_start=209
  _globals['_BEGINMONIKERSIDEBANDSTREAMRESPONSE']._serialized_end=373
  _globals['_MONIKER']._serialized_start=375
  _globals['_MONIKER']._serialized_end=454
  _globals['_MONIKERWRITEREQUEST']._serialized_start=457
  _globals['_MONIKERWRITEREQUEST']._serialized_end=592
  _globals['_MONIKERREADRESPONSE']._serialized_start=594
  _globals['_MONIKERREADRESPONSE']._serialized_end=662
  _globals['_MONIKERLIST']._serialized_start=664
  _globals['_MONIKERLIST']._serialized_end=778
  _globals['_MONIKERVALUES']._serialized_start=780
  _globals['_MONIKERVALUES']._serialized_end=833
  _globals['_SIDEBANDWRITEREQUEST']._serialized_start=835
  _globals['_SIDEBANDWRITEREQUEST']._serialized_end=922
  _globals['_SIDEBANDREADRESPONSE']._serialized_start=924
  _globals['_SIDEBANDREADRESPONSE']._serialized_end=1011
  _globals['_STREAMWRITERESPONSE']._serialized_start=1013
  _globals['_STREAMWRITERESPONSE']._serialized_end=1034
  _globals['_DATAMONIKER']._serialized_start=1229
  _globals['_DATAMONIKER']._serialized_end=1665
# @@protoc_insertion_point(module_scope)
