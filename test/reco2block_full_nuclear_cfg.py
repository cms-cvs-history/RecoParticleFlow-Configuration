import FWCore.ParameterSet.Config as cms

process = cms.Process("BLOCK")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FakeConditions_cff")
process.load("RecoParticleFlow.Configuration.RecoParticleFlow_nuclear_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('/store/relval/CMSSW_2_1_4/RelValSinglePiPt10/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V6_v1/0004/625F8CDD-1A6C-DD11-8826-001617DBD316.root')
)

process.MessageLogger = cms.Service(
    "MessageLogger",
    nucl_rectoblk = cms.untracked.PSet(
    threshold = cms.untracked.string('INFO')),
    destinations = cms.untracked.vstring('nucl_rectoblk')
    )

process.Timing =cms.Service("Timing")



process.dump = cms.EDAnalyzer("EventContentAnalyzer")
process.block = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('nuclear_block.root'),
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

process.p = cms.Path(process.siPixelRecHits*
                     process.siStripMatchedRecHits*
                     process.ckftracks*
                     process.electronSequence*
                     process.nuclearRemainingHits*
                     process.particleFlowTrackWithNuclear*
                     process.particleFlowBlock
                     )



process.outpath = cms.EndPath(process.block)



