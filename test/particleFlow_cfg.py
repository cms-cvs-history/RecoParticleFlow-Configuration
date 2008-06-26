import FWCore.ParameterSet.Config as cms


process = cms.Process("PFLOW")

process.source = cms.Source("PoolSource", 
                            fileNames = cms.untracked.vstring("file:display.root") )


process.dump = cms.OutputModule("EventContentAnalyzer")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)


#fastsim
#process.load("FastSimulation.Configuration.FamosSequences_cff")
process.load("RecoParticleFlow.Configuration.RecoParticleFlow_cff")

process.load("RecoParticleFlow.PFBlockProducer.particleFlowSimParticle_cff")

process.p1 = cms.Path(
    process.particleFlowBlock+
    process.particleFlow
    )




# process.outpath = cms.EndPath(process.aod + process.display)

#
