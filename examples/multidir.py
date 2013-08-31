__author__ = 'Christoph Statz, christoph.statz <at> tu-dresden.de'

import numpy
from pyvisfile.silo import SiloFile, DB_CLOBBER

f = SiloFile("dir.silo", mode=DB_CLOBBER)

f.mk_dir("AAA")
f.set_dir("AAA")

f.mk_dir("BBB")
f.set_dir("BBB")
print f.get_dir()

f.set_dir("../")
print f.get_dir()

f.set_dir("../")
print f.get_dir()

f.set_dir("../")
print f.get_dir()

f.close()
