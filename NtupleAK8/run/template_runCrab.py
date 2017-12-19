import os
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = '_requestName_'
config.General.workArea = '_workArea_'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '_psetName_'
config.JobType.allowUndistributedCMSSW = True
#config.JobType.sendExternalFolder = True

config.Data.inputDataset = '_inputDataset_'
config.JobType.pyCfgParams = _pyCfgParams_
config.JobType.pyCfgParams += ['inputDataset=%s' % config.Data.inputDataset]
# config.JobType.inputFiles = []

#config.Data.inputDBS = 'phys03'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = _unitsPerJob_
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.ignoreLocality = True


# uncomment this part to use CRAB to submit to FNAL_LPC
# config.Data.ignoreLocality = True

config.Site.whitelist = ['T2_CH_CERN', 'T2_HU_Budapest', 'T2_DE_RWTH']
#config.Site.ignoreGlobalBlacklist = True
#config.Site.blacklist = ['T3_US_UMiss', ]

#config.Site.storageSite = '_storageSite_'
config.Site.storageSite = "T2_DE_RWTH"

config.User.voGroup = 'dcms'
config.User.voRole = 'NULL'

