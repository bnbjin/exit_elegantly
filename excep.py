# globally catch exception SystemExit/KeyboardInterrupt to clean the scene

import sys
import traceback

try:
    sys.exit(-1)

except (SystemExit, KeyboardInterrupt) as e:
    traceback.print_exc()
