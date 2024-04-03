# c2po
extracts two-photon absorption spectra

modify parameters.inp file

1) initial wavelength
2) final wavelength
3) powers used
4) input file names
5) False if spectral detector is used, True if NDD detector is used

Run macro:
python3 c2po.py

outputs (raw spectra) in the main folder as .png and file data:
spectrum_i.dat
all.dat


NB: files from the microscope are encoded in utf-16le
to convert to utf-8 from terminal 

iconv -f utf-16le -t utf-8 nome_file_input.txt -o nome_file_output.txt

