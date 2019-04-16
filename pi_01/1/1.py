import sys
import os
import requests
from img import getImage

def main():
    args = sys.argv[1:]

    if "http" in args[-1]:
        response = requests.get(args[-1])

        if "-s" in args:
            print("STATUS CODE =", response.status_code)

        if "-h" in args:
            for header in response.headers:
                print("HEADER = ", header, end=" :: ")

        if "-l" in args:
            print("LENGHT = ", len(response.content))

        if "-b" in args:
            print("BODY = ", response.content)
            
        if "-img" in args and len(args) == 2:
            try:
                os.mkdir("images")
                print("Directory 'images' Created")
            except FileExistsError:
                print("Directory 'images' already exits")
            if getImage(response, "images/"):
                print("File sucess saved!")
            else:
                print("File is not a image")
            

        
if __name__ == "__main__":
    main()