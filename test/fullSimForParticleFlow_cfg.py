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
    process.particleFlowReco
    )




process.load("Configuration.EventContent.EventContent_cff")
process.aod = cms.OutputModule("PoolOutputModule",
    process.AODEventContent,
    fileName = cms.untracked.string('aod.root')
)

process.reco = cms.OutputModule("PoolOutputModule",
    process.RECOEventContent,
    fileName = cms.untracked.string('reco.root')
)



process.block = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('blocks_full.root'),
    outputCommands = cms.untracked.vstring(
            'drop *', 
            'keep recoPFRecHits_*_*_*',
            'keep recoPFClusters_*_*_*',
            'keep recoPFRecTracks_*_*_*',
	    'keep recoPFBlocks_particleFlowBlock_*_*',
	    'keep recoPFCandidates_particleFlow_*_*',
	    'keep recoCandidatesOwned_*_*_*',
            'keep recoPFSimParticles_*_*_*',
            'keep recoTracks_*_*_*',
	    'keep recoCaloJets_*_*_*',
	    'keep CaloTowersSorted_*_*_*',
	    'keep edmHepMCProduct_*_*_*'	 
)
)

process.outpath = cms.EndPath(
   process.aod+
   process.reco+
   process.block
)

#
