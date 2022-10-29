from netCDF4 import Dataset
import time

testno = '1'
cdffile = Dataset("E:\\MS\\test"+testno+".cdf", "w", format="NETCDF3_CLASSIC")

scan_no = 100  #no. of scans
inst_no = 1 #??
error_no = 1 #??
point_no = None #or scan_no*datapoints

#set dimensions
byte2_string = cdffile.createDimension("_2_byte_string", 2)
byte4_string = cdffile.createDimension("_4_byte_string", 4)
byte8_string = cdffile.createDimension("_8_byte_string", 8)
byte16_string = cdffile.createDimension("_16_byte_string", 16)
byte32_string = cdffile.createDimension("_32_byte_string", 32)
byte64_string = cdffile.createDimension("_64_byte_string", 64)
byte80_string = cdffile.createDimension("_80_byte_string", 80)
byte128_string = cdffile.createDimension("_128_byte_string", 128)
byte255_string = cdffile.createDimension("_255_byte_string", 255)
scanNumDim = cdffile.createDimension("scan_number", scan_no)
instNumDim = cdffile.createDimension("instrument_number", inst_no)
errNumDim = cdffile.createDimension("error_number", error_no)
pointNumDim = cdffile.createDimension("point_number", point_no)

#global attributes
cdffile.dataset_completeness = 'C1+C2'
cdffile.ms_template_revision = '1.0.1'
cdffile.netcdf_revision = '2.3.2'
cdffile.languages = 'English' 
cdffile.netcdf_file_date_time_stamp = 'C1+C2' #'20211023210008+0000
cdffile.experiment_title = '' #title
cdffile.experiment_date_time_stamp = '' #exp time
cdffile.operator_name = '' #op
cdffile.source_file_reference = '' #filepath
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
cdffile.raw_data_mass_format = 'Float'
cdffile.raw_data_intensity_format = 'Float'

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
scan_index[:] = 0
point_count = cdffile.createVariable("point_count","i4",('scan_number',))
point_count[:] = 0
flag_count = cdffile.createVariable("flag_count","i4",('scan_number',))
flag_count[:] = 0
a_d_sampling_rate = cdffile.createVariable("a_d_sampling_rate","f4",('scan_number',))
a_d_sampling_rate[:] = 0.0
scan_acquisition_time = cdffile.createVariable("scan_acquisition_time","f4",('scan_number',))
scan_acquisition_time[:] = 0.0
scan_duration = cdffile.createVariable("scan_duration","f4",('scan_number',))
scan_duration[:] = 0.0
mass_range_min = cdffile.createVariable("mass_range_min","f4",('scan_number',))
mass_range_min[:] = 0.0
mass_range_max = cdffile.createVariable("mass_range_max","f4",('scan_number',))
mass_range_max[:] = 0.0
scan_type = cdffile.createVariable("scan_type","i4",('scan_number',))
scan_type[:] = 0
resolution = cdffile.createVariable("resolution","f4",('scan_number',))
mass_range_min[:] = 0.0
total_intensity = cdffile.createVariable("total_intensity","f4",('scan_number',)) #attr
total_intensity[:] = 0.0


#data
mass_values = cdffile.createVariable("mass_values","f4",('point_number',)) #attr
mass_values[:] = [1000.,850.,700.,500.,300.,250.,200.,150.,100.,50.]

intensity_values = cdffile.createVariable("intensity_values","f4",('point_number',)) #attr
intensity_values[:] = [1000.,850.,700.,500.,300.,250.,200.,150.,100.,50.]

#cleanup
cdffile.close
"""
    error_log            
           Size:       64x1
           Dimensions: _64_byte_string,error_number
           Datatype:   char
    instrument_name      
           Size:       32x1
           Dimensions: _32_byte_string,instrument_number
           Datatype:   char
    instrument_id        
           Size:       32x1
           Dimensions: _32_byte_string,instrument_number
           Datatype:   char
    instrument_mfr       
           Size:       32x1
           Dimensions: _32_byte_string,instrument_number
           Datatype:   char
    instrument_model     
           Size:       32x1
           Dimensions: _32_byte_string,instrument_number
           Datatype:   char
    instrument_sw_version
           Size:       32x1
           Dimensions: _32_byte_string,instrument_number
           Datatype:   char
    instrument_os_version
           Size:       32x1
           Dimensions: _32_byte_string,instrument_number
           Datatype:   char
    scan_index           
           Size:       1677x1
           Dimensions: scan_number
           Datatype:   int32
    point_count          
           Size:       1677x1
           Dimensions: scan_number
           Datatype:   int32
    flag_count           
           Size:       1677x1
           Dimensions: scan_number
           Datatype:   int32
    a_d_sampling_rate    
           Size:       1677x1
           Dimensions: scan_number
           Datatype:   double
    scan_acquisition_time
           Size:       1677x1
           Dimensions: scan_number
           Datatype:   double
    scan_duration        
           Size:       1677x1
           Dimensions: scan_number
           Datatype:   double
    mass_range_min       
           Size:       1677x1
           Dimensions: scan_number
           Datatype:   double
    mass_range_max       
           Size:       1677x1
           Dimensions: scan_number
           Datatype:   double
    scan_type            
           Size:       1677x1
           Dimensions: scan_number
           Datatype:   int32
    resolution           
           Size:       1677x1
           Dimensions: scan_number
           Datatype:   double
    total_intensity      
           Size:       1677x1
           Dimensions: scan_number
           Datatype:   double
           Attributes:
                       units = 'Total Counts'
    mass_values          
           Size:       21561189x1
           Dimensions: point_number
           Datatype:   double
           Attributes:
                       scale_factor = 1
                       units        = 'M/Z'
    intensity_values     
           Size:       21561189x1
           Dimensions: point_number
           Datatype:   int32
           Attributes:
                       scale_factor = 1
                       units        = 'Arbitrary Intensity Units'
                       """