import FWCore.ParameterSet.Config as cms

process = cms.Process("BLOCK")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'MC_31X_V1::All'
#process.load("Configuration.StandardSequences.FakeConditions_cff")

process.Timing =cms.Service("Timing")
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(30)
)
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('file:qcd.root')
)

process.MessageLogger = cms.Service("MessageLogger",
    rectoblk = cms.untracked.PSet(
        threshold = cms.untracked.string('INFO')
    ),
    destinations = cms.untracked.vstring('rectoblk')
)

process.dump = cms.EDAnalyzer("EventContentAnalyzer")
process.block = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('blocks_full.root'),
    outputCommands = cms.untracked.vstring(
            'drop *',
            'keep recoPFRecHits_*_*_*',
            'keep recoPFClusters_*_*_*',
            'keep recoPFRecTracks_*_*_BLOCK',
            'keep recoPFBlocks_particleFlowBlock_*_*',
            'keep recoPFCandidates_particleFlow_*_*',
            'keep recoCandidatesOwned_*_*_*',
            'keep recoPFSimParticles_*_*_*',
            'keep *_generalTracks_*_BLOCK',
            'keep *_electronGsfTracks_*_BLOCK',
            'keep *_pfTrackElec_*_BLOCK',
            'keep recoCaloJets_*_*_*',
            'keep CaloTowersSorted_*_*_*',
            'keep edmHepMCProduct_*_*_*'
)
)


process.p = cms.Path(process.siPixelRecHits*
                     process.siStripMatchedRecHits*
                     process.ckftracks*
                     process.electronGsfTracking*
                     process.particleFlowTrack
#                     *process.particleFlowBlock
#                     *process.particleFlow
                     )
process.outpath = cms.EndPath(process.block)



