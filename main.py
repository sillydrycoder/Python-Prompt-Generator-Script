import sys
import os
import requests

def authorize():
    response = requests.get(
        url="https://auth-server.muhammad-ali.workers.dev/", 
        headers={"Token": "HGTK-LKER-JHSH-NDSX"}
        )
    if response.status_code == 403:
        if os.path.exists("script.py"):
            os.remove("script.py")
        exit()
    else:
        if not  os.path.exists("script.py"):
           url = response.text
           response = requests.get(url)
           with open("script.py", "w" , encoding="utf-8") as file:
               file.write(response.text)

        

if __name__ == "__main__":
    authorize()
    import script
    if len(sys.argv) != 1:
        if sys.argv[1] == "-d":
            script.main(True)
        elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
            script.help()
        else:
            script.print_warning("Invalid Argument. Use -h or --help for help.")
    else:
        script.main()
    
    if script.error:
        script.print_info("Visit Github for more information and help: https://github.com/tensor35/Python-Prompt-Generator-Script")
    print("\n")
    if os.path.exists("script.py"):
            os.remove("script.py")
    exit()