#!/usr/bin/env python3

import platform

def do_info():
  global platform
  Machine = platform.machine()
  Version = platform.version()
  Platform = platform.platform()
  System = platform.system()
  Processor = platform.processor()
  return "Sysinfo:\n"+Machine+"\n"+Version+"\n"+Platform+"\n"+System+"\n"+Processor

if __name__ == "__main__":
  print (do_info())
