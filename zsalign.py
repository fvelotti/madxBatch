# -*- coding: utf-8 -*-
"""
Example SPS slow extraction study: downstream zs scan

@author: Linda Stoel
"""
from python.batching import Settings, submit_job

#pos = [40000, 40500, 41000, 41500, 42000, 42500, 43000, 43500, 44000]
pos = [41500]
pc = False
db = True
thin = True

for zsdown in pos:
    name = "scandown_"+str(zsdown)
    name += "_thin" if thin else "_thick"
    name += "_pc" if pc else "_nopc"
    name += "_db" if db else "_nodb"

    settings=Settings(name, studygroup='zsalign', disk='afsproject')

    settings.seed = 0
    settings.flavour = "espresso"
    settings.savetracks = False

    if pc:
        settings.pycollimate=True
        settings.septadb = settings.home+"/input/septa_DB_scan.tfs"
        settings.septadbreplace = {'zsdown': str(zsdown/1E6)}
        settings.elements=['AP.UP.ZS21633_M','AP.DO.ZS21676_M','TPST.21760']
    else:
        settings.pycollimate=False
        settings.elements=['AP.UP.ZS21633','AP.DO.ZS21676','AP.UP.TPST21760']

    settings.myreplace = {"zswiredo = 0.04245;": "zswiredo = "+str(zsdown/1.0E6)+";"}

    settings.nturns=300
    settings.nbatches=10
    settings.nparperbatch=1000
    settings.ffile=1

    if db:
        settings.dynamicbump=True
    else:
        settings.dynamicbump=False

    settings.slices=[-0.0015,-0.0010,-0.0005,0.0,0.0005,0.0010,0.0015]
    if thin:
        settings.slicewidth=0.0

    submit_job(settings)