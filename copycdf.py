from netCDF4 import Dataset
import numpy
import time

path = 'E:\\MS\\'
filename = 'copytest'
sname = 'source'
ext = '.raw'

source = Dataset(path+sname+".cdf")
cdffile = Dataset(path+filename+".cdf", "w", "NETCDF3_CLASSIC")

"""#cdffile.dimensions['scan_number'].size = source.dimensions['scan_number'].size
cdffile.variables['scan_index'][:] = source.variables['scan_index'][:]
cdffile.variables['point_count'][:] = source.variables['point_count'][:]
cdffile.variables['scan_acquisition_time'][:] = source.variables['scan_acquisition_time'][:]
cdffile.variables['mass_range_min'][:] = source.variables['mass_range_min'][:]
cdffile.variables['mass_range_max'][:] = source.variables['mass_range_max'][:]
cdffile.variables['total_intensity'][:] = source.variables['total_intensity'][:]
cdffile.variables['mass_values'][:] = source.variables['mass_values'][:]
cdffile.variables['intensity_values'][:] = source.variables['intensity_values'][:]"""

scan_no = source.dimensions['scan_number'].size
scan_index_array = source.variables['scan_index'][:]
point_count_array = source.variables['point_count'][:]
rt_array = source.variables['scan_acquisition_time'][:]
min_mass_array = source.variables['mass_range_min'][:]
max_mass_array = source.variables['mass_range_max'][:]
TIC_array = source.variables['total_intensity'][:]
mass_array = source.variables['mass_values'][:]
intensity_array = source.variables['intensity_values'][:]
flag_count_array = source.variables['flag_count'][:]
a_d_sampling_rate_array = source.variables['a_d_sampling_rate'][:]
scan_duration_array = source.variables['scan_duration'][:]
scan_type_array = source.variables['scan_type'][:]
resolution_array = source.variables['resolution'][:]
error_log_array = source.variables['error_log'][:]
instrument_name_array = source.variables['instrument_name'][:]
instrument_id_array = source.variables['instrument_id'][:]
instrument_mfr_array = source.variables['instrument_mfr'][:]
instrument_model_array = source.variables['instrument_model'][:]
instrument_sw_version_array = source.variables['instrument_sw_version'][:]
instrument_os_version_array = source.variables['instrument_os_version'][:]

inst_no = 1
error_no = 1
point_no = 0

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
"""cdffile.dataset_completeness        = 'C1+C2'
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
cdffile.intensity_axis_label        = 'Abundance'"""

cdffile.dataset_completeness        = source.dataset_completeness
cdffile.ms_template_revision        = source.ms_template_revision
cdffile.administrative_comments     = source.administrative_comments
cdffile.dataset_owner               = source.dataset_owner
cdffile.experiment_title            = source.experiment_title
cdffile.experiment_date_time_stamp  = source.experiment_date_time_stamp
cdffile.netcdf_file_date_time_stamp = source.netcdf_file_date_time_stamp
cdffile.experiment_type             = source.experiment_type
cdffile.netcdf_revision             = source.netcdf_revision
cdffile.operator_name               = source.operator_name
cdffile.source_file_reference       = source.source_file_reference
cdffile.source_file_date_time_stamp = source.source_file_date_time_stamp
cdffile.source_file_format          = source.source_file_format
cdffile.languages                   = source.languages
cdffile.external_file_ref_0         = source.external_file_ref_0
cdffile.instrument_number           = source.instrument_number
cdffile.sample_prep_comments        = source.sample_prep_comments
cdffile.sample_comments             = source.sample_comments
cdffile.test_separation_type        = source.test_separation_type
cdffile.test_ms_inlet               = source.test_ms_inlet
cdffile.test_ionization_mode        = source.test_ionization_mode
cdffile.test_ionization_polarity    = source.test_ionization_polarity
cdffile.test_detector_type          = source.test_detector_type
cdffile.test_scan_function          = source.test_scan_function
cdffile.test_scan_direction         = source.test_scan_direction
cdffile.test_scan_law               = source.test_scan_law
cdffile.number_of_scans             = source.number_of_scans
cdffile.raw_data_mass_format        = source.raw_data_mass_format
cdffile.raw_data_intensity_format   = 'Float'#source.raw_data_intensity_format
cdffile.actual_run_time             = source.actual_run_time
cdffile.actual_delay_time           = source.actual_delay_time
cdffile.global_mass_min             = source.global_mass_min
cdffile.global_mass_max             = source.global_mass_max
cdffile.calibrated_mass_min         = source.calibrated_mass_min
cdffile.calibrated_mass_max         = source.calibrated_mass_max
cdffile.mass_axis_label             = source.mass_axis_label
cdffile.intensity_axis_label        = source.intensity_axis_label

# variables
error_log = cdffile.createVariable("error_log","S1",('error_number','_64_byte_string'))
error_log[:] = error_log_array
instrument_name = cdffile.createVariable("instrument_name","S1",('instrument_number', '_32_byte_string'))
instrument_name[:] = instrument_name_array
instrument_id = cdffile.createVariable("instrument_id","S1",('instrument_number','_32_byte_string'))
instrument_id[:] = instrument_id_array
instrument_mfr = cdffile.createVariable("instrument_mfr","S1",('instrument_number','_32_byte_string'))
instrument_mfr[:] = instrument_mfr_array
instrument_model = cdffile.createVariable("instrument_model","S1",('instrument_number','_32_byte_string'))
instrument_model[:] = instrument_model_array
instrument_sw_version = cdffile.createVariable("instrument_sw_version","S1",('instrument_number','_32_byte_string'))
instrument_sw_version[:] = instrument_sw_version_array
instrument_os_version = cdffile.createVariable("instrument_os_version","S1",('instrument_number','_32_byte_string'))
instrument_os_version[:] = instrument_os_version_array

scan_index = cdffile.createVariable("scan_index","i4",('scan_number',))
scan_index[:] = scan_index_array
point_count = cdffile.createVariable("point_count","i4",('scan_number',))
point_count[:] = point_count_array
flag_count = cdffile.createVariable("flag_count","i4",('scan_number',))
flag_count[:] = flag_count_array
a_d_sampling_rate = cdffile.createVariable("a_d_sampling_rate","f8",('scan_number',))
a_d_sampling_rate[:] = a_d_sampling_rate_array
scan_acquisition_time = cdffile.createVariable("scan_acquisition_time","f8",('scan_number',))
scan_acquisition_time[:] = rt_array
scan_duration = cdffile.createVariable("scan_duration","f8",('scan_number',))
scan_duration[:] = scan_duration_array
mass_range_min = cdffile.createVariable("mass_range_min","f8",('scan_number',))
mass_range_min[:] = min_mass_array
mass_range_max = cdffile.createVariable("mass_range_max","f8",('scan_number',))
mass_range_max[:] = max_mass_array
scan_type = cdffile.createVariable("scan_type","i4",('scan_number',))
scan_type[:] = scan_type_array
resolution = cdffile.createVariable("resolution","f8",('scan_number',))
resolution[:] = resolution_array
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