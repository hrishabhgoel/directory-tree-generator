import os
from datetime import datetime as dt
from cv2 import QT_STYLE_OBLIQUE
from docopt import *
from colr import color
from PIL import Image, ImageDraw, ImageFont

# ------------------ colors 
colors = ['#728239', '#fd742d', '#4a9396', '#cb7f07', '#c7bab1', '#a6b401', '#c1dee7', '#6389df', '#f891a0']
borderTopBottom = '-' * 120

# ------------------ methods
# @desc   fileSearch in a dir func
# @params _dirpath: path of _dir to search
#         filename: name of file to search       
# @return allDirs: a string of all diretories 
#                   containing filename 
def fileSearch(_dirpath, filename):
     global colors
     i = 0
     global borderTopBottom
     allDirs = borderTopBottom

     for root, dirs, files in os.walk(_dirpath):
          for file in files:
               if filename in file:
                    if i == len(colors):
                         i = 0
                    allDirs += color("\n" + os.path.join(root,file), fore=colors[i])
                    i += 1
               
     allDirs += borderTopBottom
     return allDirs

# @desc   gentree of a dir func
# @params path: dir to genTree
# @return treePath: tree of path 
def genTree (path): 
     global colors
     i = 0
     global borderTopBottom 
     treePath = borderTopBottom + '\n'

     for root, dirs, files in os.walk(path):

          root = root.replace(path, "")

          # determine the level by counting the os separators
          level = root.count(os.sep)

          # create branch for each file in directory
          if level == 0:
               treePath += color(path + "\n", fore='red')

               for file in files:
                    treePath += color("  "*level + "|--", 'red')
                    treePath += color(file + "\n", colors[i])
                    i += 1
          else:
               treePath += color("|" + "--"*level + root + "\n", fore='red', style='bright')

               # create branch for each file in directory
               for file in files:
                    if i == len(colors): i = 0
                    treePath += color("|" + "  "*level + "|--", 'red')
                    treePath += color(file + "\n", colors[i])
                    i += 1

               treePath += color("|\n", fore='red')
     treePath += borderTopBottom
     return treePath

# ------------------ how to use
howToUse = ''' 
     Usage: 
     dtg.py -t <DIRECTORY_PATH>
     dtg.py -s <DIRECTORY_PATH> <FILE_NAME>

''' 

# ------------------ main
args = docopt(howToUse)

if args['-t']:
    output = genTree(args['<DIRECTORY_PATH>'])
    print(output)

if args['-s']:
    output = fileSearch(args['<DIRECTORY_PATH>'], args['<FILE NAME>'])
    print(output)
