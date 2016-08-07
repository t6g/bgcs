from pylab import *

center = loadtxt('../../data/lcp_center.txt')

co2b  = np.loadtxt('../../simulations/labile1/co2.txt', skiprows=2)
co4b  = np.loadtxt('../../simulations/labile1/co4.txt', skiprows=2)
co8b  = np.loadtxt('../../simulations/labile1/co8.txt', skiprows=2)

co2   = np.loadtxt('../../simulations/bio1/co2.txt', skiprows=2)
co4   = np.loadtxt('../../simulations/bio1/co4.txt', skiprows=2)
co8   = np.loadtxt('../../simulations/bio1/co8.txt', skiprows=2)

co2a  = np.loadtxt('../../simulations/bio2/co2.txt', skiprows=2)
co4a  = np.loadtxt('../../simulations/bio2/co4.txt', skiprows=2)
co8a  = np.loadtxt('../../simulations/bio2/co8.txt', skiprows=2)

lx = 0.85
ly = 0.85

fig = figure()

ax1=subplot(3, 2, 1);
ax1.plot(co2[:, 0], co2[:, 3], 'b-', co4[:, 0], co4[:, 3], 'g-', co8[:, 0], co8[:, 3], 'r-', \
         co2a[:, 0], co2a[:, 3], 'b--', co4a[:, 0], co4a[:, 3], 'g--', co8a[:, 0], co8a[:, 3], 'r--', \
         co2b[:, 0], co2b[:, 3], 'b-.', co4b[:, 0], co4b[:, 3], 'g-.', co8b[:, 0], co8b[:, 3], 'r-.', \
         center[:, 0], center[:, 1], 'b+', center[:, 0], center[:, 2], 'bx', center[:, 0], center[:, 3], 'b.', \
         center[:, 0], center[:, 4], 'g+', center[:, 0], center[:, 5], 'gx', center[:, 0], center[:, 6], 'g.', \
         center[:, 0], center[:, 7], 'r+', center[:, 0], center[:, 8], 'rx', center[:, 0], center[:, 9], 'r.')
plt.xlim([-5, 70])
plt.ylim([-3, 30])
plt.ylabel('CO$_2$(%)')
plt.yticks([0, 10, 20, 30])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(a)', transform=ax1.transAxes)

ax2=subplot(3, 2, 2);
ax2.plot(co2[:, 0], co2[:, 4], 'b-', co4[:, 0], co4[:, 4], 'g-', co8[:, 0], co8[:, 4], 'r-', \
         co2a[:, 0], co2a[:, 4], 'b--', co4a[:, 0], co4a[:, 4], 'g--', co8a[:, 0], co8a[:, 4], 'r--', \
         co2b[:, 0], co2b[:, 4], 'b-.', co4b[:, 0], co4b[:, 4], 'g-.', co8b[:, 0], co8b[:, 4], 'r-.', \
         center[:, 0], center[:, 19], 'bx', center[:, 0], center[:, 20], 'b+', center[:, 0], center[:, 21], 'b.', \
         center[:, 0], center[:, 22], 'gx', center[:, 0], center[:, 23], 'g+', center[:, 0], center[:, 24], 'g.', \
         center[:, 0], center[:, 25], 'rx', center[:, 0], center[:, 26], 'r+', center[:, 0], center[:, 27], 'r.')
plt.xlim([-5, 70])
plt.ylim([-2, 20])
plt.text(lx, ly, '(b)', transform=ax2.transAxes)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.ylabel('CH$_4$(%)')

index=6
ax3=subplot(3, 2, 3);
ax3.plot(co8b[:, 0], co8b[:, index], 'r-.', co8[:, 0], co8[:, index], 'r-', co8a[:, 0], co8a[:, index], 'r--', \
         co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b--', co4a[:, 0], co4a[:, index], 'g--', co8a[:, 0], co8a[:, index], 'r--', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.')
plt.xlim([-5, 70])
plt.ylim([-2, 25])
plt.text(lx, ly, '(c)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.ylabel('CO$_2$ (mM)')
lgd = plt.legend(('$f_{\mathrm{bio}}$ = 10$^{-6}$', '$f_{\mathrm{bio}}$ = 10$^{-5}$', '$f_{\mathrm{bio}}$ = 2 $\\times$ 10$^{-5}$'),loc=2)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='medium') 

index = 9 
ax4=subplot(3, 2, 4);
ot3 = [0, 30, 60];
ac2co = [6.37, 14.71, 13.08]
ac4co = [6.37, 17.93,  6.67]
ac8co = [6.37, 21.19,  5.35]
ax4.plot(co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b--', co4a[:, 0], co4a[:, index], 'g--', co8a[:, 0], co8a[:, index], 'r--', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.', \
         ot3, ac2co, 'b+', ot3, ac4co, 'gx', ot3, ac8co, 'r.')
plt.xlim([-5, 70])
plt.ylim([-2, 30])
plt.text(lx, ly, '(d)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.ylabel('Ac (mM)')

ot1 = [0, 15, 30, 60];
index = 13
ax5=subplot(3, 2, 5);
fe2co = [0.789,10.541, 10.198, 12.734]
fe4co = [0.789, 6.601, 12.568, 15.624]
fe8co = [0.789, 9.283, 16.091, 16.601]
ax5.plot(co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b--', co4a[:, 0], co4a[:, index], 'g--', co8a[:, 0], co8a[:, index], 'r--', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.', \
         ot1, fe2co, 'b+', ot1, fe4co, 'gx', ot1, fe8co, 'r.')
plt.xlim([-5, 70])
plt.ylim([0, 30])
plt.text(lx, ly, '(e)', transform=ax5.transAxes)
#plt.setp(ax5.get_xticklabels(), visible=False)
#plt.setp(ax5.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')
plt.ylabel('Fe(II) (mM)')

index = 1
ymax = 7 
ot1 = [0, 15, 30, 60];
ax6=subplot(3, 2, 6);
ph2co = [5.02, 5.02, 5.38, 5.71]
ph4co = [5.02, 5.09, 5.62, 5.32]
ph8co = [5.02, 5.09, 5.31, 5.42]
ax6.plot(co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b--', co4a[:, 0], co4a[:, index], 'g--', co8a[:, 0], co8a[:, index], 'r--', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.', \
         ot1, ph2co, 'b+', ot1, ph4co, 'gx', ot1, ph8co, 'r.')
plt.xlim([-5, 70])
plt.ylim([4, ymax])
plt.yticks([4, 5, 6, 7])
plt.xticks([0, 20, 40, 60])
plt.text(lx, ly, '(f)', transform=ax6.transAxes)
plt.xlabel('Time (d)')
plt.ylabel('pH')

plt.subplots_adjust(left=0.08, right=0.95, top=0.95, bottom=0.08, hspace=0.1, wspace=0.2)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(8, 8)
savefig('fig5.png')
savefig('fig5.pdf')
#show()
