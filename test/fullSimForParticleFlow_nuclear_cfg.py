import FWCore.ParameterSet.Config as cms


process = cms.Process("PROD")


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

#generation
process.load("RecoParticleFlow.Configuration.source_singleTau_cfi")
process.load("Configuration.StandardSequences.SimulationRandomNumberGeneratorSeeds_cff")

#simulation
process.load("Configuration.StandardSequences.Simulation_cff")
process.load("Configuration.StandardSequences.MixingNoPileUp_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.FakeConditions_cff")
process.load("Configuration.StandardSequences.RawToDigi_cff")
process.load("Configuration.StandardSequences.DigiToRaw_cff")
#reconstruction
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("RecoParticleFlow.Configuration.RecoParticleFlow_nuclear_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
#Trigger
process.load("Configuration.StandardSequences.L1Emulator_cff")


process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring('FullSim'),
                                    FullSim = cms.untracked.PSet(
    threshold = cms.untracked.string('INFO')
    )
                                    )

process.p1 = cms.Path(
    process.simulation+
    process.L1Emulator+
    process.DigiToRaw+
    process.RawToDigi+
    process.localreco+
    process.globalreco+
    process.egammareco+
    process.particleFlowRecoNuclear
    )






process.load("RecoParticleFlow.Configuration.Display_EventContent_cff")
process.block = cms.OutputModule("PoolOutputModule",
                          process.DisplayEventContent,         
    fileName = cms.untracked.string('blocks_full_nuclear.root'),
)

process.outpath = cms.EndPath(

   process.block
)

#
