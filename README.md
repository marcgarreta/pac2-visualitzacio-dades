# Arc Diagram — Rutes Aèries Domèstiques a Espanya

Visualització creada per a la **PAC 2** de l'assignatura de Visualització de Dades  
**Màster Universitari de Ciència de Dades · UOC**

## Descripció

Arc Diagram que representa les principals connexions de vols domèstics espanyols  
per volum de passatgers (AENA 2023).

- **21 nodes** — aeroports espanyols, ordenats per nombre de connexions
- **44 arcs** — rutes domèstiques; el gruix codifica els passatgers anuals
- **Colors** — identifiquen el grup geogràfic de l'aeroport origen

## Visualització en línia

👉 [Veure la visualització](https://[el-teu-usuari].github.io/pac2-visualitzacio-dades/)

## Reproduir localment

### 1. Clona el repositori
```bash
git clone https://github.com/[el-teu-usuari]/pac2-visualitzacio.git
cd pac2-visualitzacio-dades
```

### 2. Crea un entorn virtual (recomanat)
```bash
python3 -m venv venv
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows
```

### 3. Instal·la les dependències
```bash
pip install -r requirements.txt
```

### 4. Executa l'script
```bash
python3 arc_diagram_final.py
```

Genera el fitxer `arc_diagram_espanya.png` a la carpeta actual.

## Dependències

| Llibreria | Versió mínima | Ús |
|---|---|---|
| `matplotlib` | 3.7.0 | Dibuix del gràfic |
| `numpy` | 1.24.0 | Càlcul de les corbes dels arcs |
| `networkx` | 3.0 | Gestió de l'estructura del graf |

## Font de dades

- **AENA** — Estadístiques de tràfic aeri 2023
- Dades obertes · [aena.es/es/estadisticas.html](https://www.aena.es/es/estadisticas.html)

## Llicència

CC BY 4.0 — Lliure ús amb atribució
