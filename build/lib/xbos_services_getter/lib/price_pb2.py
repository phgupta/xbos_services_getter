# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: price.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='price.proto',
  package='price',
  syntax='proto3',
  serialized_options=_b('P\001'),
  serialized_pb=_b('\n\x0bprice.proto\x12\x05price\"G\n\nPricePoint\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x0c\n\x04unit\x18\x03 \x01(\t\x12\x0e\n\x06window\x18\x04 \x01(\t\"o\n\x0cPriceRequest\x12\x0f\n\x07utility\x18\x01 \x01(\t\x12\x0e\n\x06tariff\x18\x02 \x01(\t\x12\x12\n\nprice_type\x18\x03 \x01(\t\x12\r\n\x05start\x18\x04 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x05 \x01(\x03\x12\x0e\n\x06window\x18\x06 \x01(\t\"/\n\nPriceReply\x12!\n\x06prices\x18\x01 \x03(\x0b\x32\x11.price.PricePoint2=\n\x05Price\x12\x34\n\x08GetPrice\x12\x13.price.PriceRequest\x1a\x11.price.PriceReply\"\x00\x42\x02P\x01\x62\x06proto3')
)




_PRICEPOINT = _descriptor.Descriptor(
  name='PricePoint',
  full_name='price.PricePoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='price.PricePoint.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='price.PricePoint.price', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='price.PricePoint.unit', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window', full_name='price.PricePoint.window', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=93,
)


_PRICEREQUEST = _descriptor.Descriptor(
  name='PriceRequest',
  full_name='price.PriceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='utility', full_name='price.PriceRequest.utility', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tariff', full_name='price.PriceRequest.tariff', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_type', full_name='price.PriceRequest.price_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='price.PriceRequest.start', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='price.PriceRequest.end', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window', full_name='price.PriceRequest.window', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=206,
)


_PRICEREPLY = _descriptor.Descriptor(
  name='PriceReply',
  full_name='price.PriceReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prices', full_name='price.PriceReply.prices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=208,
  serialized_end=255,
)

_PRICEREPLY.fields_by_name['prices'].message_type = _PRICEPOINT
DESCRIPTOR.message_types_by_name['PricePoint'] = _PRICEPOINT
DESCRIPTOR.message_types_by_name['PriceRequest'] = _PRICEREQUEST
DESCRIPTOR.message_types_by_name['PriceReply'] = _PRICEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PricePoint = _reflection.GeneratedProtocolMessageType('PricePoint', (_message.Message,), dict(
  DESCRIPTOR = _PRICEPOINT,
  __module__ = 'price_pb2'
  # @@protoc_insertion_point(class_scope:price.PricePoint)
  ))
_sym_db.RegisterMessage(PricePoint)

PriceRequest = _reflection.GeneratedProtocolMessageType('PriceRequest', (_message.Message,), dict(
  DESCRIPTOR = _PRICEREQUEST,
  __module__ = 'price_pb2'
  # @@protoc_insertion_point(class_scope:price.PriceRequest)
  ))
_sym_db.RegisterMessage(PriceRequest)

PriceReply = _reflection.GeneratedProtocolMessageType('PriceReply', (_message.Message,), dict(
  DESCRIPTOR = _PRICEREPLY,
  __module__ = 'price_pb2'
  # @@protoc_insertion_point(class_scope:price.PriceReply)
  ))
_sym_db.RegisterMessage(PriceReply)


DESCRIPTOR._options = None

_PRICE = _descriptor.ServiceDescriptor(
  name='Price',
  full_name='price.Price',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=257,
  serialized_end=318,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetPrice',
    full_name='price.Price.GetPrice',
    index=0,
    containing_service=None,
    input_type=_PRICEREQUEST,
    output_type=_PRICEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRICE)

DESCRIPTOR.services_by_name['Price'] = _PRICE

# @@protoc_insertion_point(module_scope)
