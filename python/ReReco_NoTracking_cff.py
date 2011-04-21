import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Reconstruction_cff import *
from Configuration.StandardSequences.MagneticField_38T_cff import * 
# from Configuration.StandardSequences.MagneticField_4T_cff import *
from Configuration.StandardSequences.Geometry_cff import *
from Configuration.StandardSequences.FrontierConditions_GlobalTag_cff import *

dump = cms.EDAnalyzer("EventContentAnalyzer")

# modify reconstruction sequence
#hbhereflag = hbhereco.clone()
#hbhereflag.hbheInput = 'hbhereco'
#towerMakerPF.hbheInput = 'hbhereflag'
#particleFlowRecHitHCAL.hcalRecHitsHBHE = cms.InputTag("hbhereflag")

# Local re-reco: Produce tracker rechits, pf rechits and pf clusters
localReReco = cms.Sequence(particleFlowCluster)


# Particle Flow re-processing
pfReReco = cms.Sequence(
    particleFlowReco+
    recoPFJets+
    recoPFMET+
    PFTau
    )
                                
# Gen Info re-processing
from PhysicsTools.HepMCCandAlgos.genParticles_cfi import * 
from RecoJets.Configuration.GenJetParticles_cff import *
from RecoJets.Configuration.RecoGenJets_cff import *
from RecoMET.Configuration.GenMETParticles_cff import *
from RecoMET.Configuration.RecoGenMET_cff import *
from RecoParticleFlow.PFProducer.particleFlowSimParticle_cff import *
from RecoParticleFlow.Configuration.HepMCCopy_cfi import *

genReReco = cms.Sequence(
    generator+
    genParticles+
    genJetParticles+
    recoGenJets+
    genMETParticles+
    recoGenMET+
    particleFlowSimParticle
    )

# The complete reprocessing
reRecoSequence = cms.Sequence(
    localReReco+
    pfReReco + 
    genReReco
    #+pfChargedHadronAnalyzer
    )
