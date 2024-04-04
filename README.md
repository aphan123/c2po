# c2po
extracts two-photon absorption spectra

**Requirements**:
- python3 (tested on Python 3.8.10)
- numpy
- matplotlib


Modify ``parameters.inp`` file as follows:

1) initial wavelength
2) final wavelength
3) power values 
4) input file names (same number and order as number of power values in previous row)
5) type of detector (``False``: spectral detector, ``True``: NDD detector)

Run script:
``python3 c2po.py``

outputs (raw spectra) in the main folder as .png and file data:
``spectrum_i.dat``
``all.dat``

