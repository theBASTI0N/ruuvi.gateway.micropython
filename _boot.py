import gc
import uos
from flashbdev import bdev
import createruuvi

try:
    if bdev:
        uos.mount(bdev, "/")
except OSError:
    import inisetup

    vfs = inisetup.setup()


try:
    uos.stat('/main.py')
except OSError:
    with open("/main.py", "w") as f:
        f.write("""\
import ruuvigw""")

createruuvi.create()

gc.collect()
