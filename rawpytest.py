from pymsfilereader import MSFileReader

rawfile = MSFileReader("E:\MS\CBD_50ppm.raw")

print('Version', rawfile.Version())
print('GetFileName', rawfile.GetFileName())
print('GetCreatorID', rawfile.GetCreatorID())
print('GetVersionNumber', rawfile.GetVersionNumber())
print('GetCreationDate', rawfile.GetCreationDate())
print('IsError', rawfile.IsError())
print('IsNewFile', rawfile.IsNewFile())
print('IsThereMSData', rawfile.IsThereMSData())
print('HasExpMethod', rawfile.HasExpMethod())
print('InAcquisition', rawfile.InAcquisition())
print('GetErrorCode', rawfile.GetErrorCode())
print('GetErrorMessage', rawfile.GetErrorMessage())
print('GetWarningMessage', rawfile.GetWarningMessage())
print('RefreshViewOfFile', rawfile.RefreshViewOfFile())
print('GetNumberOfControllers', rawfile.GetNumberOfControllers())

print("GetNumberOfControllersOfType('No device')", rawfile.GetNumberOfControllersOfType('No device'))
print("GetNumberOfControllersOfType('MS')", rawfile.GetNumberOfControllersOfType('MS'))
print("GetNumberOfControllersOfType('Analog')", rawfile.GetNumberOfControllersOfType('Analog'))
print("GetNumberOfControllersOfType('A/D card')", rawfile.GetNumberOfControllersOfType('A/D card'))
print("GetNumberOfControllersOfType('PDA')", rawfile.GetNumberOfControllersOfType('PDA'))
print("GetNumberOfControllersOfType('UV')", rawfile.GetNumberOfControllersOfType('UV'))
print("GetControllerType('MS')", rawfile.GetControllerType('MS'))
# print( 'GetControllerType(1)',  rawfile.GetControllerType(1) )

# print( 'GetControllerType(2)',  rawfile.GetControllerType(2) )
# print( 'GetControllerType(3)',  rawfile.GetControllerType(3) )
# print( 'GetControllerType(4)',  rawfile.GetControllerType(4) )
print('GetCurrentController()', rawfile.GetCurrentController())
# print( 'SetCurrentController(4,1)',  rawfile.SetCurrentController(4,1) )

print('GetCurrentController()', rawfile.GetCurrentController())
# print( 'SetCurrentController(0,1)',  rawfile.SetCurrentController(0,1) )

print('GetCurrentController()', rawfile.GetCurrentController())
print('GetExpectedRunTime()', rawfile.GetExpectedRunTime())
print('GetMaxIntegratedIntensity()', rawfile.GetMaxIntegratedIntensity())
print('GetMaxIntensity()', rawfile.GetMaxIntensity())
print('GetInletID()', rawfile.GetInletID())
print('GetErrorFlag()', rawfile.GetErrorFlag())
print('GetFlags()', rawfile.GetFlags())
print('GetAcquisitionFileName()', rawfile.GetAcquisitionFileName())
print('GetOperator()', rawfile.GetOperator())
print('GetComment1()', rawfile.GetComment1())
print('GetComment2()', rawfile.GetComment2())
print('GetFilters()', rawfile.GetFilters())
print('GetMassTolerance()', rawfile.GetMassTolerance())

print('rawfile.SetMassTolerance(userDefined=True, massTolerance=555.0, units=2)',
        rawfile.SetMassTolerance(userDefined=True, massTolerance=555.0, units=2))
print('GetMassTolerance()', rawfile.GetMassTolerance())
print('rawfile.SetMassTolerance(userDefined=False, massTolerance=500.0, units=0)',
        rawfile.SetMassTolerance(userDefined=False, massTolerance=500.0, units=0))
print('GetMassResolution', rawfile.GetMassResolution())
print('GetNumTrailerExtra', rawfile.GetNumTrailerExtra())
print('GetLowMass', rawfile.GetLowMass())
print('GetHighMass', rawfile.GetHighMass())
print('GetStartTime', rawfile.GetStartTime())
print('GetEndTime', rawfile.GetEndTime())
print('GetNumSpectra', rawfile.GetNumSpectra())
print('GetFirstSpectrumNumber', rawfile.GetFirstSpectrumNumber())
print('GetLastSpectrumNumber', rawfile.GetLastSpectrumNumber())
print('GetAcquisitionDate', rawfile.GetAcquisitionDate())
print('GetUniqueCompoundNames', rawfile.GetUniqueCompoundNames())

print('############################################## INSTRUMENT BEGIN')
print('GetInstrumentDescription', rawfile.GetInstrumentDescription())
print('GetInstrumentID', rawfile.GetInstrumentID())
print('GetInstSerialNumber', rawfile.GetInstSerialNumber())
print('GetInstName', rawfile.GetInstName())
print('GetInstModel', rawfile.GetInstModel())
print('GetInstSoftwareVersion', rawfile.GetInstSoftwareVersion())
print('GetInstHardwareVersion', rawfile.GetInstHardwareVersion())
print('GetInstFlags', rawfile.GetInstFlags())
print('GetInstNumChannelLabels', rawfile.GetInstNumChannelLabels())
# print( 'GetInstChannelLabel(0)', rawfile.GetInstChannelLabel(0) )
print('IsQExactive', rawfile.IsQExactive())  # Not implemented in MSFileReader 3.0.29.0
print('############################################## INSTRUMENT END')

scan_number = 1
print('############################################## XCALIBUR INTERFACE BEGIN')
print('GetScanHeaderInfoForScanNum',
        rawfile.GetScanHeaderInfoForScanNum(scan_number))  # "View/Scan header", upper part
print('GetTrailerExtraForScanNum', rawfile.GetTrailerExtraForScanNum(scan_number))  # "View/Scan header", lower part
print('GetNumTuneData', rawfile.GetNumTuneData())
print('GetTuneData(0)', rawfile.GetTuneData(0))  # "View/Report/Tune Method"
print('GetNumInstMethods', rawfile.GetNumInstMethods())
print('GetInstMethodNames', rawfile.GetInstMethodNames())
for i in range(rawfile.GetNumInstMethods()):
    print('-------------------------------------------------------------------------------')
    print(rawfile.GetInstMethod(i))  # "View/Report/Instrument Method"
    print('-------------------------------------------------------------------------------')
print('rawfile.ExtractInstMethodFromRaw', rawfile.ExtractInstMethodFromRaw(rawfile.filename + '.meth'))

# # # # # # "View/Report/Sample Information" BEGIN
print('GetVialNumber', rawfile.GetVialNumber())
print('GetInjectionVolume', rawfile.GetInjectionVolume())
print('GetInjectionAmountUnits', rawfile.GetInjectionAmountUnits())
print('GetSampleVolume', rawfile.GetSampleVolume())
print('GetSampleVolumeUnits', rawfile.GetSampleVolumeUnits())
print('GetSampleWeight', rawfile.GetSampleWeight())
print('GetSampleAmountUnits', rawfile.GetSampleAmountUnits())
print('GetSeqRowNumber', rawfile.GetSeqRowNumber())
print('GetSeqRowSampleType', rawfile.GetSeqRowSampleType())
print('GetSeqRowDataPath', rawfile.GetSeqRowDataPath())
print('GetSeqRowRawFileName', rawfile.GetSeqRowRawFileName())
print('GetSeqRowSampleName', rawfile.GetSeqRowSampleName())
print('GetSeqRowSampleID', rawfile.GetSeqRowSampleID())
print('GetSeqRowComment', rawfile.GetSeqRowComment())
print('GetSeqRowLevelName', rawfile.GetSeqRowLevelName())
print('GetSeqRowUserText', rawfile.GetSeqRowUserText(index=0))
print('GetSeqRowUserText', rawfile.GetSeqRowUserText(index=1))
print('GetSeqRowUserText', rawfile.GetSeqRowUserText(index=2))
print('GetSeqRowUserText', rawfile.GetSeqRowUserText(index=3))
print('GetSeqRowUserText', rawfile.GetSeqRowUserText(index=4))
print('GetSeqRowInstrumentMethod', rawfile.GetSeqRowInstrumentMethod())
print('GetSeqRowProcessingMethod', rawfile.GetSeqRowProcessingMethod())
print('GetSeqRowCalibrationFile', rawfile.GetSeqRowCalibrationFile())
print('GetSeqRowVial', rawfile.GetSeqRowVial())
print('GetSeqRowInjectionVolume', rawfile.GetSeqRowInjectionVolume())
print('GetSeqRowSampleWeight', rawfile.GetSeqRowSampleWeight())
print('GetSeqRowSampleVolume', rawfile.GetSeqRowSampleVolume())
print('GetSeqRowISTDAmount', rawfile.GetSeqRowISTDAmount())
print('GetSeqRowDilutionFactor', rawfile.GetSeqRowDilutionFactor())
print('GetSeqRowUserLabel', rawfile.GetSeqRowUserLabel(index=0))
print('GetSeqRowUserLabel', rawfile.GetSeqRowUserLabel(index=1))
print('GetSeqRowUserLabel', rawfile.GetSeqRowUserLabel(index=2))
print('GetSeqRowUserLabel', rawfile.GetSeqRowUserLabel(index=3))
print('GetSeqRowUserLabel', rawfile.GetSeqRowUserLabel(index=4))
print('GetSeqRowUserTextEx', rawfile.GetSeqRowUserTextEx(index=0))
print('GetSeqRowUserTextEx', rawfile.GetSeqRowUserTextEx(index=1))
print('GetSeqRowUserTextEx', rawfile.GetSeqRowUserTextEx(index=2))
print('GetSeqRowUserTextEx', rawfile.GetSeqRowUserTextEx(index=3))
print('GetSeqRowUserTextEx', rawfile.GetSeqRowUserTextEx(index=4))
print('GetSeqRowBarcode', rawfile.GetSeqRowBarcode())
print('GetSeqRowBarcodeStatus', rawfile.GetSeqRowBarcodeStatus())
# # # # # # # "View/Report/Sample Information" END
print('GetNumStatusLog', rawfile.GetNumStatusLog())
print('GetStatusLogForScanNum')  # "View/Report/Status Log"
print(rawfile.GetStatusLogForScanNum(scan_number))
print('GetStatusLogForPos(position=0)', rawfile.GetStatusLogForPos(position=0))
print('GetStatusLogForPos(position=1)', rawfile.GetStatusLogForPos(position=1))
print('GetStatusLogPlottableIndex()', rawfile.GetStatusLogPlottableIndex())

print('GetNumErrorLog', rawfile.GetNumErrorLog())
for i in range(rawfile.GetNumErrorLog()):
    print('GetErrorLogItem', i, rawfile.GetErrorLogItem(i))  # "View/Report/Error Log"
print('############################################## XCALIBUR INTERFACE END')

print('GetMassListFromScanNum', rawfile.GetMassListFromScanNum(scan_number))
print('GetMassListRangeFromScanNum', rawfile.GetMassListRangeFromScanNum(scan_number))
print('GetSegmentedMassListFromScanNum', rawfile.GetSegmentedMassListFromScanNum(scan_number))
print('GetAverageMassList', rawfile.GetAverageMassList(scan_number, scan_number + 10))
print('GetAveragedMassSpectrum', rawfile.GetAveragedMassSpectrum([scan_number, scan_number + 5, scan_number + 10]))
print('GetSummedMassSpectrum', rawfile.GetSummedMassSpectrum([scan_number, scan_number + 5, scan_number + 10]))
print('GetLabelData', rawfile.GetLabelData(scan_number))
print('GetAveragedLabelData', rawfile.GetAveragedLabelData([scan_number, scan_number + 5, scan_number + 10]))
print('GetAllMSOrderData', rawfile.GetAllMSOrderData(scan_number))
print('GetChroData', rawfile.GetChroData(startTime=rawfile.StartTime,
                                            endTime=rawfile.EndTime,
                                            massRange1="{}-{}".format(rawfile.LowMass, rawfile.HighMass),
                                            scanFilter="Full ms "))
# print( 'GetChroByCompoundName', rawfile.GetChroByCompoundName(["methyltestosterone"]) )

# print( 'GetMassPrecisionEstimate', rawfile.GetMassPrecisionEstimate(scan_number) )

print('GetFullMSOrderPrecursorDataFromScanNum(scan_number,0)',
        rawfile.GetFullMSOrderPrecursorDataFromScanNum(scan_number, 0))
print('GetFullMSOrderPrecursorDataFromScanNum(scan_number,1)',
        rawfile.GetFullMSOrderPrecursorDataFromScanNum(scan_number, 1))

print('GetPrecursorInfoFromScanNum(scan_number,1)', rawfile.GetPrecursorInfoFromScanNum(scan_number))

with open('test.tsv', 'wt') as f:
    print('\t'.join(map(str, ('scan_number',
                                'RetentionTime',
                                'scan_number',
                                'GetFilterForScanNum(i)',
                                'GetMSOrderForScanNum(i)',
                                'GetNumberOfMSOrdersFromScanNum(i)',
                                'GetScanTypeForScanNum(i)',
                                'GetDetectorTypeForScanNum(i)',
                                'GetMassAnalyzerTypeForScanNum(i)',
                                'GetActivationTypeForScanNum(i,MSOrder=2)',
                                'IsProfileScanForScanNum(i)',
                                'IsCentroidScanForScanNum(i)',
                                'GetIsolationWidthForScanNum(i,MSOrder=1)',
                                'GetCollisionEnergyForScanNum(i,MSOrder=1)',
                                'GetPrecursorInfoFromScanNum(i)',
                                'GetMassCalibrationValueFromScanNum(i,massCalibrationIndex=0)',
                                'GetScanEventForScanNum(i)',
                                'GetSegmentAndEventForScanNum(i)',
                                'GetCycleNumberFromScanNumber(i)',
                                'GetAValueFromScanNum(i)',
                                'GetBValueFromScanNum(i)',
                                'GetKValueFromScanNum(i)',
                                'GetRValueFromScanNum(i)',
                                'GetVValueFromScanNum(i)',
                                'GetMSXMultiplexValueFromScanNum(i)',
                                'GetCompoundNameFromScanNum(i)',
                                'GetNumberOfMassRangesFromScanNum(i)',
                                'GetMassRangeFromScanNum(i,0)',
                                'GetMassRangeFromScanNum(i,1)',
                                'GetNumberOfSourceFragmentsFromScanNum(i)',
                                'GetSourceFragmentValueFromScanNum(i,0)',
                                'GetNumberOfSourceFragmentationMassRangesFromScanNum(i)'
                                ))), file=f)

    for i in range(rawfile.FirstSpectrumNumber, rawfile.LastSpectrumNumber + 1):
        print('\t'.join(map(str, (i,
                                    rawfile.RTFromScanNum(i),
                                    rawfile.ScanNumFromRT(rawfile.RTFromScanNum(i)),
                                    rawfile.GetFilterForScanNum(i),
                                    rawfile.GetMSOrderForScanNum(i),
                                    rawfile.GetNumberOfMSOrdersFromScanNum(i),
                                    rawfile.GetScanTypeForScanNum(i),
                                    rawfile.GetDetectorTypeForScanNum(i),
                                    rawfile.GetMassAnalyzerTypeForScanNum(i),
                                    rawfile.GetActivationTypeForScanNum(i, MSOrder=2),
                                    rawfile.IsProfileScanForScanNum(i),
                                    rawfile.IsCentroidScanForScanNum(i),
                                    rawfile.GetIsolationWidthForScanNum(i, MSOrder=1),
                                    rawfile.GetCollisionEnergyForScanNum(i, MSOrder=1),
                                    rawfile.GetPrecursorInfoFromScanNum(i),
                                    rawfile.GetMassCalibrationValueFromScanNum(i, massCalibrationIndex=0),
                                    rawfile.GetScanEventForScanNum(i),
                                    rawfile.GetSegmentAndEventForScanNum(i),
                                    rawfile.GetCycleNumberFromScanNumber(i),
                                    rawfile.GetAValueFromScanNum(i),
                                    rawfile.GetBValueFromScanNum(i),
                                    rawfile.GetKValueFromScanNum(i),
                                    rawfile.GetRValueFromScanNum(i),
                                    rawfile.GetVValueFromScanNum(i),
                                    rawfile.GetMSXMultiplexValueFromScanNum(i),
                                    rawfile.GetCompoundNameFromScanNum(i),
                                    rawfile.GetNumberOfMassRangesFromScanNum(i),
                                    rawfile.GetMassRangeFromScanNum(i, 0),
                                    rawfile.GetMassRangeFromScanNum(i, 1),
                                    rawfile.GetNumberOfSourceFragmentsFromScanNum(i),
                                    rawfile.GetSourceFragmentValueFromScanNum(i, 0),
                                    rawfile.GetNumberOfSourceFragmentationMassRangesFromScanNum(i)
                                    ))), file=f)

rawfile.Close()