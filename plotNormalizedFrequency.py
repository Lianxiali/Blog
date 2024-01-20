import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import cm

import scienceplots
plt.style.use(["science"])

color = iter(cm.rainbow(np.linspace(0, 1, 9)))

df = pd.read_excel(r'NormalizedFrequency.xlsx', sheet_name='Sheet2')

f1 = df.iloc[1:12, 0]
Anh02 = df.iloc[1:12, 2]
Anh03 = df.iloc[1:12, 4]
Anh04= df.iloc[1:12, 6]
Anh05 = df.iloc[1:12, 8]
plt.plot(f1, Anh02, color = next(color), marker='^', fillstyle = 'none', ls = '--', label=rf"$A_e/D = 0.2 $ (Anh-Hung) ", antialiased=True)
plt.plot(f1, Anh03, color = next(color), marker='s', fillstyle = 'none', ls = '--', label=rf"$A_e/D = 0.3 $ (Anh-Hung) ", antialiased=True)
plt.plot(f1, Anh04, color = next(color), marker='p', fillstyle = 'none', ls = '--', label=rf"$A_e/D = 0.4 $ (Anh-Hung) ", antialiased=True)
plt.plot(f1, Anh05, color = next(color), marker='o', fillstyle = 'none', ls = '--', label=rf"$A_e/D = 0.5 $ (Anh-Hung) ", antialiased=True)

f2 = df.iloc[1:9, 14]
chylan = df.iloc[1:9, 15]
plt.plot(f2, chylan, color = next(color), marker='x', ls = '--', label=rf"$A_e/D = 0.3 $ (Cheylan) ", antialiased=True)

f3 = df.iloc[17:24, 0]
ibm02 = df.iloc[17:24, 1]
ibm03 = df.iloc[17:24, 3]
ibm04 = df.iloc[17:24, 5]
ibm05 = df.iloc[17:24, 7]
plt.plot(f3, ibm02, color = next(color), marker='^', ls = '-', label=rf"$A_e/D = 0.2 $ (Present) ", antialiased=True)
plt.plot(f3, ibm03, color = next(color), marker='s', ls = '-', label=rf"$A_e/D = 0.3 $ (Present) ", antialiased=True)
plt.plot(f3, ibm04, color = next(color), marker='p', ls = '-', label=rf"$A_e/D = 0.4 $ (Present) ", antialiased=True)
plt.plot(f3, ibm05, color = next(color), marker='o', ls = '-', label=rf"$A_e/D = 0.5 $ (Present) ", antialiased=True)

plt.xlabel(r"$f_r$")
plt.ylabel(r"$f_s/f_o$")
plt.axis('square')

plt.tight_layout()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


plt.show()
