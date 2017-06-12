# -*- coding: utf-8 -*-
"""
Nominal SPS slow extraction with and without scattering

@author: Linda Stoel
"""
from python.batching import Settings, submit_job

bl = [True, False]

# Simulations with sweep
for pc, db, fast in [(True,False,True)]:#[(x,y,z) for x in bl for y in bl for z in bl]:
    if pc and not fast:
        break

    name = "pc" if pc else "nopc"
    name += "_db" if db else "_nodb"
    name += "_fast" if fast else ""

    settings=Settings(name, studygroup="nominal", disk='afsproject')
    settings.seed = 0
    settings.pycollimate = pc
    settings.dynamicbump = db

    if fast:
        settings.nturns = 50000
        settings.ffile = 500
        if pc and db:
            settings.flavour = "tomorrow"
    else:
        settings.nturns = 204565
        settings.ffile = 2045
        #if pc and db:
        #    settings.flavour = "testmatch"

    if pc:
        settings.elements = ['AP.UP.ZS21633_M','AP.DO.ZS21676_M','TPST.21760']
        settings.nbatches = 100
        settings.nparperbatch = 1000
    else:
        settings.elements = ['AP.UP.ZS21633','AP.DO.ZS21676','TPST.21760']
        settings.nbatches = 500
        settings.nparperbatch = 200

    submit_job(settings)

# Simulations of momentum slices
'''for pc, db, wide in [(x,y,z) for x in bl for y in bl for z in bl]:
    name = "sliced"
    name += "_wide" if fast else ""
    name += "_pc" if pc else "_nopc"
    name += "_db" if db else "_nodb"

    settings=Settings(name, studygroup="nominal", disk='afsproject')
    settings.seed = 0
    settings.pycollimate = pc
    settings.dynamicbump = db
    settings.slices = [-0.0015,0.0,0.0015]

    settings.nturns = 300
    settings.ffile = 1
    settings.nbatches = 10
    settings.nparperbatch = 100

    if wide:
        settings.slicewidth = 2.5E-4
    else:
        settings.slicewidth = 0.0

    if pc:
        settings.elements = ['AP.UP.ZS21633_M','AP.DO.ZS21676_M','TPST.21760']
    else:
        settings.elements = ['AP.UP.ZS21633','AP.DO.ZS21676','TPST.21760']

    submit_job(settings)'''
