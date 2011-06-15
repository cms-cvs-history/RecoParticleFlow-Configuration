# The following comments couldn't be translated into the new config version:

#        "keep recoPFClusters_*_*_*",
#        "keep recoPFBlocks_*_*_*",	

import FWCore.ParameterSet.Config as cms

# Full Event content 
RecoParticleFlowFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
    'drop CaloTowersSorted_towerMakerPF_*_*',
    #'keep recoPFRecHits_*_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*',
    'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
    'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*',
    'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
    #'keep recoPFClusters_*_*_*',
    'keep recoPFClusters_particleFlowClusterECAL_*_*',
    'keep recoPFClusters_particleFlowClusterHCAL_*_*',
    'keep recoPFClusters_particleFlowClusterHFEM_*_*',
    'keep recoPFClusters_particleFlowClusterHFHAD_*_*',
    'keep recoPFClusters_particleFlowClusterPS_*_*',
    #'keep recoPFBlocks_*_*_*',
    'keep recoPFBlocks_particleFlowBlock_*_*',
    #'keep recoPFCandidates_*_*_*',
    'keep recoPFCandidates_particleFlow_*_*',
    #'keep recoPFDisplacedVertexs_*_*_*',
    'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
    'keep *_pfElectronTranslator_*_*',
    'keep *_pfPhotonTranslator_*_*',
    'keep *_trackerDrivenElectronSeeds_preid_*')
    )
# RECO content
RecoParticleFlowRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
    'drop CaloTowersSorted_towerMakerPF_*_*', 
    #'keep recoPFRecHits_*_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*',
    'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
    'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*',
    'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
    #'keep recoPFClusters_*_*_*',
    'keep recoPFClusters_particleFlowClusterECAL_*_*',
    'keep recoPFClusters_particleFlowClusterHCAL_*_*',
    #'keep recoPFClusters_particleFlowClusterHFEM_*_*',
    #'keep recoPFClusters_particleFlowClusterHFHAD_*_*',
    'keep recoPFClusters_particleFlowClusterPS_*_*',
    #'keep recoPFBlocks_*_*_*',
    'keep recoPFBlocks_particleFlowBlock_*_*',
    #'keep recoPFCandidates_*_*_*',
    'keep recoPFCandidates_particleFlow_*_*',
    #'keep recoPFDisplacedVertexs_*_*_*',
    'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
    'keep *_pfElectronTranslator_*_*',
    'keep *_pfPhotonTranslator_*_*',
    'keep *_trackerDrivenElectronSeeds_preid_*')
)    
    
# AOD content
RecoParticleFlowAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
    'drop CaloTowersSorted_towerMakerPF_*_*',
    'drop *_pfElectronTranslator_*_*',
    #'keep recoPFRecHits_*_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*',
    'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*',
    'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
    'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*',
    'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
    #'keep recoPFCandidates_*_*_*',
    'keep recoPFCandidates_particleFlow_*_*',
    'keep recoCaloClusters_pfElectronTranslator_*_*',
    'keep recoPreshowerClusters_pfElectronTranslator_*_*',
    'keep recoSuperClusters_pfElectronTranslator_*_*',
    'keep recoCaloClusters_pfPhotonTranslator_*_*',
    'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
    'keep recoSuperClusters_pfPhotonTranslator_*_*',
    'keep recoPhotons_pfPhotonTranslator_*_*',
    'keep recoPhotonCores_pfPhotonTranslator_*_*')
)
