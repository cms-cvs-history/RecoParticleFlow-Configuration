import FWCore.ParameterSet.Config as cms


process = cms.Process("PROD")


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

#generation
process.load("RecoParticleFlow.Configuration.source_singleTau_cfi")
#process.load("FastSimulation.Configuration.SimpleJet_cfi")

#fastsim
process.load("FastSimulation.Configuration.RandomServiceInitialization_cff")
process.load("FastSimulation.Configuration.CommonInputs_cff")
process.load("FastSimulation.Configuration.FamosSequences_cff")
process.GlobalTag.globaltag = "IDEAL_30X::All"

process.famosSimHits.SimulateCalorimetry = True
#process.famosSimHits.Calorimetry.UnfoldedMode = True 
process.famosSimHits.SimulateTracking = True
process.famosPileUp.PileUpSimulator.averageNumber = 0.0

process.famosSimHits.VertexGenerator.BetaStar = 0.00001
process.famosSimHits.VertexGenerator.SigmaZ = 0.00001

# Parametrized magnetic field (new mapping, 4.0 and 3.8T)
process.load("Configuration.StandardSequences.MagneticField_40T_cff")
#process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.VolumeBasedMagneticFieldESProducer.useParametrizedTrackerField = True

#process.famosSimHits.MaterialEffects.PairProduction = False
#process.famosSimHits.MaterialEffects.Bremsstrahlung = False
#process.famosSimHits.MaterialEffects.EnergyLoss = False
#process.famosSimHits.MaterialEffects.MultipleScattering = False
#process.famosSimHits.MaterialEffects.NuclearInteraction = False

process.load("RecoParticleFlow.PFBlockProducer.particleFlowSimParticle_cff")

process.dump = cms.OutputModule("EventContentAnalyzer")

process.p1 = cms.Path(
    process.famosWithTracksAndCaloHits+
    process.famosWithElectrons+
    process.caloTowersPFRec+
    process.particleFlowCluster+
    process.elecpreid+
    process.fsGsfElCandidates+
    process.fsgsfPFtracks+
    process.pfTrackElec+
    #process.caloJetMetGen+
    #process.particleFlowSimParticle+
    process.dump
    )


process.load("FastSimulation.Configuration.EventContent_cff")
process.aod = cms.OutputModule("PoolOutputModule",
    process.AODEventContent,
    fileName = cms.untracked.string('aod.root')
)

process.load("RecoParticleFlow.Configuration.Display_EventContent_cff")
process.display = cms.OutputModule("PoolOutputModule",
    process.DisplayEventContent,
    fileName = cms.untracked.string('display.root')
)

process.outpath = cms.EndPath(process.aod + process.display)

#
