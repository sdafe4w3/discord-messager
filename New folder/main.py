from http.client import HTTPSConnection
from sys import stderr
from json import dumps
from time import sleep

# if it doesn't work, try downloading the missing files with the 'npm install' command
# if it doesn't work, try downloading the missing files with the 'npm install' command
# if it doesn't work, try downloading the missing files with the 'npm install' command
# if it doesn't work, try downloading the missing files with the 'npm install' command
 
header_data = { 
    "content-type": "application/json", 
    "user-agent": "discordapp.com", 
    "authorization": "MTEyMjI3OTM0MjA1MTk1ODg5Nw.GDxlD4.QybS4taSwCgaRoR4cc7BnvoDr3Cs4tDFcLpqMw", # write your account token here
    "host": "discordapp.com", 
    "referer": "https://discord.gg/8TMwJZMX" # this is irrelevant
} 
 
def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 
 
def send_message(conn, channel_id, message_data): 
    try: 
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
         
        if 199 < resp.status < 300: 
            print("Message sent!")
        else: 
            stderr.write(f"HTTP received {resp.status}: {resp.reason}\n") 
    except: 
        stderr.write("There was an error trying to send the message\n") 
 
def main(): 
    message_data = { 
        "content": "test run!!!!", # if this consists of more than one line, use '\n'
        "tts": "false", 
    }
    sleep(10)
    send_message(get_connection(), "1172253610042720266", dumps(message_data))
    sleep(10)
    send_message(get_connection(), "1172253610042720266", dumps(message_data))
    sleep(10)
   

if __name__ == "__main__":
    main()
