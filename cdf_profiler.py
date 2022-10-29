from netCDF4 import Dataset
import os.path
import sys

def ChangeType(filepath):
    try:
        cdffile = Dataset(filepath, "a")
        cdffile.experiment_type = 'Continuum Mass Spectrum'
        cdffile.close
        print('OK')
    except:
        print('Failed')
        print('Press enter to continue...')
        input()
        return

if __name__ == "__main__":
    print(f"File count: {len(sys.argv)-1}")
    for i, arg in enumerate(sys.argv):
        if i > 0:
            ext = arg.split('.')
            if os.path.isfile(arg) and ext[len(ext)-1] == 'cdf':
                ChangeType(arg)
            else:
                print('File not found or not .cdf : ' + arg)
    print('Press enter to finish...')
    input()

