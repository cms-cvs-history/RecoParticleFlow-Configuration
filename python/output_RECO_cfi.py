import FWCore.ParameterSet.Config as cms


from Configuration.EventContent.EventContent_cff import RECOSIMEventContent

reco = cms.OutputModule(
    "PoolOutputModule",
    RECOSIMEventContent,
    #outputCommands = cms.untracked.vstring('keep *'),
    #process.RECOSIMEventContent,
    fileName = cms.untracked.string('reco.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p'))
    )
