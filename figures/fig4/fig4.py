from pylab import *

center = loadtxt('../../data/lcp_center.txt')
trough = loadtxt('../../data/lcp_trough.txt')
ridge  = loadtxt('../../data/lcp_ridge.txt')

co2  = np.loadtxt('../../simulations/labile1/co2.txt', skiprows=2)
co4  = np.loadtxt('../../simulations/labile1/co4.txt', skiprows=2)
co8  = np.loadtxt('../../simulations/labile1/co8.txt', skiprows=2)
ro2  = np.loadtxt('../../simulations/labile1/ro2.txt', skiprows=2)
ro4  = np.loadtxt('../../simulations/labile1/ro4.txt', skiprows=2)
ro8  = np.loadtxt('../../simulations/labile1/ro8.txt', skiprows=2)
to2  = np.loadtxt('../../simulations/labile1/to2.txt', skiprows=2)
to4  = np.loadtxt('../../simulations/labile1/to4.txt', skiprows=2)
to8  = np.loadtxt('../../simulations/labile1/to8.txt', skiprows=2)

co2a  = np.loadtxt('../../simulations/labile0/co2.txt', skiprows=2)
co4a  = np.loadtxt('../../simulations/labile0/co4.txt', skiprows=2)
co8a  = np.loadtxt('../../simulations/labile0/co8.txt', skiprows=2)
ro2a  = np.loadtxt('../../simulations/labile0/ro2.txt', skiprows=2)
ro4a  = np.loadtxt('../../simulations/labile0/ro4.txt', skiprows=2)
ro8a  = np.loadtxt('../../simulations/labile0/ro8.txt', skiprows=2)
to2a  = np.loadtxt('../../simulations/labile0/to2.txt', skiprows=2)
to4a  = np.loadtxt('../../simulations/labile0/to4.txt', skiprows=2)
to8a  = np.loadtxt('../../simulations/labile0/to8.txt', skiprows=2)

co2b  = np.loadtxt('../../simulations/labile2/co2.txt', skiprows=2)
co4b  = np.loadtxt('../../simulations/labile2/co4.txt', skiprows=2)
co8b  = np.loadtxt('../../simulations/labile2/co8.txt', skiprows=2)
ro2b  = np.loadtxt('../../simulations/labile2/ro2.txt', skiprows=2)
ro4b  = np.loadtxt('../../simulations/labile2/ro4.txt', skiprows=2)
ro8b  = np.loadtxt('../../simulations/labile2/ro8.txt', skiprows=2)
to2b  = np.loadtxt('../../simulations/labile2/to2.txt', skiprows=2)
to4b  = np.loadtxt('../../simulations/labile2/to4.txt', skiprows=2)
to8b  = np.loadtxt('../../simulations/labile2/to8.txt', skiprows=2)

lx = 0.05
ly = 0.85

fig = figure()
subplots_adjust(left=0.07, hspace=0.08, right=0.95, wspace=0.08)

ax1=subplot(5, 3, 1);
ax1.plot(to2[:, 0], to2[:, 3], 'b-', to4[:, 0], to4[:, 3], 'g-', to8[:, 0], to8[:, 3], 'r-', \
         to2a[:, 0], to2a[:, 3], 'b:', to4a[:, 0], to4a[:, 3], 'g:', to8a[:, 0], to8a[:, 3], 'r:', \
         to2b[:, 0], to2b[:, 3], 'b-.', to4b[:, 0], to4b[:, 3], 'g-.', to8b[:, 0], to8b[:, 3], 'r-.', \
         trough[:, 0], trough[:, 1], 'b+', trough[:, 0], trough[:, 2], 'bx', trough[:, 0], trough[:, 3], 'b.', \
         trough[:, 0], trough[:, 4], 'g+', trough[:, 0], trough[:, 5], 'gx', trough[:, 0], trough[:, 6], 'g.', \
         trough[:, 0], trough[:, 7], 'r+', trough[:, 0], trough[:, 8], 'rx', trough[:, 0], trough[:, 9], 'r.')
plt.xlim([-5, 70])
plt.ylim([-3, 30])
plt.ylabel('CO$_2$(%)')
plt.yticks([0, 10, 20, 30])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(a1)', transform=ax1.transAxes)
plt.text(0.4, 1.08, 'trough', transform=ax1.transAxes)

ax2=subplot(5, 3, 2);
ax2.plot(ro2a[:, 0], ro2a[:, 3], 'b:', ro4a[:, 0], ro4a[:, 3], 'g:', ro8a[:, 0], ro8a[:, 3], 'r:', \
         ro2[:, 0], ro2[:, 3], 'b-', ro4[:, 0], ro4[:, 3], 'g-', ro8[:, 0], ro8[:, 3], 'r-', \
         ro2b[:, 0], ro2b[:, 3], 'b-.', ro4b[:, 0], ro4b[:, 3], 'g-.', ro8b[:, 0], ro8b[:, 3], 'r-.', \
         ridge[:, 0], ridge[:, 1], 'b+', ridge[:, 0], ridge[:, 2], 'bx', \
         ridge[:, 0], ridge[:, 5], 'r+', ridge[:, 0], ridge[:, 6], 'rx', \
         ridge[:, 0], ridge[:, 3], 'g+', ridge[:, 0], ridge[:, 4], 'gx')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.yticks([0, 10, 20, 30])
plt.xlim([-5, 70])
plt.ylim([-3, 30])
plt.text(lx, ly, '(a2)', transform=ax2.transAxes)
plt.text(0.4, 1.08, 'ridge', transform=ax2.transAxes)
plt.text(0.3, 1.30, 'organic', transform=ax2.transAxes, fontsize=15)

ax3=subplot(5, 3, 3);
ax3.plot(co2[:, 0], co2[:, 3], 'b-', co4[:, 0], co4[:, 3], 'g-', co8[:, 0], co8[:, 3], 'r-', \
         co2a[:, 0], co2a[:, 3], 'b:', co4a[:, 0], co4a[:, 3], 'g:', co8a[:, 0], co8a[:, 3], 'r:', \
         co2b[:, 0], co2b[:, 3], 'b-.', co4b[:, 0], co4b[:, 3], 'g-.', co8b[:, 0], co8b[:, 3], 'r-.', \
         center[:, 0], center[:, 1], 'b+', center[:, 0], center[:, 2], 'bx', center[:, 0], center[:, 3], 'b.', \
         center[:, 0], center[:, 4], 'g+', center[:, 0], center[:, 5], 'gx', center[:, 0], center[:, 6], 'g.', \
         center[:, 0], center[:, 7], 'r+', center[:, 0], center[:, 8], 'rx', center[:, 0], center[:, 9], 'r.')
plt.yticks([0, 10, 20, 30])
plt.xlim([-5, 70])
plt.ylim([-3, 30])
plt.text(lx, ly, '(a3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'center', transform=ax3.transAxes)

ax1=subplot(5, 3, 4);
ax1.plot(to2[:, 0], to2[:, 4], 'b-', to4[:, 0], to4[:, 4], 'g-', to8[:, 0], to8[:, 4], 'r-', \
         to2a[:, 0], to2a[:, 4], 'b:', to4a[:, 0], to4a[:, 4], 'g:', to8a[:, 0], to8a[:, 4], 'r:', \
         to2b[:, 0], to2b[:, 4], 'b-.', to4b[:, 0], to4b[:, 4], 'g-.', to8b[:, 0], to8b[:, 4], 'r-.', \
         trough[:, 0], trough[:, 19], 'bx', trough[:, 0], trough[:, 20], 'b+', trough[:, 0], trough[:, 21], 'b.', \
         trough[:, 0], trough[:, 22], 'gx', trough[:, 0], trough[:, 23], 'g+', trough[:, 0], trough[:, 24], 'g.', \
         trough[:, 0], trough[:, 25], 'rx', trough[:, 0], trough[:, 26], 'r+', trough[:, 0], trough[:, 27], 'r.')
plt.xlim([-5, 70])
plt.ylim([-0.5, 5])
plt.yticks([0, 1, 2, 3 ,4])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(b1)', transform=ax1.transAxes)
plt.ylabel('CH$_4$(%)')

ax2=subplot(5, 3, 5);
ax2.plot(ro2a[:, 0], ro2a[:, 4], 'b:', ro4a[:, 0], ro4a[:, 4], 'g:', ro8a[:, 0], ro8a[:, 4], 'r:', \
         ro2[:, 0], ro2[:, 4], 'b-', ro4[:, 0], ro4[:, 4], 'g-', ro8[:, 0], ro8[:, 4], 'r-', \
         ro2b[:, 0], ro2b[:, 4], 'b-.', ro4b[:, 0], ro4b[:, 4], 'g-.', ro8b[:, 0], ro8b[:, 4], 'r-.', \
         ridge[:, 0], ridge[:, 20], 'rx', ridge[:, 0], ridge[:, 21], 'r+', \
         ridge[:, 0], ridge[:, 16], 'bx', ridge[:, 0], ridge[:, 17], 'b+', \
         ridge[:, 0], ridge[:, 18], 'gx', ridge[:, 0], ridge[:, 19], 'g+')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([-0.5, 5])
plt.text(lx, ly, '(b2)', transform=ax2.transAxes)

ax3=subplot(5, 3, 6);
ax3.plot(co2[:, 0], co2[:, 4], 'b-', co4[:, 0], co4[:, 4], 'g-', co8[:, 0], co8[:, 4], 'r-', \
         co2a[:, 0], co2a[:, 4], 'b:', co4a[:, 0], co4a[:, 4], 'g:', co8a[:, 0], co8a[:, 4], 'r:', \
         co2b[:, 0], co2b[:, 4], 'b-.', co4b[:, 0], co4b[:, 4], 'g-.', co8b[:, 0], co8b[:, 4], 'r-.', \
         center[:, 0], center[:, 19], 'bx', center[:, 0], center[:, 20], 'b+', center[:, 0], center[:, 21], 'b.', \
         center[:, 0], center[:, 22], 'gx', center[:, 0], center[:, 23], 'g+', center[:, 0], center[:, 24], 'g.', \
         center[:, 0], center[:, 25], 'rx', center[:, 0], center[:, 26], 'r+', center[:, 0], center[:, 27], 'r.')
plt.xlim([-5, 70])
plt.ylim([-0.5, 5])
plt.text(lx, ly, '(b3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

index=9
ymax = 40.0
ot3 = [0, 30, 60];
ax1=subplot(5, 3, 7);
ac2to = [1.03,  3.83,  2.79]
ac4to = [1.03, 93.58,  1.60]
ac8to = [1.03,120.80,  2.30]
ax1.plot(to2[:, 0], to2[:, index], 'b-', to4[:, 0], to4[:, index], 'g-', to8[:, 0], to8[:, index], 'r-', \
         to2a[:, 0], to2a[:, index], 'b:', to4a[:, 0], to4a[:, index], 'g:', to8a[:, 0], to8a[:, index], 'r:', \
         to2b[:, 0], to2b[:, index], 'b-.', to4b[:, 0], to4b[:, index], 'g-.', to8b[:, 0], to8b[:, index], 'r-.', \
         ot3, ac2to, 'b+', ot3, ac4to, 'gx', ot3, ac8to, 'r.')
plt.xlim([-5, 70])
plt.ylim([-2, ymax])
plt.yticks([0, 10,  20, 30])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(c1)', transform=ax1.transAxes)
plt.ylabel('Ac (mM)')

ax2=subplot(5, 3, 8);
ot2 = [0, 30];
ac2ro = [0.057, 0.24]
ac4ro = [0.057, 0.05]
ac8ro = [0.057, 2.24]
ax2.plot(ro2a[:, 0], ro2a[:, index], 'b:', ro4a[:, 0], ro4a[:, index], 'g:', ro8a[:, 0], ro8a[:, index], 'r:', \
         ro2[:, 0], ro2[:, index], 'b-', ro4[:, 0], ro4[:, index], 'g-', ro8[:, 0], ro8[:, index], 'r-', \
         ro2b[:, 0], ro2b[:, index], 'b-.', ro4b[:, 0], ro4b[:, index], 'g-.', ro8b[:, 0], ro8b[:, index], 'r-.', \
         ot2, ac2ro, 'b+', ot2, ac4ro, 'gx', ot2, ac8ro, 'r.')
plt.xlim([-5, 70])
plt.ylim([-2, ymax])
plt.text(lx, ly, '(c2)', transform=ax2.transAxes)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)

ax3=subplot(5, 3, 9);
ac2co = [6.37, 14.71, 13.08]
ac4co = [6.37, 17.93,  6.67]
ac8co = [6.37, 21.19,  5.35]
ax3.plot(co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b:', co4a[:, 0], co4a[:, index], 'g:', co8a[:, 0], co8a[:, index], 'r:', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.', \
         ot3, ac2co, 'b+', ot3, ac4co, 'gx', ot3, ac8co, 'r.')
plt.xlim([-5, 70])
plt.ylim([-2, ymax])
plt.text(lx, ly, '(c3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

ot1 = [0, 15, 30, 60];
index = 13
ax1=subplot(5, 3, 10);
fe2to = [15.67,25.36 , 32.26 , 27.82 ]
fe4to = [15.67,21.82 , 34.03 , 33.07 ]
fe8to = [15.67,16.05 , 28.07 , 34.15 ]
ax1.plot(to2[:, 0], to2[:, index], 'b-', to4[:, 0], to4[:, index], 'g-', to8[:, 0], to8[:, index], 'r-', \
         to2a[:, 0], to2a[:, index], 'b:', to4a[:, 0], to4a[:, index], 'g:', to8a[:, 0], to8a[:, index], 'r:', \
         to2b[:, 0], to2b[:, index], 'b-.', to4b[:, 0], to4b[:, index], 'g-.', to8b[:, 0], to8b[:, index], 'r-.', \
         ot1, fe2to, 'b+', ot1, fe4to, 'gx', ot1, fe8to, 'r.')
plt.xlim([-5, 70])
plt.ylim([0, 100])
plt.yticks([0, 20, 40, 60, 80])
plt.ylabel('Fe(II) (mM)')
plt.text(lx, ly, '(d1)', transform=ax1.transAxes)
plt.setp(ax1.get_xticklabels(), visible=False)

ax2=subplot(5, 3, 11);
fe2ro = [0.102, 7.30, 20.85, 23.76]
fe4ro = [0.102, 2.62, 19.51, 37.49]
fe8ro = [0.102, 2.34, 17.90, 31.31]
ax2.plot(ro2a[:, 0], ro2a[:, index], 'b:', ro4a[:, 0], ro4a[:, index], 'g:', ro8a[:, 0], ro8a[:, index], 'r:', \
         ro2[:, 0], ro2[:, index], 'b-', ro4[:, 0], ro4[:, index], 'g-', ro8[:, 0], ro8[:, index], 'r-', \
         ro2b[:, 0], ro2b[:, index], 'b-.', ro4b[:, 0], ro4b[:, index], 'g-.', ro8b[:, 0], ro8b[:, index], 'r-.', \
         ot1, fe2ro, 'b+', ot1, fe4ro, 'gx', ot1, fe8ro, 'r.')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([0, 100])
plt.text(lx, ly, '(d2)', transform=ax2.transAxes)

ax3=subplot(5, 3, 12);
fe2co = [0.789,10.541, 10.198, 12.734]
fe4co = [0.789, 6.601, 12.568, 15.624]
fe8co = [0.789, 9.283, 16.091, 16.601]
ax3.plot(co8a[:, 0], co8a[:, index], 'r:', co8[:, 0], co8[:, index], 'r-', co8b[:, 0], co8b[:, index], 'r-.', \
         co2a[:, 0], co2a[:, index], 'b:', co4a[:, 0], co4a[:, index], 'g:', co8a[:, 0], co8a[:, index], 'r:', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.', \
         ot1, fe2co, 'b+', ot1, fe4co, 'gx', ot1, fe8co, 'r.')
plt.xlim([-5, 70])
plt.ylim([0, 100])
plt.text(lx, ly, '(d3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)
lgd = plt.legend(('$f_{\mathrm{labile}}$ = 0.002', '$f_{\mathrm{labile}}$ = 0.01', '$f_{\mathrm{labile}}$ = 0.02'),loc=1,numpoints=1)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='small') 

index = 1
ymax = 8 
ot1 = [0, 15, 30, 60];
ax1=subplot(5, 3, 13);
ph2to = [5.23, 5.20, 5.10, 5.20]
ph4to = [5.23, 5.23, 5.11, 5.76]
ph8to = [5.23, 5.23, 5.55, 6.15]
ax1.plot(to2[:, 0], to2[:, index], 'b-', to4[:, 0], to4[:, index], 'g-', to8[:, 0], to8[:, index], 'r-', \
         to2a[:, 0], to2a[:, index], 'b:', to4a[:, 0], to4a[:, index], 'g:', to8a[:, 0], to8a[:, index], 'r:', \
         to2b[:, 0], to2b[:, index], 'b-.', to4b[:, 0], to4b[:, index], 'g-.', to8b[:, 0], to8b[:, index], 'r-.', \
         ot1, ph2to, 'b+', ot1, ph4to, 'gx', ot1, ph8to, 'r.')
plt.xlim([-5, 70])
plt.ylim([4, ymax])
plt.xticks([0, 20, 40, 60])
plt.yticks([4, 5, 6, 7])
plt.ylabel('pH')
plt.text(lx, ly, '(e1)', transform=ax1.transAxes)
plt.xlabel('Time (d)')

ax2=subplot(5, 3, 14);
ph2ro = [5.21, 5.50, 6.00, 6.00]
ph4ro = [5.21, 5.21, 5.92, 6.02]
ph8ro = [5.21, 5.21, 5.98, 6.21]
ax2.plot(ro2a[:, 0], ro2a[:, index], 'b:', ro4a[:, 0], ro4a[:, index], 'g:', ro8a[:, 0], ro8a[:, index], 'r:', \
         ro2[:, 0], ro2[:, index], 'b-', ro4[:, 0], ro4[:, index], 'g-', ro8[:, 0], ro8[:, index], 'r-', \
         ro2b[:, 0], ro2b[:, index], 'b-.', ro4b[:, 0], ro4b[:, index], 'g-.', ro8b[:, 0], ro8b[:, index], 'r-.', \
         ot1, ph2ro, 'b+', ot1, ph4ro, 'gx', ot1, ph8ro, 'r.')
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([4, ymax])
plt.xticks([0, 20, 40, 60])
plt.yticks([4, 5, 6, 7])
plt.text(lx, ly, '(e2)', transform=ax2.transAxes)
plt.xlabel('Time (d)')

ax3=subplot(5, 3, 15);
ph2co = [5.02, 5.02, 5.38, 5.71]
ph4co = [5.02, 5.09, 5.62, 5.32]
ph8co = [5.02, 5.09, 5.31, 5.42]
ax3.plot(co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b:', co4a[:, 0], co4a[:, index], 'g:', co8a[:, 0], co8a[:, index], 'r:', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.', \
         ot1, ph2co, 'b+', ot1, ph4co, 'gx', ot1, ph8co, 'r.')
plt.setp(ax3.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([4, ymax])
plt.yticks([4, 5, 6, 7])
plt.xticks([0, 20, 40, 60])
plt.text(lx, ly, '(e3)', transform=ax3.transAxes)
plt.xlabel('Time (d)')

plt.subplots_adjust(left=0.08, right=0.98, top=0.92, bottom=0.06)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(7.5, 9)
savefig('fig4.png')
savefig('fig4.pdf')
#show()
