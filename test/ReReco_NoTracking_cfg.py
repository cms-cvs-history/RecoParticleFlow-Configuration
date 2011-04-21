import FWCore.ParameterSet.Config as cms

process = cms.Process("REPROD")

process.load('RecoParticleFlow.Configuration.ReReco_NoTracking_cff')

# global tag for 4_1_X: 
process.GlobalTag.globaltag = 'GR_R_311_V2::All'

# process.GlobalTag.toGet = cms.VPSet(
#  cms.PSet(record = cms.string("PFCalibrationRcd"),
#           tag = cms.string("PFCalibration"),
#           connect = cms.untracked.string("sqlite_file:/afs/cern.ch/user/p/pjanot/scratch0/CMSSW_3_11_0/src/RecoParticleFlow/Configuration/test/PFCalibration.db")
#           #connect = cms.untracked.string("sqlite_file:PFCalibration.db")
#          )
#)

runOnMC = False 

#process.Timing =cms.Service("Timing")
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# definition of the source

# Flat Pt QCD: 
# process.load('RecoParticleFlow.Configuration.source_QCDFlatPt_cfi')

# user source
process.source = cms.Source(
    'PoolSource',
    fileNames = cms.untracked.vstring('file:pickevents_1_1_JDa.root')
    )

print process.source.fileNames

process.load("RecoParticleFlow.Configuration.output_RECO_cfi")
process.load("RecoParticleFlow.Configuration.output_DISPLAY_cfi")

prefix = 'ReReco_NoTracking_'
process.display.fileName = cms.untracked.string(prefix + process.display.fileName._value)
process.reco.fileName = cms.untracked.string(prefix + process.reco.fileName._value)

if not runOnMC:
    process.reRecoSequence.remove( process.genReReco )

# The complete reprocessing
process.p = cms.Path(
    process.reRecoSequence
    )

# And the output.
process.outpath = cms.EndPath(
    process.display +
    process.reco
    )

# And the logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10


