import subprocess
import time
from rich import print
from rich.panel import Panel
import requests
from rich.align import Align

#colors
blue = "\033[94;1m"
white = "\033[97;1m"

# banner 
banner = Align.center("""
┬─┐  ┌─┐  ┬  ┬  ┬  ┌─┐
├┬┘  ├┤   └┐┌┘  │  ├─┘
┴└─  └─┘   └┘   ┴  ┴
""")

def Main():
    subprocess.call('clear',shell=False)
    print(Panel(banner,border_style='blue bold'))
    inp = input(f"{blue}hostname :{white} ")
    url = f"https://api.hackertarget.com/reversedns/?q={inp}"
    req = requests.get(url)
    txt = Align.center(req.text)
    print(Panel(txt,border_style='blue bold',highlight=True,title=" INFO "))

if __name__ == "__main__":
    Main()

