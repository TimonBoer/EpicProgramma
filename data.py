import tkinter as tk
window = tk.Tk()
border = tk.GROOVE
borderW = 5
BGtitle = 'gray80'
matrix = [[1, 'H', 'Waterstof', 1.00794, 0.000084, -259.1, -252.9],
          [2, 'He', 'helium', 4.002602, 0.00017, -272.2, -268.9],
          [3, 'Li', 'lithium', 6.941, 0.53, 180.5, 1317],
          [4, 'Be', 'beryllium', 9.012182, 1.85, 1278, 2970],
          [5, 'B', 'boor', 10.811, 2.46, 2300, 2550],
          [6, 'C', 'koolstof', 12.011, 3.51, 3550, 4827],
          [7, 'N', 'stikstof', 14.00674, 0.00117, -209.9, -195.8],
          [8, 'O', 'zuurstof', 15.9994, 0.00133, -218.4, -182.9],
          [9, 'F', 'fluor', 18.9984032, 0.00158, -219.6, -188.1],
          [10, 'Ne', 'neon', 20.1797, 0.00084, -248.7, -246.1],
          [11, 'Na', 'natrium', 22.989768, 0.97, 97.8, 892],
          [12, 'Mg', 'magnesium', 24.305, 1.74, 648.8, 1107],
          [13, 'Al', 'aluminium', 26.981539, 2.7, 660.5, 2467],
          [14, 'Si', 'silicium', 28.0855, 2.33, 1410, 2355],
          [15, 'P', 'fosfor', 30.973762, 1.82, 44, 280],
          [16, 'S', 'zwavel', 32.066, 2.06, 113, 444.7],
          [17, 'Cl', 'chloor', 35.4527, 0.00295, -101, -34.6],
          [18, 'Ar', 'argon', 39.948, 0.00166, -189.4, -185.9],
          [19, 'K', 'kalium', 39.0983, 0.86, 63.7, 774],
          [20, 'Ca', 'calcium', 40.078, 1.54, 839, 1487],
          [21, 'Sc', 'scandium', 44.95591, 2.99, 1539, 2832],
          [22, 'Ti', 'titanium', 47.88, 4.51, 1660, 3260],
          [23, 'V', 'vanadium', 50.9415, 6.09, 1890, 3380],
          [24, 'Cr', 'chroom', 51.9961, 7.14, 1857, 2482],
          [25, 'Mn', 'mangaan', 54.93805, 7.44, 1244, 2097],
          [26, 'Fe', 'ijzer', 55.847, 7.87, 1535, 2750],
          [27, 'Co', 'kobalt', 58.9332, 8.89, 1495, 2870],
          [28, 'Ni', 'nikkel', 58.69, 8.91, 1453, 2732],
          [29, 'Cu', 'koper', 63.546, 8.92, 1083.5, 2595],
          [30, 'Zn', 'zink', 65.39, 7.14, 419.6, 907],
          [31, 'Ga', 'gallium', 69.723, 5.91, 29.8, 2403],
          [32, 'Ge', 'germanium', 72.61, 5.32, 937.4, 2830],
          [33, 'As', 'arseen', 74.92159, 5.72, 613, 613],
          [34, 'Se', 'seleen', 78.96, 4.82, 217, 685],
          [35, 'Br', 'broom', 79.904, 3.14, -7.3, 58.8],
          [36, 'Kr', 'krypton', 83.8, 0.00348, -156.6, -152.3],
          [37, 'Rb', 'rubidium', 85.4678, 1.53, 39, 688],
          [38, 'Sr', 'strontium', 87.62, 2.63, 769, 1384],
          [39, 'Y', 'yttrium', 88.90585, 4.47, 1523, 3337],
          [40, 'Zr', 'zirkonium', 91.224, 6.51, 1852, 4377],
          [41, 'Nb', 'niobium', 92.90638, 8.58, 2468, 4927],
          [42, 'Mo', 'molybdeen', 95.94, 10.28, 2617, 5560],
          [43, 'Tc', 'technetium', 98.9063, 11.49, 2172, 5030],
          [44, 'Ru', 'ruthenium', 101.07, 12.45, 2310, 3900],
          [45, 'Rh', 'rodium', 102.9055, 12.41, 1966, 3727],
          [46, 'Pd', 'palladium', 106.42, 12.02, 1552, 3140],
          [47, 'Ag', 'zilver', 107.8682, 10.49, 961.9, 2212],
          [48, 'Cd', 'cadmium', 112.411, 8.64, 321, 765],
          [49, 'In', 'indium', 114.82, 7.31, 156.2, 2080],
          [50, 'Sn', 'tin', 118.71, 7.29, 232, 2270],
          [51, 'Sb', 'antimoon', 121.75, 6.69, 630.7, 1750],
          [52, 'Te', 'telluur', 127.6, 6.25, 449.6, 990],
          [53, 'I', 'jood', 126.90447, 4.94, 113.5, 184.4],
          [54, 'Xe', 'xenon', 131.29, 0.00449, -111.9, -107],
          [55, 'Cs', 'cesium', 132.90543, 1.9, 28.4, 690],
          [56, 'Ba', 'barium', 137.327, 3.65, 725, 1640],
          [57, 'La', 'lanthaan', 138.9055, 6.16, 920, 3454],
          [58, 'Ce', 'cerium', 140.115, 6.77, 798, 3257],
          [59, 'Pr', 'praseodymium', 140.90765, 6.48, 931, 3212],
          [60, 'Nd', 'neodymium', 144.24, 7, 1010, 3127],
          [61, 'Pm', 'promethium', 146.9151, 7.22, 1080, 2730],
          [62, 'Sm', 'samarium', 150.36, 7.54, 1072, 1778],
          [63, 'Eu', 'europium', 151.965, 5.25, 822, 1597],
          [64, 'Gd', 'gadolinium', 157.25, 7.89, 1311, 3233],
          [65, 'Tb', 'terbium', 158.92534, 8.25, 1360, 3041],
          [66, 'Dy', 'dysprosium', 162.5, 8.56, 1409, 2335],
          [67, 'Ho', 'holmium', 164.93032, 8.78, 1470, 2720],
          [68, 'Er', 'erbium', 167.26, 9.05, 1522, 2510],
          [69, 'Tm', 'thulium', 168.93421, 9.32, 1545, 1727],
          [70, 'Yb', 'ytterbium', 173.04, 6.97, 824, 1193],
          [71, 'Lu', 'lutetium', 174.967, 9.84, 1656, 3315],
          [72, 'Hf', 'hafnium', 178.49, 13.31, 2150, 5400],
          [73, 'Ta', 'tantaal', 180.9479, 16.68, 2996, 5425],
          [74, 'W', 'wolfraam', 183.85, 19.26, 3407, 5927],
          [75, 'Re', 'renium', 186.207, 21.03, 3180, 5627],
          [76, 'Os', 'osmium', 190.2, 22.61, 3045, 5027],
          [77, 'Ir', 'iridium', 192.22, 22.65, 2410, 4130],
          [78, 'Pt', 'platina', 195.08, 21.45, 1772, 3827],
          [79, 'Au', 'goud', 196.96654, 19.32, 1064.4, 2940],
          [80, 'Hg', 'kwik', 200.59, 13.55, -38.9, 356.6],
          [81, 'Tl', 'thallium', 204.3833, 11.85, 303.6, 1457],
          [82, 'Pb', 'lood', 207.2, 11.34, 327.5, 1740],
          [83, 'Bi', 'bismut', 208.98037, 9.8, 271.4, 1560],
          [84, 'Po', 'polonium', 208.9824, 9.2, 254, 962],
          [85, 'At', 'astaat', 209.9871, 6.35, 302, 337],
          [86, 'Rn', 'radon', 222.0176, 0.00923, -71, -61.8],
          [87, 'Fr', 'francium', 223.0197, 2.9, 27, 677],
          [88, 'Ra', 'radium', 226.0254, 5.5, 700, 1140],
          [89, 'Ac', 'actinium', 227.0278, 10.07, 1047, 3197],
          [90, 'Th', 'thorium', 232.0381, 11.72, 1750, 4787],
          [91, 'Pa', 'protactinium', 231.0359, 15.37, 1554, 4030],
          [92, 'U', 'uranium', 238.0289, 18.97, 1132.4, 3818],
          [93, 'Np', 'neptunium', 237.0482, 20.48, 640, 3902],
          [94, 'Pu', 'plutonium', 244.0642, 19.74, 641, 3327],
          [95, 'Am', 'americium', 243.0614, 13.67, 994, 2607],
          [96, 'Cm', 'curium', 247.0703, 13.51, 1340, 3110],
          [97, 'Bk', 'berkelium', 247.0703, 13.25, 986, 2627],
          [98, 'Cf', 'californium', 251.0796, 15.1, 900, 1470],
          [99, 'Es', 'einsteinium', 252.0829, 8.84, 860, 996],
          [100, 'Fm', 'fermium', 257.0951, 9.71, 1527, ''],
          [101, 'Md', 'mendelevium', 258.0986, 10.37, 827, ''],
          [102, 'No', 'nobelium', 259.1009, 9.94, 827, ''],
          [103, 'Lr', 'lawrencium', 260.1053, 16.1, 1627, ''],
          [104, 'Rf', 'rutherfordium', 261.1087, 23.2, 2100, 5500],
          [105, 'Db', 'dubnium', 262.1138, 29.3, '', ''],
          [106, 'Sg', 'seaborgium', 263.1182, 35, '', ''],
          [107, 'Bh', 'bohrium', 262.1229, 37.1, '', ''],
          [108, 'Hs', 'hassium', 265, 41, '', ''],
          [109, 'Mt', 'meitnerium', 266, 37.4, '', ''],
          [110, 'Ds', 'darmstadtium', 269, 34.8, '', ''],
          [111, 'Rg', 'röntgenium', 272, 28.7, '', ''],
          [112, 'Cn', 'copernicium', 277, 23.7, '', ''],
          [113, 'Nh', 'nihonium', 284, 16, 430, 1130],
          [114, 'Fl', 'flerovium', 289, 14, '', -60],
          [115, 'Mc', 'moscovium', 295, 13.5, 400, 1100],
          [116, 'Lv', 'livermorium', 297, 12.9, 435.5, 812],
          [117, 'Ts', 'tennessine', 291, 7.2, 450, 610],
          [118, 'Og', 'oganesson', 293, 5, '', 80],
          [119, 'Uue', 'eka-francium', '', '', '', ''],
          [120, 'Ubn', 'eka-radium', '', '', '', ''],
          [121, 'Ubu', 'eka-actinium', '', '', '', ''],
          [122, 'Ubb', 'eka-thorium', '', '', '', ''],
          [123, 'C6H12O6', 'Glucose', 180.1577, 1.56, 146, ''],
          [124, 'H2O2', 'waterstofperoxide', 34.01468, 1.45, -0.41, 150.2],
          [125, 'HCl', 'waterstofchloride', 36.46, 0.00149, -114.8, -85],
          [126, 'O2', 'zuurstof (molecuul)', 31.999, 0.001429, -218.2, -182.8],
          [127, 'H2', 'waterstof (molecuul)', 2.01588, 0.00008988, -258.99, -252.72],
          [128, 'H2O', 'water', 18.01528, 0.997, 0, 100],
          [129, 'N2', 'stikstof (molecuul)', 28.01348, 0.0012506, -209.7, -195.6],
          [130, 'C3H8', 'propaan', 44.09652, 0.493, -188, -42],
          [131, 'CO2', 'koolstofdioxide', 44.0098, 0.00198, -57, -78.46],
          [132, 'C2H4', 'Etheen', 28.05376, 0.00118, -169.15, -103.71],
          [133, 'NH3', 'Ammoniak', 17.03056, 0.000717, -78, -33],
          [134, 'N2H4', 'Hydrazine', 32.04524, 1.01, 1.4, 113.5],
          [135, 'C4H10', 'Butaan', 58.1234, 0.573, -138.35, -1],
          [136, 'CH4', 'Methaan', 16.04276, 0.000656, -182, -164],
          [137, 'C2H5OH', 'Ethanol', 46.06904, 0.000789, -114.1, 78.37]]
cijfers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
frameRow2 = tk.Frame(master=window)
frameRow3 = tk.Frame(master=window)
frameRow4 = tk.Frame(master=window)