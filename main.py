import grpc
import RemouteSmartRieltor_pb2_grpc
import RemouteSmartRieltor_pb2
import pandas as pd
import json
import openpyxl

def pd_to_byte():
    with open('FILE.xlsx', 'rb') as file:
        data = file.read()
        return data

def run():
    with grpc.insecure_channel('localhost:15000') as channel:

        stub = RemouteSmartRieltor_pb2_grpc.ClientServiceStub(channel)
        data = stub.postData(RemouteSmartRieltor_pb2.File(file = pd_to_byte()))
        print("Greeter client received: " + str(data.code))

if __name__ == '__main__':
    run()
