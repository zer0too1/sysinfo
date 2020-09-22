#!/usr/bin/env python3

import platform

def do_info():
  global platform
  Machine = platform.machine()
  Version = platform.version()
  Platform = platform.platform()
  System = platform.system()
  Processor = platform.processor()
  return "Sysinfo:<br>"+Machine+"<br>"+Version+"<br>"+Platform+"<br>"+System+"<br>"+Processor

if __name__ == "__main__":
  print("Content-type: text/html\n\n")
  print (do_info())
