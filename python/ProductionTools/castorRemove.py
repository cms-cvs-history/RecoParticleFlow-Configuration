#!/usr/bin/env python

from optparse import OptionParser
import sys,os, re, pprint
import castortools

parser = OptionParser()
parser.usage = "%prog <castor dir> <regexp pattern>: place all files matching regexp in a castor directory in a Trash."
parser.add_option("-n", "--negate", action="store_true",
                  dest="negate",
                  help="do not proceed",
                  default=False)

(options,args) = parser.parse_args()

if len(args)!=2:
    parser.print_help()
    sys.exit(1)

castorDir = args[0]
regexp = args[1]

files = castortools.matchingFiles( castorDir, regexp )

if options.negate:
    print 'NOT removing ',  
    pprint.pprint(files)
else:
    print 'Removing ',  
    pprint.pprint(files)
    trash = castortools.createSubDir( castorDir, 'Trash')
    castortools.move( trash, files )