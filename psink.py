#!/usr/bin/python2

import sys
import os
import argparse

PATHROOT='.'

def add_paper(p):
  path=PATHROOT+'/'+'/'.join(p)
  command='mkdir -p %s' % path
  os.system(command)

def del_paper(p):
  pass

def main():
  parser = argparse.ArgumentParser(description='Sink Papers.')
  parser.add_argument('--add','-a',dest='ADD',nargs=3,help='add new paper')
  parser.add_argument('--remove','-r',dest='DEL',nargs=3,help='del exist paper')
  parser.add_argument('--paper','-p',help='paper name')
  parser.add_argument('--version','-v',action='version',version='%(prog)s 1.0')
  args = parser.parse_args()
  if args.ADD:
    add_paper(args.ADD)
  if args.DEL:
    del_paper(args.DEL)

if __name__ == "__main__":
  main()

