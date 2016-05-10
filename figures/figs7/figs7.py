import numpy as np
import matplotlib.pyplot as plt

TC = np.arange(-20, 51, 1)
TK = TC + 273.15
T0 = 298.15

ftclmcn = np.exp(308.56*(1/71.02-1/(TK-227.13)))
ftcentury = 0.56+0.46*np.arctan(0.097*(TC-15.7))
ftrothc = 47.9/(1+np.exp(106.0/(TC+18.3)))

ftq102 = 1.8**((TK-298.15)/10.0)
ftq103 = 2.0**((TK-298.15)/10.0)
ftq104 = 2.5**((TK-298.15)/10.0)

fta1 = np.exp(-50.0e3/8.314 *(1.0/TK - 1.0/298.15))
fta2 = np.exp(-60.0e3/8.314 *(1.0/TK - 1.0/298.15))
fta3 = np.exp(-70.0e3/8.314 *(1.0/TK - 1.0/298.15))

ftr1 = (TK - 250.0) * (TK - 250.0) / (T0 - 250.0) / (T0 - 250.0)
ftr2 = (TK - 260.0) * (TK - 260.0) / (T0 - 260.0) / (T0 - 260.0)
ftr3 = (TK - 270.0) * (TK - 270.0) / (T0 - 270.0) / (T0 - 270.0)

lx = 0.05
ly = 0.9
ymax = 2.0

fig = plt.figure()
plt.subplots_adjust(hspace=0.05, wspace=0.05, left=0.08, right=0.95, top=0.95, bottom=0.1)

ax1 = fig.add_subplot(221)
ax1.plot(TC, ftclmcn, 'b-', TC, ftcentury, 'r-.', linewidth=2)
ax1.plot([-2, -2], [0, ymax], 'k:')
ax1.plot([4, 4], [0, ymax], 'k:')
ax1.plot([8, 8], [0, ymax], 'k:')
ax1.set_ylim([0.0, ymax])
ax1.set_ylabel('f(T)')
lg1 = ax1.legend(('CLM-CN', 'CENTURY'), loc=6)
lg1.draw_frame(False)
lgt = lg1.get_texts()
plt.setp(lgt, fontsize='medium')
plt.text(lx, ly, '(a)', transform=ax1.transAxes)
#ax1.set_xlabel('$^\circ$C')

ax2 = fig.add_subplot(222)
ax2.plot(TC, ftclmcn, 'b-', TC, ftq102, 'r-.', TC, ftq103, 'g--', TC, ftq104, 'm:', linewidth=2)
ax2.plot([-2, -2], [0, ymax], 'k:')
ax2.plot([4, 4], [0, ymax], 'k:')
ax2.plot([8, 8], [0, ymax], 'k:')
ax2.set_ylim([0.0, ymax])
lg2 = ax2.legend(('CLM-CN', '$\mathrm{Q_{10}}$ = 1.8', '$\mathrm{Q_{10}}$ = 2.0', '$\mathrm{Q_{10}}$ = 2.5'), loc=6)
lg2.draw_frame(False)
lgt = lg2.get_texts()
plt.setp(lgt, fontsize='medium')
plt.text(lx, ly, '(b)', transform=ax2.transAxes)
#ax2.set_xlabel('$^\circ$C')

ax3 = fig.add_subplot(223)
ax3.plot(TC, ftclmcn, 'b-', TC, ftr1, 'r-.', TC, ftr2, 'g--', TC[17:71], ftr3[17:71], 'm:', linewidth=2)
ax3.plot([-2, -2], [0, ymax], 'k:')
ax3.plot([4, 4], [0, ymax], 'k:')
ax3.plot([8, 8], [0, ymax], 'k:')
ax3.set_ylabel('f(T)')
ax3.set_ylim([0.0, ymax])
lg3 = ax3.legend(('CLM-CN', '$\mathrm{T_{m}\ =\ 250\ ^{\circ}K}$', '$\mathrm{T_{m}\ =\ 260\ ^{\circ}K}$', '$\mathrm{T_{m}\ =\ 270\ ^{\circ}K}$'), loc=6)
lg3.draw_frame(False)
lgt = lg3.get_texts()
plt.setp(lgt, fontsize='medium')
plt.text(lx, ly, '(c)', transform=ax3.transAxes)
ax3.set_xlabel('Temperature ($^\circ$C)')
ax3.set_xticks([-20, -10, 0, 10, 20, 30, 40])
ax3.set_yticks([0, 0.5, 1, 1.5])

ax4 = fig.add_subplot(224)
ax4.plot(TC, ftclmcn, 'b-', TC, fta1, 'r-.', TC, fta2, 'g--', TC, fta3, 'm:', linewidth=2)
#ax4.plot(TC, ftclmcn, 'b-', TC[7:71], ftr1[7:71], 'r-.', TC[17:61], ftr2[17:61], 'g--', TC[27:71], ftr3[27:71], 'm:', linewidth=2)
ax4.plot([-2, -2], [0, ymax], 'k:')
ax4.plot([4, 4], [0, ymax], 'k:')
ax4.plot([8, 8], [0, ymax], 'k:')
ax4.set_xlabel('Temperature ($^\circ$C)')
ax4.set_ylim([0.0, ymax])
lg4= ax4.legend(('CLM-CN', '$\mathrm{E_{a}\ =\ 50\ kJ\ mol^{-1}}$', '$\mathrm{E_{a}\ =\ 60\ kJ\ mol^{-1}}$', '$\mathrm{E_{a}\ =\ 70\ kJ\ mol^{-1}}$'), loc=6)
lg4.draw_frame(False)
lgt = lg4.get_texts()
plt.setp(lgt, fontsize='medium')
plt.text(lx, ly, '(d)', transform=ax4.transAxes)

xticklabels = ax1.get_xticklabels() + ax2.get_xticklabels() 
yticklabels = ax2.get_yticklabels() + ax4.get_yticklabels() 
plt.setp(xticklabels, visible=False)
plt.setp(yticklabels, visible=False)

fig.set_size_inches(8.5, 6)
plt.savefig('figs7.pdf')
plt.savefig('figs7.png')
plt.show()
