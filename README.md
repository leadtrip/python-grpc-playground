Playing around with GRPC, there are few sample apps in here, the following describes setting up and running one of them
the process is the same for the other client/server apps, just change the file names when starting.

Java clients exist for the greet and SE examples in here - https://github.com/leadtrip/grpc-playground

### setup
`pip3 install grpcio-tools`

### generate grpc code from proto files 
Do this after each time you change a proto file

`python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/*.proto`

### start the server
`python3 se_server.py`

### start the client
`python3 se_client.py`