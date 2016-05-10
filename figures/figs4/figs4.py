from pylab import *

"""
co2  = np.loadtxt('../simulations/labile2/co2.txt', skiprows=2)
co4  = np.loadtxt('../simulations/labile2/co4.txt', skiprows=2)
co8  = np.loadtxt('../simulations/labile2/co8.txt', skiprows=2)
cm2  = np.loadtxt('../simulations/fe31/cm2.txt', skiprows=2)
cm4  = np.loadtxt('../simulations/fe31/cm4.txt', skiprows=2)
cm8  = np.loadtxt('../simulations/fe31/cm8.txt', skiprows=2)
ro2  = np.loadtxt('../simulations/labile2/ro2.txt', skiprows=2)
ro4  = np.loadtxt('../simulations/labile2/ro4.txt', skiprows=2)
ro8  = np.loadtxt('../simulations/labile2/ro8.txt', skiprows=2)
rm2  = np.loadtxt('../simulations/fe31/rm2.txt', skiprows=2)
rm4  = np.loadtxt('../simulations/fe31/rm4.txt', skiprows=2)
rm8  = np.loadtxt('../simulations/fe31/rm8.txt', skiprows=2)
to2  = np.loadtxt('../simulations/labile2/to2.txt', skiprows=2)
to4  = np.loadtxt('../simulations/labile2/to4.txt', skiprows=2)
to8  = np.loadtxt('../simulations/labile2/to8.txt', skiprows=2)
tm2  = np.loadtxt('../simulations/fe31/tm2.txt', skiprows=2)
tm4  = np.loadtxt('../simulations/fe31/tm4.txt', skiprows=2)
tm8  = np.loadtxt('../simulations/fe31/tm8.txt', skiprows=2)
"""

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

#CO2 in the gas phase mmole
ymax = 0.600
index = 15
index1 = 6 
ax1=subplot(9, 6, 1);
ax1.plot(tm2[:, 0], tm2[:, index]*scaletm+tm2[:, index1]*vwtm, 'b-', tm4[:, 0], tm4[:, index]*scaletm+tm4[:, index1]*vwtm, 'g-', tm8[:, 0], tm8[:, index]*scaletm+tm8[:, index1]*vwtm, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.yticks([0.0,0.2,0.4])
plt.ylabel('CO$_2$')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(a1)', transform=ax1.transAxes)
plt.text(0.4, 1.08, 'trough', transform=ax1.transAxes)

ax2=subplot(9, 6, 2);
ax2.plot(rm2[:, 0], rm2[:, index]*scalerm+rm2[:,index1]*vwrm, 'b-', rm4[:, 0], rm4[:, index]*scalerm+rm4[:,index1]*vwrm, 'g-', rm8[:, 0], rm8[:, index]*scalerm+rm8[:,index1]*vwrm, 'r-')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.ylim([0, ymax])
plt.xlim([-5, 70])
plt.text(lx, ly, '(a2)', transform=ax2.transAxes)
plt.text(0.4, 1.08, 'ridge', transform=ax2.transAxes)
plt.text(0.3, 1.30, 'mineral', transform=ax2.transAxes, fontsize=15)

ax3=subplot(9, 6, 3);
ax3.plot(cm2[:, 0], cm2[:, index]*scalecm+cm2[:,index1]*vwcm, 'b-', cm4[:, 0], cm4[:, index]*scalecm+cm4[:,index1]*vwcm, 'g-', cm8[:, 0], cm8[:, index]*scalecm+cm8[:,index1]*vwcm, 'r-')
plt.ylim([0, ymax])
plt.xlim([-5, 70])
plt.text(lx, ly, '(a3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'center', transform=ax3.transAxes)

ax4=subplot(9, 6, 4);
ax4.plot(to2[:, 0], to2[:, index]*scaleto+to2[:,index1]*vwto, 'b-', to4[:, 0], to4[:, index]*scaleto+to4[:,index1]*vwto, 'g-', to8[:, 0], to8[:, index]*scaleto+to8[:,index1]*vwto, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(a4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'trough', transform=ax4.transAxes)

ax5=subplot(9, 6, 5);
ax5.plot(ro2[:, 0], ro2[:, index]*scalero+ro2[:,index1]*vwro, 'b-', ro4[:, 0], ro4[:, index]*scalero+ro4[:,index1]*vwro, 'g-', ro8[:, 0], ro8[:, index]*scalero+ro8[:,index1]*vwro, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(a5)', transform=ax5.transAxes)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'ridge', transform=ax5.transAxes)
plt.text(0.3, 1.30, 'organic', transform=ax5.transAxes, fontsize=15)

ax6=subplot(9, 6, 6);
ax6.plot(co2[:, 0], co2[:, index]*scaleco+co2[:,index1]*vwco, 'b-', co4[:, 0], co4[:, index]*scaleco+co4[:,index1]*vwco, 'g-', co8[:, 0], co8[:, index]*scaleco+co8[:,index1]*vwco, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(a6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'center', transform=ax6.transAxes)

# CH4
index = 16
index1 = 7
ymax = 0.1 
ax1=subplot(9, 6, 7);
ax1.plot(tm2[:, 0], tm2[:, index]*scaletm+tm2[:, index1]*vwtm, 'b-', tm4[:, 0], tm4[:, index]*scaletm+tm4[:, index1]*vwtm, 'g-', tm8[:, 0], tm8[:, index]*scaletm+tm8[:, index1]*vwtm, 'r-')
#ax1.plot(tm2[:, 0], tm2[:, index]*vwtm, 'b-', tm4[:, 0], tm4[:, index]*vwtm, 'g-', tm8[:, 0], tm8[:, index]*vwtm, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.yticks([0.0, 0.04, 0.08])
plt.ylabel('CH$_4$')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(b1)', transform=ax1.transAxes)

ax2=subplot(9, 6, 8);
ax2.plot(rm2[:, 0], rm2[:, index]*scalerm+rm2[:,index1]*vwrm, 'b-', rm4[:, 0], rm4[:, index]*scalerm+rm4[:,index1]*vwrm, 'g-', rm8[:, 0], rm8[:, index]*scalerm+rm8[:,index1]*vwrm, 'r-')
#ax2.plot(rm2[:, 0], rm2[:, index]*vwrm, 'b-', rm4[:, 0], rm4[:, index]*vwrm, 'g-', rm8[:, 0], rm8[:, index]*vwrm, 'r-')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(b2)', transform=ax2.transAxes)

ax3=subplot(9, 6, 9);
ax3.plot(cm2[:, 0], cm2[:, index]*scalecm+cm2[:,index1]*vwcm, 'b-', cm4[:, 0], cm4[:, index]*scalecm+cm4[:,index1]*vwcm, 'g-', cm8[:, 0], cm8[:, index]*scalecm+cm8[:,index1]*vwcm, 'r-')
#ax3.plot(cm2[:, 0], cm2[:, index]*vwcm, 'b-', cm4[:, 0], cm4[:, index]*vwcm, 'g-', cm8[:, 0], cm8[:, index]*vwcm, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(b3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

ax4=subplot(9, 6,10);
ax4.plot(to2[:, 0], to2[:, index]*scaleto+to2[:,index1]*vwto, 'b-', to4[:, 0], to4[:, index]*scaleto+to4[:,index1]*vwto, 'g-', to8[:, 0], to8[:, index]*scaleto+to8[:,index1]*vwto, 'r-')
#ax4.plot(to2[:, 0], to2[:, index]*vwto, 'b-', to4[:, 0], to4[:, index]*vwto, 'g-', to8[:, 0], to8[:, index]*vwto, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(b4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(9, 6,11);
ax5.plot(ro2[:, 0], ro2[:, index]*scalero+ro2[:,index1]*vwro, 'b-', ro4[:, 0], ro4[:, index]*scalero+ro4[:,index1]*vwro, 'g-', ro8[:, 0], ro8[:, index]*scalero+ro8[:,index1]*vwro, 'r-')
#ax5.plot(ro2[:, 0], ro2[:, index]*vwro, 'b-', ro4[:, 0], ro4[:, index]*vwro, 'g-', ro8[:, 0], ro8[:, index]*vwro, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(b5)', transform=ax5.transAxes)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)

ax6=subplot(9, 6,12);
#ax6.plot(co2[:, 0], co2[:, index]*vwco, 'b-', co4[:, 0], co4[:, index]*vwco, 'g-', co8[:, 0], co8[:, index]*vwco, 'r-')
ax6.plot(co2[:, 0], co2[:, index]*scaleco+co2[:,index1]*vwco, 'b-', co4[:, 0], co4[:, index]*scaleco+co4[:,index1]*vwco, 'g-', co8[:, 0], co8[:, index]*scaleco+co8[:,index1]*vwco, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(b6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)

# aqueous CH3COOH phase mmole
index = 9
ymax = 0.6
stoich = 2.0
ax1=subplot(9, 6,13);
ax1.plot(tm2[:, 0], tm2[:, index]*vwtm*stoich, 'b-', tm4[:, 0], tm4[:, index]*vwtm*stoich, 'g-', tm8[:, 0], tm8[:, index]*vwtm*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.yticks([0.0, 0.2, 0.4])
plt.ylabel('Acetate-C')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(d1)', transform=ax1.transAxes)

ax2=subplot(9, 6,14);
ax2.plot(rm2[:, 0], rm2[:, index]*vwrm*stoich, 'b-', rm4[:, 0], rm4[:, index]*vwrm*stoich, 'g-', rm8[:, 0], rm8[:, index]*vwrm*stoich, 'r-')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(d2)', transform=ax2.transAxes)

ax3=subplot(9, 6,15);
ax3.plot(cm2[:, 0], cm2[:, index]*vwcm*stoich, 'b-', cm4[:, 0], cm4[:, index]*vwcm*stoich, 'g-', cm8[:, 0], cm8[:, index]*vwcm*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(d3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

ax4=subplot(9, 6,16);
ax4.plot(to2[:, 0], to2[:, index]*vwto*stoich, 'b-', to4[:, 0], to4[:, index]*vwto*stoich, 'g-', to8[:, 0], to8[:, index]*vwto*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(d4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(9, 6,17);
ax5.plot(ro2[:, 0], ro2[:, index]*vwro*stoich, 'b-', ro4[:, 0], ro4[:, index]*vwro*stoich, 'g-', ro8[:, 0], ro8[:, index]*vwro*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(d5)', transform=ax5.transAxes)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)

ax6=subplot(9, 6,18);
ax6.plot(co2[:, 0], co2[:, index]*vwco*stoich, 'b-', co4[:, 0], co4[:, index]*vwco*stoich, 'g-', co8[:, 0], co8[:, index]*vwco*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(d6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)

# aqueous labiledoc phase mmole
index = 10
ymax = 0.1
stoich = 6.0
ax1=subplot(9, 6,19);
ax1.plot(tm2[:, 0], tm2[:, index]*vwtm*stoich, 'b-', tm4[:, 0], tm4[:, index]*vwtm*stoich, 'g-', tm8[:, 0], tm8[:, index]*vwtm*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.yticks([0.0, 0.04, 0.08])
plt.ylabel('LabileDOC')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(e1)', transform=ax1.transAxes)

ax2=subplot(9, 6,20);
ax2.plot(rm2[:, 0], rm2[:, index]*vwrm*stoich, 'b-', rm4[:, 0], rm4[:, index]*vwrm*stoich, 'g-', rm8[:, 0], rm8[:, index]*vwrm*stoich, 'r-')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(e2)', transform=ax2.transAxes)

ax3=subplot(9, 6,21);
ax3.plot(cm2[:, 0], cm2[:, index]*vwcm*stoich, 'b-', cm4[:, 0], cm4[:, index]*vwcm*stoich, 'g-', cm8[:, 0], cm8[:, index]*vwcm*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(e3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

ax4=subplot(9, 6,22);
ax4.plot(to2[:, 0], to2[:, index]*vwto*stoich, 'b-', to4[:, 0], to4[:, index]*vwto*stoich, 'g-', to8[:, 0], to8[:, index]*vwto*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(e4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(9, 6,23);
ax5.plot(ro2[:, 0], ro2[:, index]*vwro*stoich, 'b-', ro4[:, 0], ro4[:, index]*vwro*stoich, 'g-', ro8[:, 0], ro8[:, index]*vwro*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(e5)', transform=ax5.transAxes)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)

ax6=subplot(9, 6,24);
ax6.plot(co2[:, 0], co2[:, index]*vwco*stoich, 'b-', co4[:, 0], co4[:, index]*vwco*stoich, 'g-', co8[:, 0], co8[:, index]*vwco*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(e6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)

#FeRB
index = 23
stoich = 6.0
ymax = 0.05
ax1=subplot(9, 6,25);
ax1.plot(tm2[:, 0], tm2[:, index]*scaletm*stoich, 'b-', tm4[:, 0], tm4[:, index]*scaletm*stoich, 'g-', tm8[:, 0], tm8[:, index]*scaletm*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.yticks([0.0, 0.01, 0.02, 0.03, 0.04])
plt.ylabel('FeRB-C')
plt.text(lx, ly, '(f1)', transform=ax1.transAxes)
plt.setp(ax1.get_xticklabels(), visible=False)

ax2=subplot(9, 6,26);
ax2.plot(rm2[:, 0], rm2[:, index]*scalerm*stoich, 'b-', rm4[:, 0], rm4[:, index]*scalerm*stoich, 'g-', rm8[:, 0], rm8[:, index]*scalerm*stoich, 'r-')
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(f2)', transform=ax2.transAxes)
plt.setp(ax2.get_xticklabels(), visible=False)

ax3=subplot(9, 6,27);
ax3.plot(cm2[:, 0], cm2[:, index]*scalecm*stoich, 'b-', cm4[:, 0], cm4[:, index]*scalecm*stoich, 'g-', cm8[:, 0], cm8[:, index]*scalecm*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(f3)', transform=ax3.transAxes)
plt.setp(ax3.get_yticklabels(), visible=False)
plt.setp(ax3.get_xticklabels(), visible=False)

ax4=subplot(9, 6,28);
ax4.plot(to2[:, 0], to2[:, index]*scaleto*stoich, 'b-', to4[:, 0], to4[:, index]*scaleto*stoich, 'g-', to8[:, 0], to8[:, index]*scaleto*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(f4)', transform=ax4.transAxes)
plt.setp(ax4.get_yticklabels(), visible=False)
plt.setp(ax4.get_xticklabels(), visible=False)

ax5=subplot(9, 6,29);
ax5.plot(ro2[:, 0], ro2[:, index]*scalero*stoich, 'b-', ro4[:, 0], ro4[:, index]*scalero*stoich, 'g-', ro8[:, 0], ro8[:, index]*scalero*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(f5)', transform=ax5.transAxes)
plt.setp(ax5.get_yticklabels(), visible=False)
plt.setp(ax5.get_xticklabels(), visible=False)

ax6=subplot(9, 6,30);
ax6.plot(co2[:, 0], co2[:, index]*scaleco*stoich, 'b-', co4[:, 0], co4[:, index]*scaleco*stoich, 'g-', co8[:, 0], co8[:, index]*scaleco*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(f6)', transform=ax6.transAxes)
plt.setp(ax6.get_yticklabels(), visible=False)
plt.setp(ax6.get_xticklabels(), visible=False)

#MeGA
index = 24
ymax = 0.005
stoich = 6.0
ax1=subplot(9, 6,31);
ax1.plot(tm2[:, 0], tm2[:, index]*scaletm*stoich, 'b-', tm4[:, 0], tm4[:, index]*scaletm*stoich, 'g-', tm8[:, 0], tm8[:, index]*scaletm*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.yticks([0.0, 0.001, 0.002, 0.003, 0.004])
plt.ylabel('MeGA-C')
plt.text(lx, ly, '(g1)', transform=ax1.transAxes)
plt.setp(ax1.get_xticklabels(), visible=False)

ax2=subplot(9, 6,32);
ax2.plot(rm2[:, 0], rm2[:, index]*scalerm*stoich, 'b-', rm4[:, 0], rm4[:, index]*scalerm*stoich, 'g-', rm8[:, 0], rm8[:, index]*scalerm*stoich, 'r-')
plt.setp(ax2.get_yticklabels(), visible=False)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(g2)', transform=ax2.transAxes)

ax3=subplot(9, 6,33);
ax3.plot(cm2[:, 0], cm2[:, index]*scalecm*stoich, 'b-', cm4[:, 0], cm4[:, index]*scalecm*stoich, 'g-', cm8[:, 0], cm8[:, index]*scalecm*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(g3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

ax4=subplot(9, 6,34);
ax4.plot(to2[:, 0], to2[:, index]*scaleto*stoich, 'b-', to4[:, 0], to4[:, index]*scaleto*stoich, 'g-', to8[:, 0], to8[:, index]*scaleto*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(g4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(9, 6,35);
ax5.plot(ro2[:, 0], ro2[:, index]*scalero*stoich, 'b-', ro4[:, 0], ro4[:, index]*scalero*stoich, 'g-', ro8[:, 0], ro8[:, index]*scalero*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(g5)', transform=ax5.transAxes)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)

ax6=subplot(9, 6,36);
ax6.plot(co2[:, 0], co2[:, index]*scaleco*stoich, 'b-', co4[:, 0], co4[:, index]*scaleco*stoich, 'g-', co8[:, 0], co8[:, index]*scaleco*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(g6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)

#MeGH
index = 25
stoich = 6.0
ax1=subplot(9, 6,37);
ax1.plot(tm2[:, 0], tm2[:, index]*scaletm*stoich, 'b-', tm4[:, 0], tm4[:, index]*scaletm*stoich, 'g-', tm8[:, 0], tm8[:, index]*scaletm*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.yticks([0.0, 0.001, 0.002, 0.003, 0.004])
plt.ylabel('MeGH-C')
plt.text(lx, ly, '(h1)', transform=ax1.transAxes)
plt.setp(ax1.get_xticklabels(), visible=False)

ax2=subplot(9, 6,38);
ax2.plot(rm2[:, 0], rm2[:, index]*scalerm*stoich, 'b-', rm4[:, 0], rm4[:, index]*scalerm*stoich, 'g-', rm8[:, 0], rm8[:, index]*scalerm*stoich, 'r-')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(h2)', transform=ax2.transAxes)

ax3=subplot(9, 6,39);
ax3.plot(cm2[:, 0], cm2[:, index]*scalecm*stoich, 'b-', cm4[:, 0], cm4[:, index]*scalecm*stoich, 'g-', cm8[:, 0], cm8[:, index]*scalecm*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(h3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

ax4=subplot(9, 6,40);
ax4.plot(to2[:, 0], to2[:, index]*scaleto*stoich, 'b-', to4[:, 0], to4[:, index]*scaleto*stoich, 'g-', to8[:, 0], to8[:, index]*scaleto*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(h4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(9, 6,41);
ax5.plot(ro2[:, 0], ro2[:, index]*scalero*stoich, 'b-', ro4[:, 0], ro4[:, index]*scalero*stoich, 'g-', ro8[:, 0], ro8[:, index]*scalero*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(h5)', transform=ax5.transAxes)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)

ax6=subplot(9, 6,42);
ax6.plot(co2[:, 0], co2[:, index]*scaleco*stoich, 'b-', co4[:, 0], co4[:, index]*scaleco*stoich, 'g-', co8[:, 0], co8[:, index]*scaleco*stoich, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(h6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)

#SOM1
index = 19
ymax = 2
ax1=subplot(9, 6,43);
ax1.plot(tm2[:, 0], tm2[:, index]*scaletm, 'b-', tm4[:, 0], tm4[:, index]*scaletm, 'g-', tm8[:, 0], tm8[:, index]*scaletm, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.yticks([0, 0.5, 1.0, 1.5])
plt.ylabel('SOM1')
plt.text(lx, ly, '(i1)', transform=ax1.transAxes)
plt.setp(ax1.get_xticklabels(), visible=False)

ax2=subplot(9, 6,44);
ax2.plot(rm2[:, 0], rm2[:, index]*scalerm, 'b-', rm4[:, 0], rm4[:, index]*scalerm, 'g-', rm8[:, 0], rm8[:, index]*scalerm, 'r-')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(i2)', transform=ax2.transAxes)

ax3=subplot(9, 6,45);
ax3.plot(cm2[:, 0], cm2[:, index]*scalecm, 'b-', cm4[:, 0], cm4[:, index]*scalecm, 'g-', cm8[:, 0], cm8[:, index]*scalecm, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(i3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

ax4=subplot(9, 6,46);
ax4.plot(to2[:, 0], to2[:, index]*scaleto, 'b-', to4[:, 0], to4[:, index]*scaleto, 'g-', to8[:, 0], to8[:, index]*scaleto, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(i4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(9, 6,47);
ax5.plot(ro2[:, 0], ro2[:, index]*scalero, 'b-', ro4[:, 0], ro4[:, index]*scalero, 'g-', ro8[:, 0], ro8[:, index]*scalero, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(i5)', transform=ax5.transAxes)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')

ax6=subplot(9, 6,48);
ax6.plot(co2[:, 0], co2[:, index]*scaleco, 'b-', co4[:, 0], co4[:, index]*scaleco, 'g-', co8[:, 0], co8[:, index]*scaleco, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.text(lx, ly, '(i6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)

#SOM2
index = 20
ymax = 3
ax1=subplot(9, 6,49);
ax1.plot(tm2[:, 0], tm2[:, index]*scaletm, 'b-', tm4[:, 0], tm4[:, index]*scaletm, 'g-', tm8[:, 0], tm8[:, index]*scaletm, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.xticks([0, 20, 40, 60])
plt.yticks([0, 1, 2])
plt.ylabel('SOM2')
plt.text(lx, ly, '(j1)', transform=ax1.transAxes)
plt.xlabel('Time (d)')

ax2=subplot(9, 6,50);
ax2.plot(rm2[:, 0], rm2[:, index]*scalerm, 'b-', rm4[:, 0], rm4[:, index]*scalerm, 'g-', rm8[:, 0], rm8[:, index]*scalerm, 'r-')
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.xticks([0, 20, 40, 60])
plt.text(lx, ly, '(j2)', transform=ax2.transAxes)
plt.xlabel('Time (d)')

ax3=subplot(9, 6,51);
ax3.plot(cm2[:, 0], cm2[:, index]*scalecm, 'b-', cm4[:, 0], cm4[:, index]*scalecm, 'g-', cm8[:, 0], cm8[:, index]*scalecm, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.xticks([0, 20, 40, 60])
plt.text(lx, ly, '(j3)', transform=ax3.transAxes)
plt.setp(ax3.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')

ax4=subplot(9, 6,52);
ax4.plot(to2[:, 0], to2[:, index]*scaleto, 'b-', to4[:, 0], to4[:, index]*scaleto, 'g-', to8[:, 0], to8[:, index]*scaleto, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.xticks([0, 20, 40, 60])
plt.text(lx, ly, '(j4)', transform=ax4.transAxes)
plt.setp(ax4.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')

ax5=subplot(9, 6,53);
ax5.plot(ro2[:, 0], ro2[:, index]*scalero, 'b-', ro4[:, 0], ro4[:, index]*scalero, 'g-', ro8[:, 0], ro8[:, index]*scalero, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.xticks([0, 20, 40, 60])
plt.text(lx, ly, '(j5)', transform=ax5.transAxes)
plt.setp(ax5.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')

ax6=subplot(9, 6,54);
ax6.plot(co2[:, 0], co2[:, index]*scaleco, 'b-', co4[:, 0], co4[:, index]*scaleco, 'g-', co8[:, 0], co8[:, index]*scaleco, 'r-')
plt.xlim([-5, 70])
plt.ylim([0, ymax])
plt.xticks([0, 20, 40, 60])
plt.text(lx, ly, '(j6)', transform=ax6.transAxes)
plt.setp(ax6.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')

plt.subplots_adjust(left=0.07, hspace=0.05, right=0.98, wspace=0.05, top=0.95, bottom=0.04)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(12, 13)
savefig('figs4.png')
savefig('figs4.pdf')
#show()
