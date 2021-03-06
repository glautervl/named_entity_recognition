# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from services.model import named_entity_recognition_rpc_pb2 as services_dot_model_dot_named__entity__recognition__rpc__pb2


class ShowMessageStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.show = channel.unary_unary(
        '/ShowMessage/show',
        request_serializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.InputMessage.SerializeToString,
        response_deserializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.OutputMessage.FromString,
        )


class ShowMessageServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def show(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ShowMessageServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'show': grpc.unary_unary_rpc_method_handler(
          servicer.show,
          request_deserializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.InputMessage.FromString,
          response_serializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.OutputMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ShowMessage', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class TaggingMessageStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.tag = channel.unary_unary(
        '/TaggingMessage/tag',
        request_serializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.InputMessage.SerializeToString,
        response_deserializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.OutputMessage.FromString,
        )


class TaggingMessageServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def tag(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TaggingMessageServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'tag': grpc.unary_unary_rpc_method_handler(
          servicer.tag,
          request_deserializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.InputMessage.FromString,
          response_serializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.OutputMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'TaggingMessage', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class TokenizeMessageStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.tokenize = channel.unary_unary(
        '/TokenizeMessage/tokenize',
        request_serializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.InputMessage.SerializeToString,
        response_deserializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.OutputMessage.FromString,
        )


class TokenizeMessageServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def tokenize(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TokenizeMessageServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'tokenize': grpc.unary_unary_rpc_method_handler(
          servicer.tokenize,
          request_deserializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.InputMessage.FromString,
          response_serializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.OutputMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'TokenizeMessage', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ChunkMessageStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.chunk = channel.unary_unary(
        '/ChunkMessage/chunk',
        request_serializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.InputMessage.SerializeToString,
        response_deserializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.OutputMessage.FromString,
        )


class ChunkMessageServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def chunk(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChunkMessageServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'chunk': grpc.unary_unary_rpc_method_handler(
          servicer.chunk,
          request_deserializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.InputMessage.FromString,
          response_serializer=services_dot_model_dot_named__entity__recognition__rpc__pb2.OutputMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ChunkMessage', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
