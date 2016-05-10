import numpy as np
import matplotlib.pyplot as plt

pH   = np.arange(3.0, 10.1, 0.1)
pHmin = 4.0
pHmax =10.0
pHopt = 7.0
fpH1 = (pH - pHmin) * (pH - pHmax) / ((pH - pHmin) * (pH - pHmax) - (pH - pHopt) * (pH - pHopt))
fpH2 = 10**(-0.2235*pH*pH + 2.7727*pH - 8.6)
fpH3 = np.zeros_like(pH)

i    = 0
for iph in pH:
  if iph < 4.0:
    fpH3[i] = 0.0
  elif iph < 7.0:
    fpH3[i] = 1.02 / (1.0 + 1.0e6 * np.exp(-2.5*iph))
  else:
    fpH3[i] = 1.02 / (1.0 + 1.0e6 * np.exp(-2.5*(14.0 - iph)))
  i = i + 1
    
fig = plt.figure()

plt.plot(pH, fpH2, 'b-', pH, fpH1, 'r-.', pH, fpH3, 'g--', linewidth=2)
plt.plot([4.5, 4.5], [0, 1.2], 'k:') #, [5, 5], [0, 1.2], 'k:')
plt.plot([5.5, 5.5], [0, 1.2], 'k:') #, [6, 6], [0, 1.2], 'k:')
plt.plot([6.5, 6.5], [0, 1.2], 'k:') #, [7, 7], [0, 1.2], 'k:')
#plt.grid()
lg = plt.legend(('CLM4Me', 'TEM', 'DLEM'), loc=1)
lg.draw_frame(False)
lgt = lg.get_texts()
plt.setp(lgt, fontsize='small')
plt.xlabel('pH')
plt.ylabel('f(pH)')
plt.ylim([0, 1.2])

plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.15)

fig.set_size_inches(6, 4)
plt.savefig('fig6.pdf')
plt.savefig('fig6.png')
plt.show()
