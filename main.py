import sys
import os
import requests

if __name__ == "__main__":
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
    exit()