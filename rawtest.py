from pymsfilereader import MSFileReader

rawfile = MSFileReader("E:\MS\ctest.raw")

scanno = 10
print('RTFromScanNum', rawfile.RTFromScanNum(scanno))
print('GetMSOrderForScanNum', rawfile.GetMSOrderForScanNum(scanno))
print('IsProfileScanForScanNum', rawfile.IsProfileScanForScanNum(scanno))
print('IsCentroidScanForScanNum', rawfile.IsCentroidScanForScanNum(scanno))
print('GetScanEventForScanNum', rawfile.GetScanEventForScanNum(scanno))
print('GetNumberOfMassRangesFromScanNum', rawfile.GetNumberOfMassRangesFromScanNum(scanno))
print('GetMassRangeFromScanNum', rawfile.GetMassRangeFromScanNum(scanno, 0))
print('GetMassRangeFromScanNum', rawfile.GetMassRangeFromScanNum(scanno, 1))
print('GetScanHeaderInfoForScanNum', rawfile.GetScanHeaderInfoForScanNum(scanno))
raw_tuple = rawfile.GetMassListFromScanNum(1, "", 0, 0, 0, True, 0)
a, b = raw_tuple
print(a[1])
#print('GetMass', rawfile.GetMassListFromScanNum(scanno, "", 0, 0, 0, True, 0))

rawfile.Close()
