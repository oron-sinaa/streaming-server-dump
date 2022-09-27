"""

ORGANISATION        : Staqu Technologies Pvt Ltd
AUTHOR              : Aanis Noor, Shashank Kumar
OBJECTIVE           : Create organisation's self-hosted streaming server

PROBLEM STATEMENT   :
1. Pull RTSP
2. GET RTSP pushed
3. Generate RTSP and HLS streams
4. Store DVR
5. Return live thumbnail

"""

import requests


# CONFIG
DOMAIN = "http://localhost:4242"
API_DOMAIN = "http://localhost:4242/api?command="
DVR_FOLDER = "/home/aanisnoor/Personal/Work/respositories/streaming-server-dump/streaming-server-dump/mdvr"

TEST_SOURCES = \
    (
    "rtsp://android:stackqueue@35.207.248.73:1935/live/BerkowitsAsrao11.stream",
    "/home/aanisnoor/Videos/sample.mp4",
    )
TEST_SOURCE = TEST_SOURCES[1]

STREAM_NAME = "test_push"
TARGET = "rtsp://admin:admin%40123@10.101.2.148:554/unicast/c1/s0/live"


def choices(inp):
    match inp:
            case 1:
                print(pull_rtsp())
            
            case 2:
                print(push_rtsp())
                        
            case 3:
                print(push_hls())
                
            case 4:
                print(store_dvr())
                
            case 5:
                print(generate_thumbnail())
                
            case 6:
                exit()

            case _:
                print("Invalid!\n")


def get_ouput_urls():
    # by Shashank Kumar
    outputs_url = f"http://localhost:8080/json_{STREAM_NAME}.js"
    response = requests.get(outputs_url).json()['source']

    return response
    
    out_hls = list(filter(lambda source: source.get('hrn') == "RTSP", response))[0].get('url')


def pull_rtsp():

    call = f'{{"addstream":{{"{STREAM_NAME}":{{"source":"{TEST_SOURCE}","always_on":true}}}}}}'
    print(f"API = {API_DOMAIN}{call}")
    response = requests.get(API_DOMAIN + call)
    called_url = f"{TEST_SOURCE} (source) running at {STREAM_NAME} (stream)"

    return called_url


def push_rtsp():

    call = f'{{"push_start":{{"stream":"{STREAM_NAME}","target":{DVR_FOLDER}/test_push.mkv"}}}}'
    print(f"API = {API_DOMAIN}{call}")
    response = requests.get(API_DOMAIN + call)
    called_url = f"{TEST_SOURCE} (source) pushed to {DVR_FOLDER}/test_push.mkv (stream)"

    return called_url


def push_hls():
    response = get_ouput_urls()
    out_hls = list(filter(lambda X: X.get('hrn') == "HLS (TS)", response))[0].get('url')

    return out_hls
    

def store_dvr():
    
    dvr_location = f"{DVR_FOLDER}/{STREAM_NAME}_$datetime.mkv"
    call = f'{{"push_start":{{"stream":"{STREAM_NAME}","target":{dvr_location}}}}}'
    response = requests.get(API_DOMAIN + call)

    return f"Recording at {dvr_location}"


def generate_thumbnail():

    return "Task pending..."


def main():

    print("MistServer initial API test")
    print("---------------------------\n")
    print("Select a function:")
    print("1. pull_rtsp \n2. push_rtsp \n3. push_hls \n4. store_dvr \n5. generate_thumbnail \n6. exit")

    inp = int(input("\nEnter choice: "))
    
    choices(inp)


if __name__ == "__main__":
    main()