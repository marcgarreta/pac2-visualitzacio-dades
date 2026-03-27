import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import numpy as np
import networkx as nx
from collections import defaultdict

routes = [
    ("Madrid","Barcelona",4200000),  ("Madrid","Palma",3800000),
    ("Madrid","Malaga",2900000),     ("Madrid","Gran Canaria",2600000),
    ("Madrid","Tenerife Sur",2400000),("Madrid","Valencia",2100000),
    ("Madrid","Sevilla",1900000),    ("Madrid","Ibiza",1700000),
    ("Madrid","Lanzarote",1500000),  ("Madrid","Bilbao",1400000),
    ("Madrid","Alicante",1300000),   ("Madrid","Fuerteventura",1200000),
    ("Madrid","Asturias",900000),    ("Madrid","Santiago",850000),
    ("Madrid","Menorca",800000),     ("Madrid","Tenerife Norte",750000),
    ("Madrid","Vigo",600000),        ("Madrid","A Coruna",550000),
    ("Madrid","Pamplona",300000),    ("Madrid","Melilla",280000),
    ("Barcelona","Palma",3200000),   ("Barcelona","Ibiza",2100000),
    ("Barcelona","Malaga",1800000),  ("Barcelona","Gran Canaria",1400000),
    ("Barcelona","Sevilla",1200000), ("Barcelona","Tenerife Sur",1100000),
    ("Barcelona","Lanzarote",900000),("Barcelona","Valencia",850000),
    ("Barcelona","Bilbao",750000),   ("Barcelona","Alicante",700000),
    ("Barcelona","Fuerteventura",650000),("Barcelona","Menorca",600000),
    ("Barcelona","Santiago",400000), ("Barcelona","Asturias",350000),
    ("Gran Canaria","Tenerife Sur",2800000),("Gran Canaria","Lanzarote",1200000),
    ("Gran Canaria","Fuerteventura",1100000),("Gran Canaria","Tenerife Norte",900000),
    ("Palma","Ibiza",700000),        ("Palma","Menorca",650000),
    ("Sevilla","Gran Canaria",400000),("Valencia","Palma",600000),
    ("Bilbao","Palma",300000),       ("Malaga","Gran Canaria",500000),
]

groups = {
    "Madrid":"Hub principal",    "Barcelona":"Hub principal",
    "Palma":"Illes Balears",     "Ibiza":"Illes Balears",    "Menorca":"Illes Balears",
    "Gran Canaria":"Illes Canaries","Tenerife Sur":"Illes Canaries",
    "Tenerife Norte":"Illes Canaries","Lanzarote":"Illes Canaries","Fuerteventura":"Illes Canaries",
    "Valencia":"Mediterrani",    "Alicante":"Mediterrani",
    "Malaga":"Mediterrani",      "Sevilla":"Mediterrani",
    "Bilbao":"Nord",             "Asturias":"Nord",   "Santiago":"Nord",
    "A Coruna":"Nord",           "Vigo":"Nord",       "Pamplona":"Nord",
    "Melilla":"Altres",
}
palette = {
    "Hub principal":"#E63946",
    "Illes Balears":"#2A9D8F",
    "Illes Canaries":"#E9C46A",
    "Mediterrani":"#F4A261",
    "Nord":"#5B9BD5",
    "Altres":"#A8DADC",
}

conn = defaultdict(int)
for s, t, v in routes:
    conn[s] += 1
    conn[t] += 1

all_nodes = sorted(conn.keys(), key=lambda x: -conn[x])
n = len(all_nodes)
node_idx = {node: i for i, node in enumerate(all_nodes)}

# Posicions X equidistants 
xs = {node: i / (n - 1) for i, node in enumerate(all_nodes)}

# Normalitzar gruix dels arcs 
max_v = max(v for _, _, v in routes)
min_v = min(v for _, _, v in routes)

def lw(v, lo=0.4, hi=8.0):
    return lo + (v - min_v) / (max_v - min_v) * (hi - lo)

def alpha_arc(v, lo=0.25, hi=0.80):
    return lo + (v - min_v) / (max_v - min_v) * (hi - lo)

BG    = "#0d1117"
PANEL = "#161b27"

fig = plt.figure(figsize=(24, 11), facecolor=BG)
ax  = fig.add_axes([0.03, 0.18, 0.94, 0.72])   # [left, bottom, width, height]
ax.set_facecolor(PANEL)
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.04, 1.05)
ax.axis('off')

Y_BASE = 0.0   # línia base dels nodes

# Dibuixar els arcs
for s, t, v in routes:
    x0, x1 = xs[s], xs[t]
    xm = (x0 + x1) / 2
    dist = abs(x1 - x0)
    h = (dist ** 0.6) * 0.85

    color = palette[groups.get(s, "Altres")]

    theta = np.linspace(0, np.pi, 120)
    arc_x = x0 + (x1 - x0) * (1 - np.cos(theta)) / 2
    arc_y = Y_BASE + h * np.sin(theta)

    ax.plot(arc_x, arc_y,
            color=color,
            linewidth=lw(v),
            alpha=alpha_arc(v),
            solid_capstyle='round',
            zorder=1)

# Dibuixar els nodes
for node in all_nodes:
    x   = xs[node]
    grp = groups.get(node, "Altres")
    c   = palette[grp]
    ax.scatter(x, Y_BASE, s=180, color=c, zorder=5,
               edgecolors='#0d1117', linewidths=1.8)

for node in all_nodes:
    x = xs[node]
    ax.text(x, Y_BASE - 0.025, node,
            ha='right', va='top',
            fontsize=9.5,
            color='#94a3b8',
            rotation=40,
            rotation_mode='anchor',
            transform=ax.transData)

fig.text(0.5, 0.96,
         "Rutes Aèries Domèstiques a Espanya",
         ha='center', va='top',
         fontsize=20, fontweight='bold', color='white')

fig.text(0.5, 0.925,
         "Arc Diagram  ·  Principals connexions domèstiques per volum de passatgers  ·  AENA 2023\n"
         "Nodes ordenats per nombre de connexions. Gruix de l'arc = passatgers anuals.",
         ha='center', va='top',
         fontsize=11, color='#64748b', linespacing=1.6)

legend_handles = [
    mpatches.Patch(color=c, label=g)
    for g, c in palette.items()
]
legend = fig.legend(
    handles=legend_handles,
    loc='lower center',
    ncol=6,
    frameon=True,
    framealpha=0.15,
    facecolor='#1e2535',
    edgecolor='#2d3748',
    fontsize=10,
    labelcolor='#cbd5e1',
    bbox_to_anchor=(0.5, 0.01),
    handlelength=1.2,
    handleheight=0.9,
)

fig.text(0.5, 0.005,
         "Font: AENA — Estadístiques de tràfic aeri 2023  ·  PAC 2 · Visualització de Dades · MUCD · UOC",
         ha='center', va='bottom',
         fontsize=8.5, color='#374151')

out = "arc_diagram_espanya.png"
plt.savefig(out, dpi=180, bbox_inches='tight', facecolor=BG)
print(f"✅ Guardat: {out}")
plt.close()
