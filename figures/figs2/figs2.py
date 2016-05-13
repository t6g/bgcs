import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

sm2 = np.loadtxt('../../simulations/solubility_co2s/sol2.txt', skiprows=2)
s04 = np.loadtxt('../../simulations/solubility_co2s/sol4.txt', skiprows=2)
s08 = np.loadtxt('../../simulations/solubility_co2s/sol8.txt', skiprows=2)
s25 = np.loadtxt('../../simulations/solubility_co2s/sol25.txt', skiprows=2)
plt.plot(sm2[:, 0], sm2[:, 4], 'r:',  s04[:, 0], s04[:, 4], 'r-.',  s08[:, 0], s08[:, 4], 'r--',  s25[:, 0], s25[:, 4], 'r-')
plt.plot(sm2[:, 0], sm2[:, 1], 'b:',  sm2[:, 0], sm2[:, 2], 'k:', sm2[:, 0], sm2[:, 3], 'g:',  sm2[:, 0], sm2[:, 4], 'r:',  sm2[:, 0], sm2[:, 5], 'm:')
plt.plot(s04[:, 0], s04[:, 1], 'b-.', s04[:, 0], s04[:, 2], 'k-.', s04[:, 0], s04[:, 3], 'g-.', s04[:, 0], s04[:, 4], 'r-.', s04[:, 0], s04[:, 5], 'm-.')
plt.plot(s08[:, 0], s08[:, 1], 'b--', s08[:, 0], s08[:, 2], 'k--', s08[:, 0], s08[:, 3], 'g--', s08[:, 0], s08[:, 4], 'r--', s08[:, 0], s08[:, 5], 'm--')
plt.plot(s25[:, 0], s25[:, 1], 'b-',  s25[:, 0], s25[:, 2], 'k-', s25[:, 0], s25[:, 3], 'g-',  s25[:, 0], s25[:, 4], 'r-',  s25[:, 0], s25[:, 5], 'm-')
lgd = plt.legend(('-2$^\circ$C', ' 4$^\circ$C', ' 8$^\circ$C', '25$^\circ$C'),loc=5)
lgd.draw_frame(False)
lgt = lgd.get_texts()
plt.setp(lgt, fontsize='small')
plt.xlabel('pH')
plt.ylabel('%')
plt.ylim([0, 105])
plt.text(4.5, 80, 'CO$_2$(s)', color='k')
plt.text(4.5, 30, 'CO$_2$(g)', color='b')
plt.text(4.5, 20, 'CO$_2$(aq)', color='g')
plt.text(8.5, 10, 'CO${_3}^{2-}$', color='m')
plt.text(8.2, 87, 'HCO${_3}^-$', color='r')

plt.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.15)
fig.set_size_inches(5, 4)
plt.savefig('figs2.pdf')
plt.savefig('figs2.png')
plt.show()
