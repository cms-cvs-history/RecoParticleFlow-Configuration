#!/usr/bin/python

from optparse import OptionParser
import sys,os, pprint
import castortools

def sourceFileList( files ):
    print '''
import FWCore.ParameterSet.Config as cms

source = cms.Source(
"PoolSource",
'''
    print "fileNames = cms.untracked.vstring("
    for file in files:
        fileLine = "'file:%s'," % os.path.abspath(file)
        print fileLine
        print ")"
        print ")"    


parser = OptionParser()
parser.usage = "%prog <dir> <regexp> : format a set of root files matching a regexp in a directory, as an input to the PoolSource."

(options,args) = parser.parse_args()

if len(args) != 2:
    parser.print_help()
    sys.exit(1)

dir = args[0]
regexp = args[1]

castor = castortools.isCastorDir( dir )

files = castortools.matchingFiles( dir, regexp,
                                    protocol=True, castor=castor)

print '''
import FWCore.ParameterSet.Config as cms

source = cms.Source(
    "PoolSource",
'''
print "\tfileNames = cms.untracked.vstring("
for file in files:
    fileLine = "\t\t%s'," % file
    print fileLine
print "\t)"
print ")"