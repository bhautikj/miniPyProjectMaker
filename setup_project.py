#
# Copyright 2018, Bhautik Joshi bjoshi@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
# and associated documentation files (the "Software"), to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software 
# is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial 
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT 
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import argparse
import shutil
import os
import sys

parser = argparse.ArgumentParser(description='Generate a minimal python project, bhautikj-style')
parser.add_argument('-n', '--name', help='project to create')
parser.add_argument('-f', '--force', help='force overwrite of existing project', action='store_true')
args = parser.parse_args()

if not args.name:
   print(sys.stderr, str('The -n/--name argument is required'))
   sys.exit(1)
   
templatePattern = "TEMPLATE"

dirList = [
  "TEMPLATE",
  "TEMPLATE/core",
  "TEMPLATE/tests"
]

fileList = [
  { "fileSrc" : ["TEMPLATE",".gitignore"],
    "fileDst" : ["TEMPLATE",".gitignore"]},
  { "fileSrc" : ["TEMPLATE","TEMPLATE.setup.py"],
    "fileDst" : ["TEMPLATE","setup.py"]},
  { "fileSrc" : ["TEMPLATE","TEMPLATE","__init__.py"],
    "fileDst" : ["TEMPLATE","TEMPLATE","__init__.py"]},
  { "fileSrc" : ["TEMPLATE","TEMPLATE","core","__init__.py"],
    "fileDst" : ["TEMPLATE","TEMPLATE","core","__init__.py"]},
  { "fileSrc" : ["TEMPLATE","TEMPLATE","core","base.py"],
    "fileDst" : ["TEMPLATE","TEMPLATE","core","base.py"]},    
  { "fileSrc" : ["TEMPLATE","TEMPLATE","tests","__init__.py"],
    "fileDst" : ["TEMPLATE","TEMPLATE","tests","__init__.py"]},
  { "fileSrc" : ["TEMPLATE","TEMPLATE","tests","test_base.py"],
    "fileDst" : ["TEMPLATE","TEMPLATE","tests","test_base.py"]}
]

def fixString(str, projName):
  return str.replace(templatePattern, projName)

def createDirs(projName, forceOverwrite):
  if os.path.exists(projName):
    if forceOverwrite == True:
      print(projName + " already exists, removing & reinitializing it")
      shutil.rmtree(projName)
    else:
      raise Exception(projName + " already exists")
    
  os.mkdir(projName)
  for d in dirList:
    os.mkdir(os.path.join(projName, fixString(d, projName)))

def createFiles(projName):
  for fn in fileList:
    src = os.path.join(*fn["fileSrc"])
    rn = lambda x : fixString(x, projName)
    dst = os.path.join(*list(map(rn, fn["fileDst"])))
    with open(src, "r") as srcf:
      outStr = ""
      for line in srcf:
        outStr += fixString(line, projName)
      with open(dst, "w") as outf:
        outf.write(outStr)

def main():
  projName = args.name
  forceOverwrite = False
  if args.force:
    forceOverwrite = True
  print("Creating project: " + projName)
  createDirs(projName, forceOverwrite)
  createFiles(projName)
  
if __name__ == "__main__":
  main()