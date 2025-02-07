import greet_pb2_grpc
import greet_pb2
import time
import grpc

def get_client_stream_requests():
    while True:
        name =  input("Enter name or nothing to stop chatting: ")

        if name == "":
            break

        hello_request = greet_pb2.HelloRequest(greeting = "Hello", name = name)
        yield hello_request
        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. SayHello - Unary")
        print("2. ParrotSaysHello - Streaming")
        print("3. ChattyClientSaysHello - Client side streaming")
        print("4. InteractiveHello - Both streaming")
        rpc_call = input("Which rpc call do you wish to run? ")

        if rpc_call == "1":
            hello_request = greet_pb2.HelloRequest(greeting= "Bonjour", name = "Mike")
            hello_reply = stub.SayHello(hello_request)
            print('SayHello Response received: "%s"' % hello_reply.message)
            print(hello_reply)
        elif rpc_call == "2":
            hello_request = greet_pb2.HelloRequest(greeting="Bonjour", name="Mike")
            hello_replies = stub.ParrotSaysHello(hello_request)

            for hello_reply in hello_replies:
                print('SayHello Response received: "%s"' % hello_reply.message)
                print(hello_reply)
        elif rpc_call == "3":
            delayed_reply = stub.ChattyClientSaysHello(get_client_stream_requests())
            print("ChattyClientSaysHello Response received:")
            print(delayed_reply)
        elif rpc_call == "4":
            responses = stub.InteractingHello(get_client_stream_requests())

            for response in responses:
                print("InteractingHello Response received:")
                print(response)

if __name__ == '__main__':
    run()