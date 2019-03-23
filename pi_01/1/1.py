import requests

def main():
    response = requests.get("http://google.com")
    
    print("STATUS CODE =", response.status_code, "\n")

    for header in response.headers:
        print("HEADER =", header, "\n")

    print("LENGHT =", len(response.content), "\n")

    print("BODY =",response.text, "\n")

if __name__ == "__main__":
    main()