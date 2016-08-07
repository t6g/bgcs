from pylab import *

center = loadtxt('../../data/lcp_center.txt')
trough = loadtxt('../../data/lcp_trough.txt')
ridge  = loadtxt('../../data/lcp_ridge.txt')

co2  = np.loadtxt('../../simulations/final/co2.txt', skiprows=2)
co4  = np.loadtxt('../../simulations/final/co4.txt', skiprows=2)
co8  = np.loadtxt('../../simulations/final/co8.txt', skiprows=2)
cm2  = np.loadtxt('../../simulations/final/cm2.txt', skiprows=2)
cm4  = np.loadtxt('../../simulations/final/cm4.txt', skiprows=2)
cm8  = np.loadtxt('../../simulations/final/cm8.txt', skiprows=2)
ro2  = np.loadtxt('../../simulations/final/ro2.txt', skiprows=2)
ro4  = np.loadtxt('../../simulations/final/ro4.txt', skiprows=2)
ro8  = np.loadtxt('../../simulations/final/ro8.txt', skiprows=2)
rm2  = np.loadtxt('../../simulations/final/rm2.txt', skiprows=2)
rm4  = np.loadtxt('../../simulations/final/rm4.txt', skiprows=2)
rm8  = np.loadtxt('../../simulations/final/rm8.txt', skiprows=2)
to2  = np.loadtxt('../../simulations/final/to2.txt', skiprows=2)
to4  = np.loadtxt('../../simulations/final/to4.txt', skiprows=2)
to8  = np.loadtxt('../../simulations/final/to8.txt', skiprows=2)
tm2  = np.loadtxt('../../simulations/final/tm2.txt', skiprows=2)
tm4  = np.loadtxt('../../simulations/final/tm4.txt', skiprows=2)
tm8  = np.loadtxt('../../simulations/final/tm8.txt', skiprows=2)

co2a  = np.loadtxt('../../simulations/f10x/co2.txt', skiprows=2)
co4a  = np.loadtxt('../../simulations/f10x/co4.txt', skiprows=2)
co8a  = np.loadtxt('../../simulations/f10x/co8.txt', skiprows=2)
cm2a  = np.loadtxt('../../simulations/f10x/cm2.txt', skiprows=2)
cm4a  = np.loadtxt('../../simulations/f10x/cm4.txt', skiprows=2)
cm8a  = np.loadtxt('../../simulations/f10x/cm8.txt', skiprows=2)
ro2a  = np.loadtxt('../../simulations/f10x/ro2.txt', skiprows=2)
ro4a  = np.loadtxt('../../simulations/f10x/ro4.txt', skiprows=2)
ro8a  = np.loadtxt('../../simulations/f10x/ro8.txt', skiprows=2)
rm2a  = np.loadtxt('../../simulations/f10x/rm2.txt', skiprows=2)
rm4a  = np.loadtxt('../../simulations/f10x/rm4.txt', skiprows=2)
rm8a  = np.loadtxt('../../simulations/f10x/rm8.txt', skiprows=2)
to2a  = np.loadtxt('../../simulations/f10x/to2.txt', skiprows=2)
to4a  = np.loadtxt('../../simulations/f10x/to4.txt', skiprows=2)
to8a  = np.loadtxt('../../simulations/f10x/to8.txt', skiprows=2)
tm2a  = np.loadtxt('../../simulations/f10x/tm2.txt', skiprows=2)
tm4a  = np.loadtxt('../../simulations/f10x/tm4.txt', skiprows=2)
tm8a  = np.loadtxt('../../simulations/f10x/tm8.txt', skiprows=2)

co2b  = np.loadtxt('../../simulations/f100x/co2.txt', skiprows=2)
co4b  = np.loadtxt('../../simulations/f100x/co4.txt', skiprows=2)
co8b  = np.loadtxt('../../simulations/f100x/co8.txt', skiprows=2)
cm2b  = np.loadtxt('../../simulations/f100x/cm2.txt', skiprows=2)
cm4b  = np.loadtxt('../../simulations/f100x/cm4.txt', skiprows=2)
cm8b  = np.loadtxt('../../simulations/f100x/cm8.txt', skiprows=2)
ro2b  = np.loadtxt('../../simulations/f100x/ro2.txt', skiprows=2)
ro4b  = np.loadtxt('../../simulations/f100x/ro4.txt', skiprows=2)
ro8b  = np.loadtxt('../../simulations/f100x/ro8.txt', skiprows=2)
rm2b  = np.loadtxt('../../simulations/f100x/rm2.txt', skiprows=2)
rm4b  = np.loadtxt('../../simulations/f100x/rm4.txt', skiprows=2)
rm8b  = np.loadtxt('../../simulations/f100x/rm8.txt', skiprows=2)
to2b  = np.loadtxt('../../simulations/f100x/to2.txt', skiprows=2)
to4b  = np.loadtxt('../../simulations/f100x/to4.txt', skiprows=2)
to8b  = np.loadtxt('../../simulations/f100x/to8.txt', skiprows=2)
tm2b  = np.loadtxt('../../simulations/f100x/tm2.txt', skiprows=2)
tm4b  = np.loadtxt('../../simulations/f100x/tm4.txt', skiprows=2)
tm8b  = np.loadtxt('../../simulations/f100x/tm8.txt', skiprows=2)

totw = [0.013588, 0.005854, 0.011788, 0.006379, 0.010690, 0.006620] #kg   water
totc = [0.045,  0.105, 0.104,  0.105,  0.074, 0.056]                #mol  total organic carbon
scaleco = 100.0/totc[0]
scalecm = 100.0/totc[1]
scalero = 100.0/totc[2]
scalerm = 100.0/totc[3]
scaleto = 100.0/totc[4]
scaletm = 100.0/totc[5]
vwco = totw[0]/1000.0*scaleco # mM to M 
vwcm = totw[1]/1000.0*scalecm
vwro = totw[2]/1000.0*scalero
vwrm = totw[3]/1000.0*scalerm
vwto = totw[4]/1000.0*scaleto
vwtm = totw[5]/1000.0*scaletm

lx = 0.05
ly = 0.85

fig = figure()
subplots_adjust(left=0.07, hspace=0.08, right=0.95, wspace=0.08)

#CO2 in the gas phase mmole
ymax = 1.500
index = 15
index1 = 6 
ax1=subplot(7, 6, 1);
co2tm2 = tm2[:, index]*scaletm+tm2[:, index1]*vwtm;
co2tm4 = tm4[:, index]*scaletm+tm4[:, index1]*vwtm;
co2tm8 = tm8[:, index]*scaletm+tm8[:, index1]*vwtm;
co2tm2a = tm2a[:, index]*scaletm+tm2a[:, index1]*vwtm;
co2tm4a = tm4a[:, index]*scaletm+tm4a[:, index1]*vwtm;
co2tm8a = tm8a[:, index]*scaletm+tm8a[:, index1]*vwtm;
co2tm2b = tm2b[:, index]*scaletm+tm2b[:, index1]*vwtm;
co2tm4b = tm4b[:, index]*scaletm+tm4b[:, index1]*vwtm;
co2tm8b = tm8b[:, index]*scaletm+tm8b[:, index1]*vwtm;

ax1.plot(tm2[:, 0], co2tm2, 'b-', tm4[:, 0], co2tm4, 'g-', tm8[:, 0], co2tm8, 'r-',
         tm2b[:, 0], co2tm2b, 'b-.', tm4b[:, 0], co2tm4b, 'g-.', tm8b[:, 0], co2tm8b, 'r-.',
         tm2a[:, 0], co2tm2a, 'b--', tm4a[:, 0], co2tm4a, 'g--', tm8a[:, 0], co2tm8a, 'r--')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.yticks([0.0,0.5,1.0,1.5])
plt.ylabel('CO$_2$/TOTC (%)')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(a1)', transform=ax1.transAxes)
plt.text(0.4, 1.08, 'trough', transform=ax1.transAxes)

ax2=subplot(7, 6, 2);
co2rm2 = rm2[:, index]*scalerm+rm2[:, index1]*vwrm;
co2rm4 = rm4[:, index]*scalerm+rm4[:, index1]*vwrm;
co2rm8 = rm8[:, index]*scalerm+rm8[:, index1]*vwrm;
co2rm2a = rm2a[:, index]*scalerm+rm2a[:, index1]*vwrm;
co2rm4a = rm4a[:, index]*scalerm+rm4a[:, index1]*vwrm;
co2rm8a = rm8a[:, index]*scalerm+rm8a[:, index1]*vwrm;
co2rm2b = rm2b[:, index]*scalerm+rm2b[:, index1]*vwrm;
co2rm4b = rm4b[:, index]*scalerm+rm4b[:, index1]*vwrm;
co2rm8b = rm8b[:, index]*scalerm+rm8b[:, index1]*vwrm;
ax2.plot(rm2[:, 0], co2rm2, 'b-', rm4[:, 0], co2rm4, 'g-', rm8[:, 0], co2rm8, 'r-',
         rm2b[:, 0], co2rm2b, 'b-.', rm4b[:, 0], co2rm4b, 'g-.', rm8b[:, 0], co2rm8b, 'r-.',
         rm2a[:, 0], co2rm2a, 'b--', rm4a[:, 0], co2rm4a, 'g--', rm8a[:, 0], co2rm8a, 'r--')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.ylim([0, ymax])
plt.xlim([-5, 70])
plt.text(lx, ly, '(a2)', transform=ax2.transAxes)
plt.text(0.4, 1.08, 'ridge', transform=ax2.transAxes)
plt.text(0.3, 1.30, 'mineral', transform=ax2.transAxes, fontsize=15)

ax3=subplot(7, 6, 3);
co2cm2 = cm2[:, index]*scalecm+cm2[:, index1]*vwcm;
co2cm4 = cm4[:, index]*scalecm+cm4[:, index1]*vwcm;
co2cm8 = cm8[:, index]*scalecm+cm8[:, index1]*vwcm;
co2cm2a = cm2a[:, index]*scalecm+cm2a[:, index1]*vwcm;
co2cm4a = cm4a[:, index]*scalecm+cm4a[:, index1]*vwcm;
co2cm8a = cm8a[:, index]*scalecm+cm8a[:, index1]*vwcm;
co2cm2b = cm2b[:, index]*scalecm+cm2b[:, index1]*vwcm;
co2cm4b = cm4b[:, index]*scalecm+cm4b[:, index1]*vwcm;
co2cm8b = cm8b[:, index]*scalecm+cm8b[:, index1]*vwcm;
ax3.plot(cm2[:, 0], co2cm2, 'b-', cm4[:, 0], co2cm4, 'g-', cm8[:, 0], co2cm8, 'r-',
         cm2b[:, 0], co2cm2b, 'b-.', cm4b[:, 0], co2cm4b, 'g-.', cm8b[:, 0], co2cm8b, 'r-.',
         cm2a[:, 0], co2cm2a, 'b--', cm4a[:, 0], co2cm4a, 'g--', cm8a[:, 0], co2cm8a, 'r--')
plt.ylim([0, ymax])
plt.xlim([-5, 70])
plt.text(lx, ly, '(a3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'center', transform=ax3.transAxes)

ax4=subplot(7, 6, 4);
co2to2 = to2[:, index]*scaleto+to2[:, index1]*vwto;
co2to4 = to4[:, index]*scaleto+to4[:, index1]*vwto;
co2to8 = to8[:, index]*scaleto+to8[:, index1]*vwto;
co2to2a = to2a[:, index]*scaleto+to2a[:, index1]*vwto;
co2to4a = to4a[:, index]*scaleto+to4a[:, index1]*vwto;
co2to8a = to8a[:, index]*scaleto+to8a[:, index1]*vwto;
co2to2b = to2b[:, index]*scaleto+to2b[:, index1]*vwto;
co2to4b = to4b[:, index]*scaleto+to4b[:, index1]*vwto;
co2to8b = to8b[:, index]*scaleto+to8b[:, index1]*vwto;
ax4.plot(to2[:, 0], co2to2, 'b-', to4[:, 0], co2to4, 'g-', to8[:, 0], co2to8, 'r-',
         to2b[:, 0], co2to2b, 'b-.', to4b[:, 0], co2to4b, 'g-.', to8b[:, 0], co2to8b, 'r-.',
         to2a[:, 0], co2to2a, 'b--', to4a[:, 0], co2to4a, 'g--', to8a[:, 0], co2to8a, 'r--')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(a4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'trough', transform=ax4.transAxes)

ax5=subplot(7, 6, 5);
co2ro2 = ro2[:, index]*scalero+ro2[:, index1]*vwro;
co2ro4 = ro4[:, index]*scalero+ro4[:, index1]*vwro;
co2ro8 = ro8[:, index]*scalero+ro8[:, index1]*vwro;
co2ro2a = ro2a[:, index]*scalero+ro2a[:, index1]*vwro;
co2ro4a = ro4a[:, index]*scalero+ro4a[:, index1]*vwro;
co2ro8a = ro8a[:, index]*scalero+ro8a[:, index1]*vwro;
co2ro2b = ro2b[:, index]*scalero+ro2b[:, index1]*vwro;
co2ro4b = ro4b[:, index]*scalero+ro4b[:, index1]*vwro;
co2ro8b = ro8b[:, index]*scalero+ro8b[:, index1]*vwro;
ax5.plot(ro2[:, 0], co2ro2, 'b-', ro4[:, 0], co2ro4, 'g-', ro8[:, 0], co2ro8, 'r-',
         ro2b[:, 0], co2ro2b, 'b-.', ro4b[:, 0], co2ro4b, 'g-.', ro8b[:, 0], co2ro8b, 'r-.',
         ro2a[:, 0], co2ro2a, 'b--', ro4a[:, 0], co2ro4a, 'g--', ro8a[:, 0], co2ro8a, 'r--')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(a5)', transform=ax5.transAxes)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'ridge', transform=ax5.transAxes)
plt.text(0.3, 1.30, 'organic', transform=ax5.transAxes, fontsize=15)

ax6=subplot(7, 6, 6);
co2co2 = co2[:, index]*scaleco+co2[:, index1]*vwco;
co2co4 = co4[:, index]*scaleco+co4[:, index1]*vwco;
co2co8 = co8[:, index]*scaleco+co8[:, index1]*vwco;
co2co2a = co2a[:, index]*scaleco+co2a[:, index1]*vwco;
co2co4a = co4a[:, index]*scaleco+co4a[:, index1]*vwco;
co2co8a = co8a[:, index]*scaleco+co8a[:, index1]*vwco;
co2co2b = co2b[:, index]*scaleco+co2b[:, index1]*vwco;
co2co4b = co4b[:, index]*scaleco+co4b[:, index1]*vwco;
co2co8b = co8b[:, index]*scaleco+co8b[:, index1]*vwco;
ax6.plot(co2[:, 0], co2co2, 'b-', co4[:, 0], co2co4, 'g-', co8[:, 0], co2co8, 'r-',
         co2b[:, 0], co2co2b, 'b-.', co4b[:, 0], co2co4b, 'g-.', co8b[:, 0], co2co8b, 'r-.',
         co2a[:, 0], co2co2a, 'b--', co4a[:, 0], co2co4a, 'g--', co8a[:, 0], co2co8a, 'r--')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(a6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'center', transform=ax6.transAxes)

# CH4
index = 16
index1 = 7
ymax = 0.12 
ax1=subplot(7, 6, 7);
ch4tm2 = tm2[:, index]*scaletm+tm2[:, index1]*vwtm;
ch4tm4 = tm4[:, index]*scaletm+tm4[:, index1]*vwtm;
ch4tm8 = tm8[:, index]*scaletm+tm8[:, index1]*vwtm;
ch4tm2a = tm2a[:, index]*scaletm+tm2a[:, index1]*vwtm;
ch4tm4a = tm4a[:, index]*scaletm+tm4a[:, index1]*vwtm;
ch4tm8a = tm8a[:, index]*scaletm+tm8a[:, index1]*vwtm;
ch4tm2b = tm2b[:, index]*scaletm+tm2b[:, index1]*vwtm;
ch4tm4b = tm4b[:, index]*scaletm+tm4b[:, index1]*vwtm;
ch4tm8b = tm8b[:, index]*scaletm+tm8b[:, index1]*vwtm;
ax1.plot(tm2[:, 0], ch4tm2, 'b-', tm4[:, 0], ch4tm4, 'g-', tm8[:, 0], ch4tm8, 'r-',
         tm2b[:, 0], ch4tm2b, 'b-.', tm4b[:, 0], ch4tm4b, 'g-.', tm8b[:, 0], ch4tm8b, 'r-.',
         tm2a[:, 0], ch4tm2a, 'b--', tm4a[:, 0], ch4tm4a, 'g--', tm8a[:, 0], ch4tm8a, 'r--')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.yticks([0.0, 0.1])
plt.ylabel('CH$_4$/TOTC (%)')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(b1)', transform=ax1.transAxes)

ax2=subplot(7, 6, 8);
ch4rm2 = rm2[:, index]*scalerm+rm2[:, index1]*vwrm;
ch4rm4 = rm4[:, index]*scalerm+rm4[:, index1]*vwrm;
ch4rm8 = rm8[:, index]*scalerm+rm8[:, index1]*vwrm;
ch4rm2a = rm2a[:, index]*scalerm+rm2a[:, index1]*vwrm;
ch4rm4a = rm4a[:, index]*scalerm+rm4a[:, index1]*vwrm;
ch4rm8a = rm8a[:, index]*scalerm+rm8a[:, index1]*vwrm;
ch4rm2b = rm2b[:, index]*scalerm+rm2b[:, index1]*vwrm;
ch4rm4b = rm4b[:, index]*scalerm+rm4b[:, index1]*vwrm;
ch4rm8b = rm8b[:, index]*scalerm+rm8b[:, index1]*vwrm;
ax2.plot(rm2[:, 0], ch4rm2, 'b-', rm4[:, 0], ch4rm4, 'g-', rm8[:, 0], ch4rm8, 'r-',
         rm2b[:, 0], ch4rm2b, 'b-.', rm4b[:, 0], ch4rm4b, 'g-.', rm8b[:, 0], ch4rm8b, 'r-.',
         rm2a[:, 0], ch4rm2a, 'b--', rm4a[:, 0], ch4rm4a, 'g--', rm8a[:, 0], ch4rm8a, 'r--')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(b2)', transform=ax2.transAxes)

ax3=subplot(7, 6, 9);
ch4cm2 = cm2[:, index]*scalecm+cm2[:, index1]*vwcm;
ch4cm4 = cm4[:, index]*scalecm+cm4[:, index1]*vwcm;
ch4cm8 = cm8[:, index]*scalecm+cm8[:, index1]*vwcm;
ch4cm2a = cm2a[:, index]*scalecm+cm2a[:, index1]*vwcm;
ch4cm4a = cm4a[:, index]*scalecm+cm4a[:, index1]*vwcm;
ch4cm8a = cm8a[:, index]*scalecm+cm8a[:, index1]*vwcm;
ch4cm2b = cm2b[:, index]*scalecm+cm2b[:, index1]*vwcm;
ch4cm4b = cm4b[:, index]*scalecm+cm4b[:, index1]*vwcm;
ch4cm8b = cm8b[:, index]*scalecm+cm8b[:, index1]*vwcm;
ax3.plot(cm2[:, 0], ch4cm2, 'b-', cm4[:, 0], ch4cm4, 'g-', cm8[:, 0], ch4cm8, 'r-',
         cm2b[:, 0], ch4cm2b, 'b-.', cm4b[:, 0], ch4cm4b, 'g-.', cm8b[:, 0], ch4cm8b, 'r-.',
         cm2a[:, 0], ch4cm2a, 'b--', cm4a[:, 0], ch4cm4a, 'g--', cm8a[:, 0], ch4cm8a, 'r--')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(b3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

ax4=subplot(7, 6,10);
ch4to2 = to2[:, index]*scaleto+to2[:, index1]*vwto;
ch4to4 = to4[:, index]*scaleto+to4[:, index1]*vwto;
ch4to8 = to8[:, index]*scaleto+to8[:, index1]*vwto;
ch4to2a = to2a[:, index]*scaleto+to2a[:, index1]*vwto;
ch4to4a = to4a[:, index]*scaleto+to4a[:, index1]*vwto;
ch4to8a = to8a[:, index]*scaleto+to8a[:, index1]*vwto;
ch4to2b = to2b[:, index]*scaleto+to2b[:, index1]*vwto;
ch4to4b = to4b[:, index]*scaleto+to4b[:, index1]*vwto;
ch4to8b = to8b[:, index]*scaleto+to8b[:, index1]*vwto;
ax4.plot(to2[:, 0], ch4to2, 'b-', to4[:, 0], ch4to4, 'g-', to8[:, 0], ch4to8, 'r-',
         to2b[:, 0], ch4to2b, 'b-.', to4b[:, 0], ch4to4b, 'g-.', to8b[:, 0], ch4to8b, 'r-.',
         to2a[:, 0], ch4to2a, 'b--', to4a[:, 0], ch4to4a, 'g--', to8a[:, 0], ch4to8a, 'r--')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(b4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(7, 6,11);
ch4ro2 = ro2[:, index]*scalero+ro2[:, index1]*vwro;
ch4ro4 = ro4[:, index]*scalero+ro4[:, index1]*vwro;
ch4ro8 = ro8[:, index]*scalero+ro8[:, index1]*vwro;
ch4ro2a = ro2a[:, index]*scalero+ro2a[:, index1]*vwro;
ch4ro4a = ro4a[:, index]*scalero+ro4a[:, index1]*vwro;
ch4ro8a = ro8a[:, index]*scalero+ro8a[:, index1]*vwro;
ch4ro2b = ro2b[:, index]*scalero+ro2b[:, index1]*vwro;
ch4ro4b = ro4b[:, index]*scalero+ro4b[:, index1]*vwro;
ch4ro8b = ro8b[:, index]*scalero+ro8b[:, index1]*vwro;
ax5.plot(ro2[:, 0], ch4ro2, 'b-', ro4[:, 0], ch4ro4, 'g-', ro8[:, 0], ch4ro8, 'r-',
         ro2b[:, 0], ch4ro2b, 'b-.', ro4b[:, 0], ch4ro4b, 'g-.', ro8b[:, 0], ch4ro8b, 'r-.',
         ro2a[:, 0], ch4ro2a, 'b--', ro4a[:, 0], ch4ro4a, 'g--', ro8a[:, 0], ch4ro8a, 'r--')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(b5)', transform=ax5.transAxes)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)

ax6=subplot(7, 6,12);
ch4co2 = co2[:, index]*scaleco+co2[:, index1]*vwco;
ch4co4 = co4[:, index]*scaleco+co4[:, index1]*vwco;
ch4co8 = co8[:, index]*scaleco+co8[:, index1]*vwco;
ch4co2a = co2a[:, index]*scaleco+co2a[:, index1]*vwco;
ch4co4a = co4a[:, index]*scaleco+co4a[:, index1]*vwco;
ch4co8a = co8a[:, index]*scaleco+co8a[:, index1]*vwco;
ch4co2b = co2b[:, index]*scaleco+co2b[:, index1]*vwco;
ch4co4b = co4b[:, index]*scaleco+co4b[:, index1]*vwco;
ch4co8b = co8b[:, index]*scaleco+co8b[:, index1]*vwco;
ax6.plot(co2[:, 0], ch4co2, 'b-', co4[:, 0], ch4co4, 'g-', co8[:, 0], ch4co8, 'r-',
         co2b[:, 0], ch4co2b, 'b-.', co4b[:, 0], ch4co4b, 'g-.', co8b[:, 0], ch4co8b, 'r-.',
         co2a[:, 0], ch4co2a, 'b--', co4a[:, 0], ch4co4a, 'g--', co8a[:, 0], ch4co8a, 'r--')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(b6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)


index=9
ax1=subplot(7, 6, 13);
ot3 = [0, 30, 60];
ac2tm = [1.84,  3.08,  0.27]
ac4tm = [1.84,  2.30,  0.22]
ac8tm = [1.84,  3.81,  0.27]
ax1.plot(tm2[:, 0], tm2[:, index], 'b-', tm4[:, 0], tm4[:, index], 'g-', tm8[:, 0], tm8[:, index], 'r-', \
         tm2a[:, 0], tm2a[:, index], 'b--', tm4a[:, 0], tm4a[:, index], 'g--', tm8a[:, 0], tm8a[:, index], 'r--', \
         tm2b[:, 0], tm2b[:, index], 'b-.', tm4b[:, 0], tm4b[:, index], 'g-.', tm8b[:, 0], tm8b[:, index], 'r-.', \
         ot3, ac2tm, 'b+', ot3, ac4tm, 'gx', ot3, ac8tm, 'r.')
plt.xlim([-5, 70])
plt.ylim([-2, 25])
plt.yticks([0, 10,  20])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(c1)', transform=ax1.transAxes)
plt.ylabel('Ac (mM)')

ax2=subplot(7, 6, 14);
ac2rm = [2.67,  4.70,  0.29]
ac4rm = [2.67,  2.07,  0.29]
ac8rm = [2.67,  2.45,  0.29]
ax2.plot(rm2[:, 0], rm2[:, index], 'b-', rm4[:, 0], rm4[:, index], 'g-', rm8[:, 0], rm8[:, index], 'r-', \
         rm2a[:, 0], rm2a[:, index], 'b--', rm4a[:, 0], rm4a[:, index], 'g--', rm8a[:, 0], rm8a[:, index], 'r--', \
         rm2b[:, 0], rm2b[:, index], 'b-.', rm4b[:, 0], rm4b[:, index], 'g-.', rm8b[:, 0], rm8b[:, index], 'r-.', \
         ot3, ac2rm, 'b+', ot3, ac4rm, 'gx', ot3, ac8rm, 'r.')
plt.xlim([-5, 70])
plt.ylim([-2, 25])
plt.text(lx, ly, '(c2)', transform=ax2.transAxes)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)

ax3=subplot(7, 6,15);
ac2cm = [2.80,  8.50,  0.28]
ac4cm = [2.80,  7.66,  0.32]
ac8cm = [2.80,  6.42,  0.33]
ax3.plot(cm2[:, 0], cm2[:, index], 'b-', cm4[:, 0], cm4[:, index], 'g-', cm8[:, 0], cm8[:, index], 'r-', \
         cm2a[:, 0], cm2a[:, index], 'b--', cm4a[:, 0], cm4a[:, index], 'g--', cm8a[:, 0], cm8a[:, index], 'r--', \
         cm2b[:, 0], cm2b[:, index], 'b-.', cm4b[:, 0], cm4b[:, index], 'g-.', cm8b[:, 0], cm8b[:, index], 'r-.', \
         ot3, ac2cm, 'b+', ot3, ac4cm, 'gx', ot3, ac8cm, 'r.')
plt.xlim([-5, 70])
plt.ylim([-2, 25])
plt.text(lx, ly, '(c3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

ax4=subplot(7, 6, 16);
ot3 = [0, 30, 60];
ac2to = [1.03,  3.83,  2.79]
ac4to = [1.03, 93.58,  1.60]
ac8to = [1.03,120.80,  2.30]
ax4.plot(to2[:, 0], to2[:, index], 'b-', to4[:, 0], to4[:, index], 'g-', to8[:, 0], to8[:, index], 'r-', \
         to2a[:, 0], to2a[:, index], 'b--', to4a[:, 0], to4a[:, index], 'g--', to8a[:, 0], to8a[:, index], 'r--', \
         to2b[:, 0], to2b[:, index], 'b-.', to4b[:, 0], to4b[:, index], 'g-.', to8b[:, 0], to8b[:, index], 'r-.', \
         ot3, ac2to, 'b+', ot3, ac4to, 'gx', ot3, ac8to, 'r.')
plt.xlim([-5, 70])
plt.ylim([-2, 25])
plt.text(lx, ly, '(c4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(7, 6, 17);
ot2 = [0, 30];
ac2ro = [0.057, 0.24]
ac4ro = [0.057, 0.05]
ac8ro = [0.057, 2.24]
ax5.plot(ro2[:, 0], ro2[:, index], 'b-', ro4[:, 0], ro4[:, index], 'g-', ro8[:, 0], ro8[:, index], 'r-', \
         ro2a[:, 0], ro2a[:, index], 'b--', ro4a[:, 0], ro4a[:, index], 'g--', ro8a[:, 0], ro8a[:, index], 'r--', \
         ro2b[:, 0], ro2b[:, index], 'b-.', ro4b[:, 0], ro4b[:, index], 'g-.', ro8b[:, 0], ro8b[:, index], 'r-.', \
         ot2, ac2ro, 'b+', ot2, ac4ro, 'gx', ot2, ac8ro, 'r.')
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([-2, 25])
plt.text(lx, ly, '(c5)', transform=ax5.transAxes)

ax6=subplot(7, 6, 18);
ac2co = [6.37, 14.71, 13.08]
ac4co = [6.37, 17.93,  6.67]
ac8co = [6.37, 21.19,  5.35]
ax6.plot(co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b--', co4a[:, 0], co4a[:, index], 'g--', co8a[:, 0], co8a[:, index], 'r--', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.', \
         ot3, ac2co, 'b+', ot3, ac4co, 'gx', ot3, ac8co, 'r.')
plt.xlim([-5, 70])
plt.ylim([-2, 25])
plt.text(lx, ly, '(c6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)

index = 13
ax1=subplot(7, 6, 19);
ot1 = [0, 15, 30, 60];
fe2tm = [ 7.18,23.040,  30.89,  44.81]
fe4tm = [ 7.18,21.140,  59.23,  33.80]
fe8tm = [ 7.18, 5.700,  50.89,  52.41]
ax1.plot(tm2[:, 0], tm2[:, index], 'b-', tm4[:, 0], tm4[:, index], 'g-', tm8[:, 0], tm8[:, index], 'r-', \
         tm2a[:, 0], tm2a[:, index], 'b--', tm4a[:, 0], tm4a[:, index], 'g--', tm8a[:, 0], tm8a[:, index], 'r--', \
         tm2b[:, 0], tm2b[:, index], 'b-.', tm4b[:, 0], tm4b[:, index], 'g-.', tm8b[:, 0], tm8b[:, index], 'r-.', \
         ot1, fe2tm, 'b+', ot1, fe4tm, 'gx', ot1, fe8tm, 'r.')
plt.xlim([-5, 70])
plt.ylim([0, 100])
plt.yticks([0, 20, 40, 60, 80])
plt.ylabel('Fe(II) (mM)')
plt.text(lx, ly, '(d1)', transform=ax1.transAxes)
plt.setp(ax1.get_xticklabels(), visible=False)

ax2=subplot(7, 6, 20);
fe2rm = [22.97,37.570,  44.19,  32.57]
fe4rm = [22.97,30.810,  44.05,  33.51]
fe8rm = [22.97,24.870,  43.78,  38.24]
ax2.plot(rm2[:, 0], rm2[:, index], 'b-', rm4[:, 0], rm4[:, index], 'g-', rm8[:, 0], rm8[:, index], 'r-', \
         rm2a[:, 0], rm2a[:, index], 'b--', rm4a[:, 0], rm4a[:, index], 'g--', rm8a[:, 0], rm8a[:, index], 'r--', \
         rm2b[:, 0], rm2b[:, index], 'b-.', rm4b[:, 0], rm4b[:, index], 'g-.', rm8b[:, 0], rm8b[:, index], 'r-.', \
         ot1, fe2rm, 'b+', ot1, fe4rm, 'gx', ot1, fe8rm, 'r.')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([0, 100])
plt.text(lx, ly, '(d2)', transform=ax2.transAxes)

ax3=subplot(7, 6, 21);
fe2cm = [22.23,33.440, 109.22, 290.47]
fe4cm = [22.23,30.630,  75.63, 309.84]
fe8cm = [22.23,38.440,  57.34,  84.38]
ax3.plot(cm2[:, 0], cm2[:, index], 'b-', cm4[:, 0], cm4[:, index], 'g-', cm8[:, 0], cm8[:, index], 'r-', \
         cm2a[:, 0], cm2a[:, index], 'b--', cm4a[:, 0], cm4a[:, index], 'g--', cm8a[:, 0], cm8a[:, index], 'r--', \
         cm2b[:, 0], cm2b[:, index], 'b-.', cm4b[:, 0], cm4b[:, index], 'g-.', cm8b[:, 0], cm8b[:, index], 'r-.', \
         ot1, fe2cm, 'b+', ot1, fe4cm, 'gx', ot1, fe8cm, 'r.')
plt.xlim([-5, 70])
plt.ylim([0, 100])
plt.text(lx, ly, '(d3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

ax4=subplot(7, 6, 22);
fe2to = [15.67,25.36 , 32.26 , 27.82 ]
fe4to = [15.67,21.82 , 34.03 , 33.07 ]
fe8to = [15.67,16.05 , 28.07 , 34.15 ]
ax4.plot(to2[:, 0], to2[:, index], 'b-', to4[:, 0], to4[:, index], 'g-', to8[:, 0], to8[:, index], 'r-', \
         to2a[:, 0], to2a[:, index], 'b--', to4a[:, 0], to4a[:, index], 'g--', to8a[:, 0], to8a[:, index], 'r--', \
         to2b[:, 0], to2b[:, index], 'b-.', to4b[:, 0], to4b[:, index], 'g-.', to8b[:, 0], to8b[:, index], 'r-.', \
         ot1, fe2to, 'b+', ot1, fe4to, 'gx', ot1, fe8to, 'r.')
plt.xlim([-5, 70])
plt.ylim([0, 100])
plt.text(lx, ly, '(d4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(7, 6, 23);
fe2ro = [0.102, 7.30, 20.85, 23.76]
fe4ro = [0.102, 2.62, 19.51, 37.49]
fe8ro = [0.102, 2.34, 17.90, 31.31]
ax5.plot(ro2[:, 0], ro2[:, index], 'b-', ro4[:, 0], ro4[:, index], 'g-', ro8[:, 0], ro8[:, index], 'r-', \
         ro2a[:, 0], ro2a[:, index], 'b--', ro4a[:, 0], ro4a[:, index], 'g--', ro8a[:, 0], ro8a[:, index], 'r--', \
         ro2b[:, 0], ro2b[:, index], 'b-.', ro4b[:, 0], ro4b[:, index], 'g-.', ro8b[:, 0], ro8b[:, index], 'r-.', \
         ot1, fe2ro, 'b+', ot1, fe4ro, 'gx', ot1, fe8ro, 'r.')
plt.xlim([-5, 70])
plt.ylim([0, 100])
plt.text(lx, ly, '(d5)', transform=ax5.transAxes)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)

ax6=subplot(7, 6, 24);
fe2co = [0.789,10.541, 10.198, 12.734]
fe4co = [0.789, 6.601, 12.568, 15.624]
fe8co = [0.789, 9.283, 16.091, 16.601]
ax6.plot(co2[:, 0], co2[:, index], 'b-', co2a[:, 0], co2a[:, index], 'b--', co2b[:, 0], co2b[:, index], 'b-.', \
        co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b--', co4a[:, 0], co4a[:, index], 'g--', co8a[:, 0], co8a[:, index], 'r--', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.', \
         ot1, fe2co, 'b+', ot1, fe4co, 'gx', ot1, fe8co, 'r.')
plt.xlim([-5, 70])
plt.ylim([0, 100])
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)
plt.text(lx, ly, '(d6)', transform=ax6.transAxes)
lgd = plt.legend(('1x Vol', '10x Vol', '100x Vol'),loc=1,numpoints=1)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='small') 

index = 1
ymax = 7 
ax1=subplot(7, 6, 25);
ot1 = [0, 15, 30, 60];
ph2tm = [4.95, 5.10, 5.61, 5.90]
ph4tm = [4.95, 4.95, 5.39, 5.61]
ph8tm = [4.95, 4.95, 5.53, 5.98]
ax1.plot(tm2[:, 0], tm2[:, index], 'b-', tm4[:, 0], tm4[:, index], 'g-', tm8[:, 0], tm8[:, index], 'r-', \
         tm2a[:, 0], tm2a[:, index], 'b--', tm4a[:, 0], tm4a[:, index], 'g--', tm8a[:, 0], tm8a[:, index], 'r--', \
         tm2b[:, 0], tm2b[:, index], 'b-.', tm4b[:, 0], tm4b[:, index], 'g-.', tm8b[:, 0], tm8b[:, index], 'r-.', \
         ot1, ph2tm, 'b+', ot1, ph4tm, 'gx', ot1, ph8tm, 'r.')
plt.xlim([-5, 70])
plt.ylim([4, ymax])
plt.xticks([0, 20, 40, 60])
plt.yticks([4, 5, 6])
plt.ylabel('pH')
plt.text(lx, ly, '(e1)', transform=ax1.transAxes)
plt.setp(ax1.get_xticklabels(), visible=False)

ax2=subplot(7, 6, 26);
ph2rm = [4.54, 4.50, 5.50, 5.03]
ph4rm = [4.54, 4.54, 5.34, 5.12]
ph8rm = [4.54, 4.54, 4.60, 4.90]
ax2.plot(rm2[:, 0], rm2[:, index], 'b-', rm4[:, 0], rm4[:, index], 'g-', rm8[:, 0], rm8[:, index], 'r-', \
         rm2a[:, 0], rm2a[:, index], 'b--', rm4a[:, 0], rm4a[:, index], 'g--', rm8a[:, 0], rm8a[:, index], 'r--', \
         rm2b[:, 0], rm2b[:, index], 'b-.', rm4b[:, 0], rm4b[:, index], 'g-.', rm8b[:, 0], rm8b[:, index], 'r-.', \
         ot1, ph2rm, 'b+', ot1, ph4rm, 'gx', ot1, ph8rm, 'r.')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([4, ymax])
plt.xticks([0, 20, 40, 60])
plt.yticks([4, 5, 6, 7])
plt.text(lx, ly, '(e2)', transform=ax2.transAxes)

ax3=subplot(7, 6, 27);
ph2cm = [4.84, 4.83, 5.67, 4.90]
ph4cm = [4.84, 4.83, 5.74, 5.81]
ph8cm = [4.84, 4.83, 5.89, 6.10]
ax3.plot(cm2[:, 0], cm2[:, index], 'b-', cm4[:, 0], cm4[:, index], 'g-', cm8[:, 0], cm8[:, index], 'r-', \
         cm2a[:, 0], cm2a[:, index], 'b--', cm4a[:, 0], cm4a[:, index], 'g--', cm8a[:, 0], cm8a[:, index], 'r--', \
         cm2b[:, 0], cm2b[:, index], 'b-.', cm4b[:, 0], cm4b[:, index], 'g-.', cm8b[:, 0], cm8b[:, index], 'r-.', \
         ot1, ph2cm, 'b+', ot1, ph4cm, 'gx', ot1, ph8cm, 'r.')
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([4, ymax])
plt.xticks([0, 20, 40, 60])
plt.yticks([4, 5, 6, 7])
plt.text(lx, ly, '(e3)', transform=ax3.transAxes)

ax4=subplot(7, 6, 28);
ph2to = [5.23, 5.20, 5.10, 5.20]
ph4to = [5.23, 5.23, 5.11, 5.76]
ph8to = [5.23, 5.23, 5.55, 6.15]
ax4.plot(to2[:, 0], to2[:, index], 'b-', to4[:, 0], to4[:, index], 'g-', to8[:, 0], to8[:, index], 'r-', \
         to2a[:, 0], to2a[:, index], 'b--', to4a[:, 0], to4a[:, index], 'g--', to8a[:, 0], to8a[:, index], 'r--', \
         to2b[:, 0], to2b[:, index], 'b-.', to4b[:, 0], to4b[:, index], 'g-.', to8b[:, 0], to8b[:, index], 'r-.', \
         ot1, ph2to, 'b+', ot1, ph4to, 'gx', ot1, ph8to, 'r.')
plt.xlim([-5, 70])
plt.ylim([4, ymax])
plt.xticks([0, 20, 40, 60])
plt.yticks([4, 5, 6, 7])
plt.text(lx, ly, '(e4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(7, 6, 29);
ph2ro = [5.21, 5.50, 6.00, 6.00]
ph4ro = [5.21, 5.21, 5.92, 6.02]
ph8ro = [5.21, 5.21, 5.98, 6.21]
ax5.plot(ro2[:, 0], ro2[:, index], 'b-', ro4[:, 0], ro4[:, index], 'g-', ro8[:, 0], ro8[:, index], 'r-', \
         ro2a[:, 0], ro2a[:, index], 'b--', ro4a[:, 0], ro4a[:, index], 'g--', ro8a[:, 0], ro8a[:, index], 'r--', \
         ro2b[:, 0], ro2b[:, index], 'b-.', ro4b[:, 0], ro4b[:, index], 'g-.', ro8b[:, 0], ro8b[:, index], 'r-.', \
         ot1, ph2ro, 'b+', ot1, ph4ro, 'gx', ot1, ph8ro, 'r.')
plt.xlim([-5, 70])
plt.ylim([4, ymax])
plt.xticks([0, 20, 40, 60])
plt.yticks([4, 5, 6, 7])
plt.text(lx, ly, '(e5)', transform=ax5.transAxes)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)

ax6=subplot(7, 6, 30);
ph2co = [5.02, 5.02, 5.38, 5.71]
ph4co = [5.02, 5.09, 5.62, 5.32]
ph8co = [5.02, 5.09, 5.31, 5.42]
ax6.plot(co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b--', co4a[:, 0], co4a[:, index], 'g--', co8a[:, 0], co8a[:, index], 'r--', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.', \
         ot1, ph2co, 'b+', ot1, ph4co, 'gx', ot1, ph8co, 'r.')
plt.xlim([-5, 70])
plt.ylim([4, ymax])
plt.xticks([0, 20, 40, 60])
plt.yticks([4, 5, 6, 7])
plt.text(lx, ly, '(e6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)

ymax = 20.0

ax1=subplot(7, 6, 31);
ax1.plot(tm2[:, 0], tm2[:, 3], 'b-', tm4[:, 0], tm4[:, 3], 'g-', tm8[:, 0], tm8[:, 3], 'r-', \
         tm2a[:, 0], tm2a[:, 3], 'b--', tm4a[:, 0], tm4a[:, 3], 'g--', tm8a[:, 0], tm8a[:, 3], 'r--', \
         tm2b[:, 0], tm2b[:, 3], 'b-.', tm4b[:, 0], tm4b[:, 3], 'g-.', tm8b[:, 0], tm8b[:, 3], 'r-.')
plt.xlim([-5, 70])
plt.ylim([-3, ymax])
plt.ylabel('CO$_2$ (%)')
plt.yticks([0, 5, 10, 15])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(f1)', transform=ax1.transAxes)

ax2=subplot(7, 6, 32);
ax2.plot(rm2[:, 0], rm2[:, 3], 'b-', rm4[:, 0], rm4[:, 3], 'g-', rm8[:, 0], rm8[:, 3], 'r-', \
         rm2a[:, 0], rm2a[:, 3], 'b--', rm4a[:, 0], rm4a[:, 3], 'g--', rm8a[:, 0], rm8a[:, 3], 'r--', \
         rm2b[:, 0], rm2b[:, 3], 'b-.', rm4b[:, 0], rm4b[:, 3], 'g-.', rm8b[:, 0], rm8b[:, 3], 'r-.')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.yticks([0, 10, 20])
plt.xlim([-5, 70])
plt.ylim([-3, ymax])
plt.text(lx, ly, '(f2)', transform=ax2.transAxes)

ax3=subplot(7, 6, 33);
ax3.plot(cm2[:, 0], cm2[:, 3], 'b-', cm4[:, 0], cm4[:, 3], 'g-', cm8[:, 0], cm8[:, 3], 'r-', \
         cm2a[:, 0], cm2a[:, 3], 'b--', cm4a[:, 0], cm4a[:, 3], 'g--', cm8a[:, 0], cm8a[:, 3], 'r--', \
         cm2b[:, 0], cm2b[:, 3], 'b-.', cm4b[:, 0], cm4b[:, 3], 'g-.', cm8b[:, 0], cm8b[:, 3], 'r-.')
plt.yticks([0, 10, 20, 30])
plt.xlim([-5, 70])
plt.ylim([-3, ymax])
plt.text(lx, ly, '(f3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

ax4=subplot(7, 6, 34);
ax4.plot(to2[:, 0], to2[:, 3], 'b-', to4[:, 0], to4[:, 3], 'g-', to8[:, 0], to8[:, 3], 'r-', \
         to2a[:, 0], to2a[:, 3], 'b--', to4a[:, 0], to4a[:, 3], 'g--', to8a[:, 0], to8a[:, 3], 'r--', \
         to2b[:, 0], to2b[:, 3], 'b-.', to4b[:, 0], to4b[:, 3], 'g-.', to8b[:, 0], to8b[:, 3], 'r-.')
plt.xlim([-5, 70])
plt.ylim([-3, ymax])
plt.text(lx, ly, '(f4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(7, 6, 35);
ax5.plot(ro2[:, 0], ro2[:, 3], 'b-', ro4[:, 0], ro4[:, 3], 'g-', ro8[:, 0], ro8[:, 3], 'r-', \
         ro2a[:, 0], ro2a[:, 3], 'b--', ro4a[:, 0], ro4a[:, 3], 'g--', ro8a[:, 0], ro8a[:, 3], 'r--', \
         ro2b[:, 0], ro2b[:, 3], 'b-.', ro4b[:, 0], ro4b[:, 3], 'g-.', ro8b[:, 0], ro8b[:, 3], 'r-.')
plt.xlim([-5, 70])
plt.ylim([-3, ymax])
plt.text(lx, ly, '(f5)', transform=ax5.transAxes)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)

ax6=subplot(7, 6, 36);
ax6.plot(co2[:, 0], co2[:, 3], 'b-', co4[:, 0], co4[:, 3], 'g-', co8[:, 0], co8[:, 3], 'r-', \
         co2a[:, 0], co2a[:, 3], 'b--', co4a[:, 0], co4a[:, 3], 'g--', co8a[:, 0], co8a[:, 3], 'r--', \
         co2b[:, 0], co2b[:, 3], 'b-.', co4b[:, 0], co4b[:, 3], 'g-.', co8b[:, 0], co8b[:, 3], 'r-.')
plt.xlim([-5, 70])
plt.ylim([-3, ymax])
plt.text(lx, ly, '(f6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)

#index = 30
index = 6
ymax = 20.0
ax1=subplot(7, 6, 37);
ax1.plot(tm2[:, 0], tm2[:, index], 'b-', tm4[:, 0], tm4[:, index], 'g-', tm8[:, 0], tm8[:, index], 'r-', \
         tm2a[:, 0], tm2a[:, index], 'b--', tm4a[:, 0], tm4a[:, index], 'g--', tm8a[:, 0], tm8a[:, index], 'r--', \
         tm2b[:, 0], tm2b[:, index], 'b-.', tm4b[:, 0], tm4b[:, index], 'g-.', tm8b[:, 0], tm8b[:, index], 'r-.')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.ylabel('CO$_2$ (mM)')
plt.text(lx, ly, '(g1)', transform=ax1.transAxes)
plt.xlabel('Time (d)')
plt.xticks([0, 20, 40, 60])
plt.yticks([0, 5, 10, 15])

ax2=subplot(7, 6, 38);
ax2.plot(rm2[:, 0], rm2[:, index], 'b-', rm4[:, 0], rm4[:, index], 'g-', rm8[:, 0], rm8[:, index], 'r-', \
         rm2a[:, 0], rm2a[:, index], 'b--', rm4a[:, 0], rm4a[:, index], 'g--', rm8a[:, 0], rm8a[:, index], 'r--', \
         rm2b[:, 0], rm2b[:, index], 'b-.', rm4b[:, 0], rm4b[:, index], 'g-.', rm8b[:, 0], rm8b[:, index], 'r-.')
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(g2)', transform=ax2.transAxes)
plt.xlabel('Time (d)')
plt.xticks([0, 20, 40, 60])

ax3=subplot(7, 6, 39);
ax3.plot(cm2[:, 0], cm2[:, index], 'b-', cm4[:, 0], cm4[:, index], 'g-', cm8[:, 0], cm8[:, index], 'r-', \
         cm2a[:, 0], cm2a[:, index], 'b--', cm4a[:, 0], cm4a[:, index], 'g--', cm8a[:, 0], cm8a[:, index], 'r--', \
         cm2b[:, 0], cm2b[:, index], 'b-.', cm4b[:, 0], cm4b[:, index], 'g-.', cm8b[:, 0], cm8b[:, index], 'r-.')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(g3)', transform=ax3.transAxes)
plt.setp(ax3.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')
plt.xticks([0, 20, 40, 60])

ax4=subplot(7, 6, 40);
ax4.plot(to8[:, 0], to8[:, index], 'r-', to8a[:, 0], to8a[:, index], 'r--', to8b[:, 0], to8b[:, index], 'r-.', \
         to2[:, 0], to2[:, index], 'b-', to4[:, 0], to4[:, index], 'g-', to8[:, 0], to8[:, index], 'r-', \
         to2a[:, 0], to2a[:, index], 'b--', to4a[:, 0], to4a[:, index], 'g--', to8a[:, 0], to8a[:, index], 'r--', \
         to2b[:, 0], to2b[:, index], 'b-.', to4b[:, 0], to4b[:, index], 'g-.', to8b[:, 0], to8b[:, index], 'r-.')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(g4)', transform=ax4.transAxes)
plt.setp(ax4.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')
plt.xticks([0, 20, 40, 60])

ax5=subplot(7, 6, 41);
ax5.plot(ro2[:, 0], ro2[:, index], 'b-', ro4[:, 0], ro4[:, index], 'g-', ro8[:, 0], ro8[:, index], 'r-', \
         ro2a[:, 0], ro2a[:, index], 'b--', ro4a[:, 0], ro4a[:, index], 'g--', ro8a[:, 0], ro8a[:, index], 'r--', \
         ro2b[:, 0], ro2b[:, index], 'b-.', ro4b[:, 0], ro4b[:, index], 'g-.', ro8b[:, 0], ro8b[:, index], 'r-.')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(g5)', transform=ax5.transAxes)
plt.setp(ax5.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')
plt.xticks([0, 20, 40, 60])

ax6=subplot(7, 6, 42);
ax6.plot(co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b--', co4a[:, 0], co4a[:, index], 'g--', co8a[:, 0], co8a[:, index], 'r--', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(g6)', transform=ax6.transAxes)
plt.setp(ax6.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')
plt.xticks([0, 20, 40, 60])


plt.subplots_adjust(left=0.06, right=0.98, top=0.95, bottom=0.06)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(12, 11)
savefig('figsb.png')
savefig('figsb.pdf')
#show()
