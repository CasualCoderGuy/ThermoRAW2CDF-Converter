from netCDF4 import Dataset
from pymsfilereader import MSFileReader
import numpy
import time

path = 'E:\\MS\\'
filename = 'ctest'
ext = '.raw'

cutoff_type = 0
cutoff_val = 0
bCentroid = False

rawfile = MSFileReader(path+filename+ext)

if rawfile.InAcquisition():
    print('RAW file is in acquisition.')
if not rawfile.IsThereMSData():
    print('RAW file does not contain MS data.') 
if rawfile.IsNewFile():
    print('RAW file does not any data.')
if rawfile.IsError():
    error = rawfile.GetErrorMessage()
    print('RAW file contains the following error:' + error)
print('Warnings: ' + rawfile.GetWarningMessage())

creation_time = rawfile.GetCreationDate() #!
scan_no = rawfile.GetNumSpectra() #no. of scans
inst_name = rawfile.GetInstName()
inst_id = rawfile.GetInstrumentID()
inst_model = rawfile.GetInstModel()
inst_sw_version = rawfile.GetInstSoftwareVersion()

mass_array = numpy.zeros(1)
intensity_array = numpy.zeros(1)
point_count_array = numpy.zeros(scan_no)
scan_index_array = numpy.zeros(scan_no)
rt_array = numpy.zeros(scan_no)
min_mass_array = numpy.zeros(scan_no)
max_mass_array = numpy.zeros(scan_no)
TIC_array = numpy.zeros(scan_no)
moving_sum = 0
moving_sum2 = 0
"""if cutoff_type:
    for i in range(rawfile.FirstSpectrumNumber, rawfile.LastSpectrumNumber + 1):
        raw_tuple = rawfile.GetMassListFromScanNum(i, "", cutoff_type, cutoff_val, 0, bCentroid, 0)
        mass_array_i = numpy.array(n for n in raw_tuple[0] if n != 0)
        mass_array = numpy.append(mass_array, mass_array_i)
        intensity_array_i = numpy.array(n for n in raw_tuple[1] if n != 0)
        intensity_array = numpy.append(intensity_array, intensity_array_i)
        scan_index_array = numpy.append(scan_index_array, moving_sum)
        point_count_array = numpy.append(point_count_array, mass_array_i.size)
        moving_sum = moving_sum + mass_array_i.size
        rt_array = numpy.append(rt_array, rawfile.RTFromScanNum(i))
        min_mass_array = numpy.append(min_mass_array, rawfile.GetMassRangeFromScanNum(i, 0)[0])
        max_mass_array = numpy.append(max_mass_array, rawfile.GetMassRangeFromScanNum(i, 0)[1])
        TIC_array = numpy.append(TIC_array, rawfile.GetScanHeaderInfoForScanNum(i)['TIC'])
else:"""
for i in range(rawfile.FirstSpectrumNumber, rawfile.LastSpectrumNumber + 1):
        raw_tuple = rawfile.GetMassListFromScanNum(i, "", cutoff_type, cutoff_val, 0, bCentroid, 0)
        mass_array = numpy.append(mass_array, numpy.asfarray(raw_tuple[0][0]))
        intensity_array = numpy.append(intensity_array, numpy.asfarray(raw_tuple[0][1]))
        scan_index_array[i-1] = moving_sum
        point_count_array[i-1] = len(raw_tuple[0][0])
        moving_sum = moving_sum + len(raw_tuple[0][0])
        moving_sum2 = moving_sum2 + len(raw_tuple[0][1])
        rt_array[i-1] = rawfile.RTFromScanNum(i)*60
        min_mass_array[i-1] = rawfile.GetMassRangeFromScanNum(i, 0)[0]
        max_mass_array[i-1] = rawfile.GetMassRangeFromScanNum(i, 0)[1]
        TIC_array[i-1] = rawfile.GetScanHeaderInfoForScanNum(i)['TIC']

rawfile.Close()

mass_array = numpy.delete(mass_array, 0)
intensity_array = numpy.delete(intensity_array, 0)
print(moving_sum)
print(moving_sum2)
print(len(mass_array))
print(len(intensity_array))

cdffile = Dataset(path+filename+".cdf", "w", format="NETCDF3_CLASSIC")

inst_no = 1
error_no = 1
point_no = None

#set dimensions
byte2_string = cdffile.createDimension("_2_byte_string", 2)
byte4_string = cdffile.createDimension("_4_byte_string", 4)
byte8_string = cdffile.createDimension("_8_byte_string", 8)
byte16_string = cdffile.createDimension("_16_byte_string", 16)
byte32_string = cdffile.createDimension("_32_byte_string", 32)
byte64_string = cdffile.createDimension("_64_byte_string", 64)
byte80_string = cdffile.createDimension("_80_byte_string", 80)
byte128_string = cdffile.createDimension("_128_byte_string", 128)
byte255_string = cdffile.createDimension("_255_byte_string", 256)
scanNumDim = cdffile.createDimension("scan_number", scan_no)
instNumDim = cdffile.createDimension("instrument_number", inst_no)
errNumDim = cdffile.createDimension("error_number", error_no)
pointNumDim = cdffile.createDimension("point_number", point_no)

#global attributes
"""cdffile.dataset_completeness = 'C1+C2'
cdffile.ms_template_revision = '1.0.1'
cdffile.netcdf_revision = '2.3.2'
cdffile.languages = 'English' 
cdffile.netcdf_file_date_time_stamp = '20211023210008+0000' #'20211023210008+0000
cdffile.experiment_title = '' #title
cdffile.experiment_date_time_stamp = '20211023210008+0000' #exp time
cdffile.operator_name = 'TSQ' #op
cdffile.source_file_reference = path+filename+ext
cdffile.source_file_format = 'Finnigan'
cdffile.experiment_type = 'Continuum Mass Spectrum' #CONTINUUM/CENTROIDED
cdffile.test_separation_type = '' #HPLC
cdffile.test_ms_inlet = '' #ESI
cdffile.test_ionization_mode = 'Electrospray Ionization' #negative
cdffile.test_ionization_polarity = 'Positive Polarity'
cdffile.test_detector_type = 'Conversion Dynode Electron Multiplier'
cdffile.test_scan_function = 'Mass Scan'
cdffile.test_scan_direction = 'Up'
cdffile.test_scan_law = 'Linear'
cdffile.raw_data_mass_format = 'Double'
cdffile.raw_data_intensity_format = 'Float'"""

cdffile.dataset_completeness        = 'C1'
cdffile.ms_template_revision        = '1.0.1'
cdffile.administrative_comments     = ''
cdffile.dataset_owner               = ''
cdffile.experiment_title            = ''
cdffile.experiment_date_time_stamp  = '20211020133713+0100'
cdffile.netcdf_file_date_time_stamp = '20211023210008+0000'
cdffile.experiment_type             = 'Continuum Mass Spectrum'
cdffile.netcdf_revision             = '2.3.2'
cdffile.operator_name               = 'Balazs'
cdffile.source_file_reference       = 'D:\ADAT\Gergo\CBD\CBD_50ppm.RAW'
cdffile.source_file_date_time_stamp = '20211020133713+0100'
cdffile.source_file_format          = 'Finnigan'
cdffile.languages                   = 'English'
cdffile.external_file_ref_0         = ''
cdffile.instrument_number           = 1
cdffile.sample_prep_comments        = ''
cdffile.sample_comments             = ''
cdffile.test_separation_type        = ''
cdffile.test_ms_inlet               = ''
cdffile.test_ionization_mode        = 'Electrospray Ionization'
cdffile.test_ionization_polarity    = 'Positive Polarity'
cdffile.test_detector_type          = 'Conversion Dynode Electron Multiplier'
cdffile.test_scan_function          = 'Mass Scan'
cdffile.test_scan_direction         = ''
cdffile.test_scan_law               = 'Linear'
cdffile.number_of_scans             = scan_no
cdffile.raw_data_mass_format        = 'Double'
cdffile.raw_data_intensity_format   = 'Float'
cdffile.actual_run_time             = 599.47
cdffile.actual_delay_time           = 0.346
cdffile.global_mass_min             = 100
cdffile.global_mass_max             = 1000
cdffile.calibrated_mass_min         = 0
cdffile.calibrated_mass_max         = 0
cdffile.mass_axis_label             = 'M/Z'
cdffile.intensity_axis_label        = 'Abundance'

# variables
error_log = cdffile.createVariable("error_log","S1",('error_number','_64_byte_string'))
error_log[:] = ''
instrument_name = cdffile.createVariable("instrument_name","S1",('instrument_number', '_32_byte_string'))
instrument_name[:] = ''
instrument_id = cdffile.createVariable("instrument_id","S1",('instrument_number','_32_byte_string'))
instrument_id[:] = ''
instrument_mfr = cdffile.createVariable("instrument_mfr","S1",('instrument_number','_32_byte_string'))
instrument_mfr[:] = ''
instrument_model = cdffile.createVariable("instrument_model","S1",('instrument_number','_32_byte_string'))
instrument_model[:] = ''
instrument_sw_version = cdffile.createVariable("instrument_sw_version","S1",('instrument_number','_32_byte_string'))
instrument_sw_version[:] = ''
instrument_os_version = cdffile.createVariable("instrument_os_version","S1",('instrument_number','_32_byte_string'))
instrument_os_version[:] = ''

scan_index = cdffile.createVariable("scan_index","i4",('scan_number',))
scan_index[:] = scan_index_array
point_count = cdffile.createVariable("point_count","i4",('scan_number',))
point_count[:] = point_count_array
flag_count = cdffile.createVariable("flag_count","i4",('scan_number',))
flag_count[:] = 0
a_d_sampling_rate = cdffile.createVariable("a_d_sampling_rate","f8",('scan_number',))
a_d_sampling_rate[:] = 1000.0
scan_acquisition_time = cdffile.createVariable("scan_acquisition_time","f8",('scan_number',))
scan_acquisition_time[:] = rt_array
scan_duration = cdffile.createVariable("scan_duration","f8",('scan_number',))
scan_duration[:] = 0.0
mass_range_min = cdffile.createVariable("mass_range_min","f8",('scan_number',))
mass_range_min[:] = min_mass_array
mass_range_max = cdffile.createVariable("mass_range_max","f8",('scan_number',))
mass_range_max[:] = max_mass_array
scan_type = cdffile.createVariable("scan_type","i4",('scan_number',))
scan_type[:] = 65540
resolution = cdffile.createVariable("resolution","f8",('scan_number',))
resolution[:] = 0.0
total_intensity = cdffile.createVariable("total_intensity","f8",('scan_number',)) #attr
total_intensity[:] = TIC_array
total_intensity.units = 'Total Counts'


#data
mass_values = cdffile.createVariable("mass_values","f8",('point_number',)) #attr
mass_values[:] = mass_array
mass_values.scale_factor = 1.0
mass_values.units = 'M/Z'

intensity_values = cdffile.createVariable("intensity_values","f4",('point_number',)) #attr
intensity_values[:] = intensity_array
intensity_values.scale_factor = 1.0
intensity_values.units = 'Arbitrary Intensity Units'


#cleanup
cdffile.close