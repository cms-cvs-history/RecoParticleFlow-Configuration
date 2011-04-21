import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.Configuration.ReDisplay_EventContent_NoTracking_cff import DisplayEventContent

display = cms.OutputModule("PoolOutputModule",
    DisplayEventContent,
    #outputCommands = cms.untracked.vstring('keep *'),
    #process.RECOSIMEventContent,
    fileName = cms.untracked.string('display.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p'))
)
