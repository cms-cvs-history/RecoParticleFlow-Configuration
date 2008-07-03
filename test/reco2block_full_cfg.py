import FWCore.ParameterSet.Config as cms

process = cms.Process("BLOCK")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FakeConditions_cff")


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('file:../../../reco.root')
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


process.p = cms.Path(process.ckftracks*process.caloTowersPFRec*process.particleFlowCluster*process.particleFlowTrack*process.particleFlowBlock)
process.outpath = cms.EndPath(process.block)



