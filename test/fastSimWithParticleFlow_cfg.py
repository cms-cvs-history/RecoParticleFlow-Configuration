import FWCore.ParameterSet.Config as cms


process = cms.Process("PROD")


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2000)
)

#generation
process.load("RecoParticleFlow.Configuration.source_singleTau_cfi")

#fastsim
process.load("FastSimulation.Configuration.RandomServiceInitialization_cff")
process.load("FastSimulation.Configuration.CommonInputsFake_cff")
process.load("FastSimulation.Configuration.FamosSequences_cff")

process.famosSimHits.SimulateCalorimetry = True
process.famosSimHits.SimulateTracking = True
process.famosPileUp.PileUpSimulator.averageNumber = 0.0

process.famosSimHits.VertexGenerator.BetaStar = 0.00001
process.famosSimHits.VertexGenerator.SigmaZ = 0.00001

# Parametrized magnetic field (new mapping, 4.0 and 3.8T)
process.load("Configuration.StandardSequences.MagneticField_40T_cff")
#process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.VolumeBasedMagneticFieldESProducer.useParametrizedTrackerField = True

# process.famosSimHits.MaterialEffects.PairProduction = false
# process.famosSimHits.MaterialEffects.Bremsstrahlung = false
# process.famosSimHits.MaterialEffects.EnergyLoss = false
# process.famosSimHits.MaterialEffects.MultipleScattering = false
# process.famosSimHits.MaterialEffects.NuclearInteraction = false

process.load("RecoParticleFlow.PFBlockProducer.particleFlowSimParticle_cff")


process.p1 = cms.Path(
    process.famosWithCaloTowersAndParticleFlow +
    process.particleFlowSimParticle
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
