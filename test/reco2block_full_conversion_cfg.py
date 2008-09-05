import FWCore.ParameterSet.Config as cms

process = cms.Process("BLOCK")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FakeConditions_cff")
process.load("RecoParticleFlow.Configuration.RecoParticleFlow_conversion_cff")




process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5)
)
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('/store/relval/CMSSW_2_1_2/RelValSingleGammaPt35/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_10TeV_v1/0005/5628896F-3574-DD11-96B6-001D09F27003.root')
                            )

process.MessageLogger = cms.Service(
    "MessageLogger",
    conv_rectoblk = cms.untracked.PSet(
    threshold = cms.untracked.string('INFO')),
    destinations = cms.untracked.vstring('conv_rectoblk')
    )

process.Timing =cms.Service("Timing")


process.block = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('conversion_block.root'),
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
                     process.conversionSequence*
                     process.particleFlowRecoConversion
                     )


process.outpath = cms.EndPath(process.block)



