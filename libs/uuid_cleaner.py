#!python3
import re
import sys
import os

uuid_pattern = re.compile(r"[ \t]*\(*.tstamp[^\)]*\)[ \t]*", re.IGNORECASE)

if __name__ == '__main__':

    for fn in sys.argv[1:]:
        if os.path.isfile(fn):
            bak_fn = fn + '.bak'
            try: 
                os.rename(fn, bak_fn)
                if os.path.isfile(fn):
                    print ('Failed to rename ', fn)
                    continue
                outp = open(fn, "w")
                with open(bak_fn, 'r') as inp:
                    for line in inp:
                        outp.write(re.sub(uuid_pattern, "", line))
                inp.close()
                outp.close()
            except Exception as e:
                print (e.__class__.__name__, ' error.')


