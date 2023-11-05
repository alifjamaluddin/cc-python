import argparse
import os
import sys
import subprocess
parser = argparse.ArgumentParser(
                    prog='ccwc',
                    description="""
The wc utility displays the number of lines, words, and bytes contained in each input file, or standard input (if no file is
specified) to the standard output.  A line is defined as a string of characters delimited by a <newline> character.  Characters 
beyond the final <newline> character will not be included in the line count.

A word is defined as a string of characters delimited by white space characters.  White space characters are the set of characters for which the iswspace(3) function returns true.  
If more than one input file is specified, a line of cumulative counts for all the files is displayed on a separate line after the output for the last file.""")

parser.add_argument('-c', action='store_true', help="The number of bytes in each input file is written to the standard output.")      
parser.add_argument('-l', action='store_true', help="The number of lines in each input file is written to the standard output.")      
parser.add_argument('-w', action='store_true', help="The number of words in each input file is written to the standard output.")      
parser.add_argument('-m', action='store_true', help="The number of characters in each input file is written to the standard output.")      

parser.add_argument('file', nargs='?',metavar="File", help='file path')

args = parser.parse_args()

filepath = args.file
enableCountByte = args.c
enableCountLine = args.l
enableCountWord = args.w
enableCountChar = args.m


if filepath != None:
    if not os.path.isfile(filepath):
        print("Error: No such file")
        exit()

    f = open(os.path.abspath(filepath), 'r')
    content = f.read()
    f.close()
else:
    content = sys.stdin.read() # get input from stdin

if (not enableCountWord) and (not enableCountByte) and (not enableCountLine) and (not enableCountChar):
    print("{lineCount} {wordCount} {byteCount} {filepath}".format( lineCount=len(content.split('\n')), wordCount=len(content.split()), byteCount=len(content), filepath=filepath if filepath != None else ""))

elif enableCountLine:
    print("{lineCount} {filepath}".format(lineCount=len(content.split('\n')) if enableCountLine else "", filepath=filepath if filepath != None else ""))
elif enableCountByte:
    print("{byteCount} {filepath}".format(byteCount=len(content), filepath=filepath if filepath != None else ""))
elif enableCountWord:
    print("{wordCount} {filepath}".format(wordCount= len(content.split()), filepath=filepath if filepath != None else ""))
elif enableCountChar:
    print("{charCount} {filepath}".format(charCount= len(content.decode("utf-8", "ignore")), filepath=filepath if filepath != None else ""))