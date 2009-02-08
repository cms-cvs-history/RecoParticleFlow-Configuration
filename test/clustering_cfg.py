import FWCore.ParameterSet.Config as cms

# runs only clustering.
# PFRecHits should be in the input file

process = cms.Process("PFC")

process.source = cms.Source("PoolSource", 
                            fileNames = cms.untracked.vstring("file:display.root") )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2000)
)

#fastsim
#process.load("FastSimulation.Configuration.RandomServiceInitialization_cff")
#process.load("FastSimulation.Configuration.CommonInputs_cff")
#process.GlobalTag.globaltag = "IDEAL_30X::All"
#process.load("FastSimulation.Configuration.FamosSequences_cff")

# Parametrized magnetic field (new mapping, 4.0 and 3.8T)
#process.load("Configuration.StandardSequences.MagneticField_40T_cff")
#process.load("Configuration.StandardSequences.MagneticField_38T_cff")

process.load("RecoParticleFlow.PFClusterProducer.particleFlowCluster_cff")


process.particleFlowClusterECAL.verbose = True

process.p1 = cms.Path(
    process.particleFlowClusterECAL+
    process.particleFlowClusterHCAL+
    process.particleFlowClusterPS 
    )



process.load("FastSimulation.Configuration.EventContent_cff")
process.reco = cms.OutputModule("PoolOutputModule",
    process.RECOSIMEventContent,
    fileName = cms.untracked.string('reco.root')
)

process.load("RecoParticleFlow.Configuration.Display_EventContent_cff")
process.display = cms.OutputModule("PoolOutputModule",
    process.DisplayEventContent,
    fileName = cms.untracked.string('clustering.root')
)

process.outpath = cms.EndPath( process.reco )

#
