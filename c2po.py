#Convert 2 PhOton absorption spectra

import numpy as np
import matplotlib.pyplot as plt

#Reading paramters
with open('parameters.inp', 'r') as file:
    wlstart = float(file.readline().split()[0])
    wlend =  float(file.readline().split()[0])
    pots = file.readline().split()
    filenames = file.readline().split()
    nddflag = file.readline().split()[0]

pots = np.array([float(i) for i in pots])
print(filenames)
nddflag = eval(nddflag)
if nddflag:
    print(f'NDD detector is being used')
    column = int(1)
else:
    print(f'Spectral detector is being used')
    column = int(4)

#Generating wavelength grid
wlstep = 10.
print(f'A {wlstep} nm step is used.')
npoints = int(np.abs(wlstart-wlend)/wlstep + 1)
wl = np.linspace(wlstart, wlend, npoints)
#print(wl)
print(f'A grid of {npoints} points is generated.')

## Correction curve
corr = np.genfromtxt('important/Excitation_Correction_optimized.txt')
# filtering values of the correction curve
filter = [i>=wlend and i<=wlstart for i in corr[:,0]]
#print(filter)
corr = corr[filter,:]
plt.title(f'Correction curve')
plt.plot(corr[:,0],corr[:,1],'k')
plt.xlim(min(corr[:,0]),max(corr[:,0]))
plt.xlabel(f'Wavelength (nm)')
plt.savefig(f'correction_curve.png')
plt.close()

## Power curve
potenze = np.genfromtxt('important/Potenze_laser.txt')
# filtering values of the power curve
filter = [i>=wlend and i<=wlstart for i in potenze[:,0]]
potenze = potenze[filter,:]
plt.title(f'Power')
plt.plot(potenze[:,0],potenze[:,1],'k')
plt.xlim(min(potenze[:,0]),max(potenze[:,0]))
plt.xlabel(f'Wavelength (nm)')
plt.ylabel(f'Power (a.u.)')
plt.savefig(f'power.png')
plt.close()

## Extracting data
datalist = []
for i,pot in enumerate(pots):
    filename = filenames[i]
    print(filename)
    #print(filename)
    with open(filename, 'r') as fff:
        flag = 0
        j = 0
        print(filename)
        for line in fff:
            #print(line[1])

            #print(line)
            if flag == 1: 
                #print(line)
                data = float(line.split()[column])
                #print(j,data)
                datalist.append(data)
                j += 1
            if line[0]=='W':
                #print(line)
                flag = 1
            else:
                flag = 0

#print(datalist)
#plt.plot(datalist)
#plt.show()
#print(len(datalist))
datalist = np.transpose(np.reshape(datalist,(len(pots),len(wl))))

# saving spectra in one file
np.savetxt('all.dat', np.column_stack((wl,datalist)))

# saving spectra in separated files
for i in range(1,len(pots)+1):
    with open(f'spectrum_{i}.out', 'w') as file:
        for j,w in enumerate(wl):
            print(f'{w}\t\t{datalist[j,i-1]}',file=file)

# plotting spectra
plt.plot(wl,datalist[:,0], 'k', label=f'p={pots[0]}')
plt.plot(wl,datalist[:,1], 'r', label=f'p={pots[1]}')
plt.plot(wl,datalist[:,2], 'b', label=f'p={pots[2]}')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.legend()
plt.savefig(f'raw_spectra.png')
plt.close()

# plotting corrected spectra
colors = ['k','r','b']
for i, pot in enumerate(pots):
    plt.plot(wl,datalist[:,i]/(potenze[:,1]*pot/100)**2*corr[::-1,1],label=f'p={pots[i]}',c=colors[i])


plt.xlabel(f'Wavelength (nm)')
plt.ylabel(f'Normalized intensity')
plt.xlim(wl[-1], wl[0])
plt.legend()
plt.savefig(f'corrected_spectra.png')
plt.close()








