# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import cmdexec.clients.python.sql_command_service_pb2 as sql__command__service__pb2


class SqlCommandServiceStub(object):
    """
    gRPC service for the SQL command execution server
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OpenSession = channel.unary_unary(
            '/com.databricks.command.SqlCommandService/OpenSession',
            request_serializer=sql__command__service__pb2.OpenSessionRequest.SerializeToString,
            response_deserializer=sql__command__service__pb2.OpenSessionRequest.Response.FromString,
        )
        self.CloseSession = channel.unary_unary(
            '/com.databricks.command.SqlCommandService/CloseSession',
            request_serializer=sql__command__service__pb2.CloseSessionRequest.SerializeToString,
            response_deserializer=sql__command__service__pb2.CloseSessionRequest.Response.FromString,
        )
        self.GetSessionInfo = channel.unary_unary(
            '/com.databricks.command.SqlCommandService/GetSessionInfo',
            request_serializer=sql__command__service__pb2.GetSessionInfoRequest.SerializeToString,
            response_deserializer=sql__command__service__pb2.GetSessionInfoRequest.Response.
            FromString,
        )
        self.ExecuteCommand = channel.unary_unary(
            '/com.databricks.command.SqlCommandService/ExecuteCommand',
            request_serializer=sql__command__service__pb2.ExecuteCommandRequest.SerializeToString,
            response_deserializer=sql__command__service__pb2.ExecuteCommandRequest.Response.
            FromString,
        )
        self.StreamExecuteCommand = channel.unary_stream(
            '/com.databricks.command.SqlCommandService/StreamExecuteCommand',
            request_serializer=sql__command__service__pb2.ExecuteCommandRequest.SerializeToString,
            response_deserializer=sql__command__service__pb2.ExecuteCommandRequest.Response.
            FromString,
        )
        self.GetCommandStatus = channel.unary_unary(
            '/com.databricks.command.SqlCommandService/GetCommandStatus',
            request_serializer=sql__command__service__pb2.GetCommandStatusRequest.SerializeToString,
            response_deserializer=sql__command__service__pb2.GetCommandStatusRequest.Response.
            FromString,
        )
        self.FetchCommandResults = channel.unary_unary(
            '/com.databricks.command.SqlCommandService/FetchCommandResults',
            request_serializer=sql__command__service__pb2.FetchCommandResultsRequest.
            SerializeToString,
            response_deserializer=sql__command__service__pb2.FetchCommandResultsRequest.Response.
            FromString,
        )
        self.CloseCommand = channel.unary_unary(
            '/com.databricks.command.SqlCommandService/CloseCommand',
            request_serializer=sql__command__service__pb2.CloseCommandRequest.SerializeToString,
            response_deserializer=sql__command__service__pb2.CloseCommandRequest.Response.FromString,
        )


class SqlCommandServiceServicer(object):
    """
    gRPC service for the SQL command execution server
    """

    def OpenSession(self, request, context):
        """
        Opens a new session using the provided ID or generates a new one.
        Returns the session ID and any requested info
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseSession(self, request, context):
        """Closes the requested session, cancels any active commands, and frees resources 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSessionInfo(self, request, context):
        """Returns the requested session info values 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteCommand(self, request, context):
        """
        Submits a new command to be executed asynchronously. Creates a new session if the session ID
        is not provided, which will be automatically closed when the command is closed.
        Returns the new command ID and command status. It also waits up to a specified amount of time
        (default 5 seconds) for the command to complete. Returns the results if the command
        completes within that time
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamExecuteCommand(self, request, context):
        """
        Submits a new command to be executed asynchronously in the same way as ExecuteCommand,
        but uses a gRPC stream response where the server pushes an update once command execution
        is completed and results are available. The first response is sent as soon as the command
        is submitted and contains the command ID. The second response is sent after the command
        completes, and will contain the command status (SUCCESS or ERROR) along with the first
        result set if available. The server will then close the connection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCommandStatus(self, request, context):
        """Retrieves the status of the requested command 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchCommandResults(self, request, context):
        """
        Fetches command results and metadata from a specified offset. Throws an error if the
        command state is not SUCCESS and returns empty results when there are no rows to return
        or the requested offset is out of bounds
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseCommand(self, request, context):
        """Closes the requested command, cancels active commands, and frees associated resources 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SqlCommandServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'OpenSession': grpc.unary_unary_rpc_method_handler(
            servicer.OpenSession,
            request_deserializer=sql__command__service__pb2.OpenSessionRequest.FromString,
            response_serializer=sql__command__service__pb2.OpenSessionRequest.Response.
            SerializeToString,
        ),
        'CloseSession': grpc.unary_unary_rpc_method_handler(
            servicer.CloseSession,
            request_deserializer=sql__command__service__pb2.CloseSessionRequest.FromString,
            response_serializer=sql__command__service__pb2.CloseSessionRequest.Response.
            SerializeToString,
        ),
        'GetSessionInfo': grpc.unary_unary_rpc_method_handler(
            servicer.GetSessionInfo,
            request_deserializer=sql__command__service__pb2.GetSessionInfoRequest.FromString,
            response_serializer=sql__command__service__pb2.GetSessionInfoRequest.Response.
            SerializeToString,
        ),
        'ExecuteCommand': grpc.unary_unary_rpc_method_handler(
            servicer.ExecuteCommand,
            request_deserializer=sql__command__service__pb2.ExecuteCommandRequest.FromString,
            response_serializer=sql__command__service__pb2.ExecuteCommandRequest.Response.
            SerializeToString,
        ),
        'StreamExecuteCommand': grpc.unary_stream_rpc_method_handler(
            servicer.StreamExecuteCommand,
            request_deserializer=sql__command__service__pb2.ExecuteCommandRequest.FromString,
            response_serializer=sql__command__service__pb2.ExecuteCommandRequest.Response.
            SerializeToString,
        ),
        'GetCommandStatus': grpc.unary_unary_rpc_method_handler(
            servicer.GetCommandStatus,
            request_deserializer=sql__command__service__pb2.GetCommandStatusRequest.FromString,
            response_serializer=sql__command__service__pb2.GetCommandStatusRequest.Response.
            SerializeToString,
        ),
        'FetchCommandResults': grpc.unary_unary_rpc_method_handler(
            servicer.FetchCommandResults,
            request_deserializer=sql__command__service__pb2.FetchCommandResultsRequest.FromString,
            response_serializer=sql__command__service__pb2.FetchCommandResultsRequest.Response.
            SerializeToString,
        ),
        'CloseCommand': grpc.unary_unary_rpc_method_handler(
            servicer.CloseCommand,
            request_deserializer=sql__command__service__pb2.CloseCommandRequest.FromString,
            response_serializer=sql__command__service__pb2.CloseCommandRequest.Response.
            SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'com.databricks.command.SqlCommandService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler, ))


# This class is part of an EXPERIMENTAL API.
class SqlCommandService(object):
    """
    gRPC service for the SQL command execution server
    """

    @staticmethod
    def OpenSession(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/com.databricks.command.SqlCommandService/OpenSession',
            sql__command__service__pb2.OpenSessionRequest.SerializeToString,
            sql__command__service__pb2.OpenSessionRequest.Response.FromString, options,
            channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)

    @staticmethod
    def CloseSession(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/com.databricks.command.SqlCommandService/CloseSession',
            sql__command__service__pb2.CloseSessionRequest.SerializeToString,
            sql__command__service__pb2.CloseSessionRequest.Response.FromString, options,
            channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)

    @staticmethod
    def GetSessionInfo(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/com.databricks.command.SqlCommandService/GetSessionInfo',
            sql__command__service__pb2.GetSessionInfoRequest.SerializeToString,
            sql__command__service__pb2.GetSessionInfoRequest.Response.FromString, options,
            channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)

    @staticmethod
    def ExecuteCommand(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/com.databricks.command.SqlCommandService/ExecuteCommand',
            sql__command__service__pb2.ExecuteCommandRequest.SerializeToString,
            sql__command__service__pb2.ExecuteCommandRequest.Response.FromString, options,
            channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)

    @staticmethod
    def StreamExecuteCommand(request,
                             target,
                             options=(),
                             channel_credentials=None,
                             call_credentials=None,
                             insecure=False,
                             compression=None,
                             wait_for_ready=None,
                             timeout=None,
                             metadata=None):
        return grpc.experimental.unary_stream(
            request, target, '/com.databricks.command.SqlCommandService/StreamExecuteCommand',
            sql__command__service__pb2.ExecuteCommandRequest.SerializeToString,
            sql__command__service__pb2.ExecuteCommandRequest.Response.FromString, options,
            channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)

    @staticmethod
    def GetCommandStatus(request,
                         target,
                         options=(),
                         channel_credentials=None,
                         call_credentials=None,
                         insecure=False,
                         compression=None,
                         wait_for_ready=None,
                         timeout=None,
                         metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/com.databricks.command.SqlCommandService/GetCommandStatus',
            sql__command__service__pb2.GetCommandStatusRequest.SerializeToString,
            sql__command__service__pb2.GetCommandStatusRequest.Response.FromString, options,
            channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)

    @staticmethod
    def FetchCommandResults(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/com.databricks.command.SqlCommandService/FetchCommandResults',
            sql__command__service__pb2.FetchCommandResultsRequest.SerializeToString,
            sql__command__service__pb2.FetchCommandResultsRequest.Response.FromString, options,
            channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)

    @staticmethod
    def CloseCommand(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/com.databricks.command.SqlCommandService/CloseCommand',
            sql__command__service__pb2.CloseCommandRequest.SerializeToString,
            sql__command__service__pb2.CloseCommandRequest.Response.FromString, options,
            channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)