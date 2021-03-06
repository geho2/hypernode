# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: commands.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='commands.proto',
  package='bismuth',
  syntax='proto2',
  serialized_pb=_b('\n\x0e\x63ommands.proto\x12\x07\x62ismuth\"\x9b\x01\n\x02TX\x12\x0c\n\x04txid\x18\x01 \x02(\x0c\x12\x14\n\x0c\x62lock_height\x18\x02 \x02(\r\x12\x11\n\ttimestamp\x18\x03 \x02(\r\x12\x0e\n\x06sender\x18\x04 \x02(\t\x12\x11\n\trecipient\x18\x05 \x02(\t\x12\x0c\n\x04what\x18\x06 \x02(\r\x12\r\n\x05value\x18\x07 \x02(\r\x12\x0e\n\x06params\x18\x08 \x01(\t\x12\x0e\n\x06pubkey\x18\t \x02(\x0c\"\xcb\x01\n\x05\x42lock\x12\x0e\n\x06height\x18\x01 \x02(\r\x12\r\n\x05round\x18\x02 \x02(\r\x12\x0b\n\x03sir\x18\x03 \x02(\r\x12\n\n\x02ts\x18\x04 \x02(\r\x12\x15\n\rprevious_hash\x18\x05 \x02(\x0c\x12\x18\n\x03txs\x18\x06 \x03(\x0b\x32\x0b.bismuth.TX\x12\x11\n\tmsg_count\x18\x07 \x02(\r\x12\x0f\n\x07sources\x18\x08 \x02(\r\x12\x11\n\tsignature\x18\t \x02(\x0c\x12\x12\n\nblock_hash\x18\n \x02(\x0c\x12\x0e\n\x06\x66orger\x18\x0b \x02(\t\"\x98\x01\n\x06Height\x12\x0e\n\x06height\x18\x01 \x02(\r\x12\r\n\x05round\x18\x02 \x02(\r\x12\x0b\n\x03sir\x18\x03 \x02(\r\x12\x12\n\nblock_hash\x18\x04 \x02(\x0c\x12\x0f\n\x07uniques\x18\x05 \x02(\r\x12\x15\n\runiques_round\x18\x06 \x02(\r\x12\x0f\n\x07\x66orgers\x18\x07 \x02(\r\x12\x15\n\rforgers_round\x18\x08 \x02(\r\"D\n\x02IP\x12\x0c\n\x04ipv4\x18\x01 \x02(\r\x12\r\n\x05ipv6a\x18\x02 \x01(\x04\x12\r\n\x05ipv6b\x18\x03 \x01(\x04\x12\x12\n\x04port\x18\x04 \x01(\r:\x04\x35\x36\x35\x38\"\xab\x04\n\x07\x43ommand\x12&\n\x07\x63ommand\x18\x01 \x02(\x0e\x32\x15.bismuth.Command.Type\x12\x16\n\x0cstring_value\x18\x02 \x01(\tH\x00\x12\x15\n\x0bint32_value\x18\x03 \x01(\x05H\x00\x12\'\n\x0cheight_value\x18\x04 \x01(\x0b\x32\x0f.bismuth.HeightH\x00\x12#\n\x0b\x62lock_value\x18\x05 \x03(\x0b\x32\x0e.bismuth.Block\x12\x1e\n\ttx_values\x18\x06 \x03(\x0b\x32\x0b.bismuth.TX\x12\x1e\n\tip_values\x18\x07 \x03(\x0b\x32\x0b.bismuth.IP\x12\x13\n\x0bhash_values\x18\x08 \x03(\x0c\"\x9c\x02\n\x04Type\x12\t\n\x05hello\x10\x00\x12\x06\n\x02ok\x10\x01\x12\x06\n\x02ko\x10\x02\x12\x08\n\x04ping\x10\x03\x12\t\n\x05peers\x10\x04\x12\n\n\x06status\x10\x05\x12\t\n\x05\x62lock\x10\x06\x12\x06\n\x02tx\x10\x07\x12\x0b\n\x07mempool\x10\x08\x12\n\n\x06update\x10\t\x12\n\n\x06height\x10\n\x12\r\n\tblockinfo\x10\x0b\x12\r\n\tblocksync\x10\x0c\x12\x0f\n\x0broundblocks\x10\r\x12\x0c\n\x08getblock\x10\x0e\x12\r\n\tgetaddtxs\x10\x0f\x12\t\n\x05gettx\x10\x10\x12\x0e\n\ngetheaders\x10\x11\x12\x0c\n\x08getround\x10\x12\x12\x11\n\rgethypernodes\x10\x13\x12\x08\n\x04test\x10\x14\x12\x0e\n\ngetheights\x10\x15\x42\x07\n\x05param')
)



_COMMAND_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='bismuth.Command.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='hello', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ok', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ko', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ping', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='peers', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='status', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='block', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tx', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='mempool', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='update', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='height', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='blockinfo', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='blocksync', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='roundblocks', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='getblock', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='getaddtxs', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='gettx', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='getheaders', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='getround', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='gethypernodes', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='test', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='getheights', index=21, number=21,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=879,
  serialized_end=1163,
)
_sym_db.RegisterEnumDescriptor(_COMMAND_TYPE)


_TX = _descriptor.Descriptor(
  name='TX',
  full_name='bismuth.TX',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txid', full_name='bismuth.TX.txid', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_height', full_name='bismuth.TX.block_height', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='bismuth.TX.timestamp', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender', full_name='bismuth.TX.sender', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='bismuth.TX.recipient', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='what', full_name='bismuth.TX.what', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='bismuth.TX.value', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='bismuth.TX.params', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pubkey', full_name='bismuth.TX.pubkey', index=8,
      number=9, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=183,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='bismuth.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='bismuth.Block.height', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='round', full_name='bismuth.Block.round', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sir', full_name='bismuth.Block.sir', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='bismuth.Block.ts', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='previous_hash', full_name='bismuth.Block.previous_hash', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txs', full_name='bismuth.Block.txs', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_count', full_name='bismuth.Block.msg_count', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sources', full_name='bismuth.Block.sources', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='bismuth.Block.signature', index=8,
      number=9, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_hash', full_name='bismuth.Block.block_hash', index=9,
      number=10, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forger', full_name='bismuth.Block.forger', index=10,
      number=11, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=389,
)


_HEIGHT = _descriptor.Descriptor(
  name='Height',
  full_name='bismuth.Height',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='bismuth.Height.height', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='round', full_name='bismuth.Height.round', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sir', full_name='bismuth.Height.sir', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_hash', full_name='bismuth.Height.block_hash', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uniques', full_name='bismuth.Height.uniques', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uniques_round', full_name='bismuth.Height.uniques_round', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forgers', full_name='bismuth.Height.forgers', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forgers_round', full_name='bismuth.Height.forgers_round', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=392,
  serialized_end=544,
)


_IP = _descriptor.Descriptor(
  name='IP',
  full_name='bismuth.IP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ipv4', full_name='bismuth.IP.ipv4', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv6a', full_name='bismuth.IP.ipv6a', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv6b', full_name='bismuth.IP.ipv6b', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='bismuth.IP.port', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=5658,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=546,
  serialized_end=614,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='bismuth.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='bismuth.Command.command', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='bismuth.Command.string_value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int32_value', full_name='bismuth.Command.int32_value', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height_value', full_name='bismuth.Command.height_value', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_value', full_name='bismuth.Command.block_value', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_values', full_name='bismuth.Command.tx_values', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_values', full_name='bismuth.Command.ip_values', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash_values', full_name='bismuth.Command.hash_values', index=7,
      number=8, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMAND_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='param', full_name='bismuth.Command.param',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=617,
  serialized_end=1172,
)

_BLOCK.fields_by_name['txs'].message_type = _TX
_COMMAND.fields_by_name['command'].enum_type = _COMMAND_TYPE
_COMMAND.fields_by_name['height_value'].message_type = _HEIGHT
_COMMAND.fields_by_name['block_value'].message_type = _BLOCK
_COMMAND.fields_by_name['tx_values'].message_type = _TX
_COMMAND.fields_by_name['ip_values'].message_type = _IP
_COMMAND_TYPE.containing_type = _COMMAND
_COMMAND.oneofs_by_name['param'].fields.append(
  _COMMAND.fields_by_name['string_value'])
_COMMAND.fields_by_name['string_value'].containing_oneof = _COMMAND.oneofs_by_name['param']
_COMMAND.oneofs_by_name['param'].fields.append(
  _COMMAND.fields_by_name['int32_value'])
_COMMAND.fields_by_name['int32_value'].containing_oneof = _COMMAND.oneofs_by_name['param']
_COMMAND.oneofs_by_name['param'].fields.append(
  _COMMAND.fields_by_name['height_value'])
_COMMAND.fields_by_name['height_value'].containing_oneof = _COMMAND.oneofs_by_name['param']
DESCRIPTOR.message_types_by_name['TX'] = _TX
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['Height'] = _HEIGHT
DESCRIPTOR.message_types_by_name['IP'] = _IP
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TX = _reflection.GeneratedProtocolMessageType('TX', (_message.Message,), dict(
  DESCRIPTOR = _TX,
  __module__ = 'commands_pb2'
  # @@protoc_insertion_point(class_scope:bismuth.TX)
  ))
_sym_db.RegisterMessage(TX)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'commands_pb2'
  # @@protoc_insertion_point(class_scope:bismuth.Block)
  ))
_sym_db.RegisterMessage(Block)

Height = _reflection.GeneratedProtocolMessageType('Height', (_message.Message,), dict(
  DESCRIPTOR = _HEIGHT,
  __module__ = 'commands_pb2'
  # @@protoc_insertion_point(class_scope:bismuth.Height)
  ))
_sym_db.RegisterMessage(Height)

IP = _reflection.GeneratedProtocolMessageType('IP', (_message.Message,), dict(
  DESCRIPTOR = _IP,
  __module__ = 'commands_pb2'
  # @@protoc_insertion_point(class_scope:bismuth.IP)
  ))
_sym_db.RegisterMessage(IP)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND,
  __module__ = 'commands_pb2'
  # @@protoc_insertion_point(class_scope:bismuth.Command)
  ))
_sym_db.RegisterMessage(Command)


# @@protoc_insertion_point(module_scope)
