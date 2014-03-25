#!/usr/bin/python2

import sys
import re
import os
import argparse
from datetime import datetime

PATHROOT='/home/roselone/Documents/paper'

def log(m):
  with open(PATHROOT+'/'+'log','a') as f:
    f.write(m)
    f.close()


def add_paper(p,url):
  path=PATHROOT+'/'+'/'.join(p)
  command1='mkdir -p %s' % path
  command2='cd %s && wget %s' %(path,url)
  os.system(command1)
  os.system(command2)
  log('[%s] add paper %s saved as %s\n' % (datetime.now(),p[2],path))

def del_paper(p):
  pass

def find_paper(name):
  f = open(PATHROOT+'/'+'log','r')
  log = f.read()
  tmp = re.search(r'(%s/.*/%s)'%(PATHROOT,name),log,re.DOTALL)
  if not tmp:
    sys.stderr.write('Could not find the paper named %s\n' % name)
    sys.exit(1)
  return tmp.group(1)

def sink_paper(name):
  path=find_paper(name)
  os.system('vim %s/sink' % path)
  log('[%s] sink paper %s\n' %(datetime.now(),name))

def main():
  parser = argparse.ArgumentParser(description='Sink Papers.')
  parser.add_argument('--add','-a',dest='ADD',nargs=3,help='add new paper(conference year paper_name)')
  parser.add_argument('--remove','-r',dest='DEL',nargs=3,help='del exist paper(conference year paper_name)')
  parser.add_argument('--sink','-s',dest='SINK',help='paper name')
  parser.add_argument('--url',dest='URL',help='download from url')
  parser.add_argument('--version','-v',action='version',version='%(prog)s 1.0')
  args = parser.parse_args()
  if args.ADD:
    add_paper(args.ADD,args.URL)
  if args.DEL:
    del_paper(args.DEL)
  if args.SINK:
    sink_paper(args.SINK)

if __name__ == "__main__":
  main()

