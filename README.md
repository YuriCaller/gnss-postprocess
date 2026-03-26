# gnss-postprocess
QGIS plugin for GNSS PPK/PPP post-processing with RTKLIB
[README.md](https://github.com/user-attachments/files/26282639/README.md)
# GNSS Post-Process PPK/PPP

**QGIS Plugin** for professional GNSS post-processing (PPK and PPP) using RTKLIB.  
Designed for forestry, cadastre and topography professionals in Peru and Latin America.

**Author:** Ing. Yuri Fabian Caller Cordova — CIP 214377  
**Version:** 2.0.0 | **QGIS:** ≥ 3.16

---

## Features

- **PPK** (Post-Processing Kinematic) — differential correction with base/rover RINEX files
- **PPP** (Precise Point Positioning) — single-receiver precise positioning via RTKLIB
- **IGN Peru-style technical data sheet** — UTM, Geographic and Cartesian coordinates via `pyproj`
- **PDF fidelity reports** — coordinate traceability and correction tracking via `reportlab`
- **Strict geodetic base validation** — automated checks on base station quality
- **Multi-format export** — SHP, GPKG, KML, GeoJSON
- **Modular architecture** — independent engines for PPK, PPP, validation, reports and export

---

## Requirements

| Dependency | Version | Purpose |
|---|---|---|
| QGIS | ≥ 3.16 | Platform |
| RTKLIB | 2.4.3 | GNSS processing engine (auto-installed) |
| pyproj | ≥ 3.0 | Coordinate transformations |
| reportlab | ≥ 3.6 | PDF report generation |

> RTKLIB binaries are downloaded automatically on first use via the built-in installer.

---

## Installation

### From QGIS Plugin Repository
1. Open QGIS → **Plugins → Manage and Install Plugins**
2. Search for `GNSS Post-Process PPK/PPP`
3. Click **Install**

### Manual Installation
1. Download the latest release ZIP from [Releases](https://github.com/YuriCaller/gnss-postprocess/releases)
2. In QGIS: **Plugins → Manage and Install Plugins → Install from ZIP**
3. Select the downloaded file and click **Install Plugin**

---

## Usage

1. After installation, the plugin appears in the **GNSS Post-Process** menu and toolbar
2. Click the icon to open the processing panel (dockable, right side)
3. Select your workflow: **PPK** or **PPP**
4. Load your RINEX observation and navigation files
5. For PPK: also load the base station file and enter its precise coordinates
6. Run processing — results are automatically loaded as a QGIS layer
7. Generate PDF report and export to your preferred format

---

## Project Structure

```
gnss_postprocess/
├── __init__.py               # Plugin entry point
├── plugin_main.py            # QGIS plugin class
├── metadata.txt              # Plugin metadata
├── icons/
│   └── icon.png              # Plugin icon
├── gnss_engine/
│   ├── ppk_processor.py      # PPK processing via RTKLIB
│   ├── ppp_processor.py      # PPP processing via RTKLIB
│   ├── config_builder.py     # RTKLIB configuration builder
│   └── coord_converter.py    # UTM/Geographic/Cartesian conversions
├── validators/
│   ├── base_validator.py     # Base station quality checks
│   ├── ppk_validator.py      # PPK input validation
│   └── ppp_validator.py      # PPP input validation
├── results/
│   ├── pos_parser.py         # RTKLIB .pos file parser
│   └── layer_builder.py      # QGIS vector layer builder
├── reports/
│   ├── pdf_report.py         # PDF fidelity report (reportlab)
│   └── html_report.py        # HTML summary report
├── export/
│   └── csv_exporter.py       # CSV/SHP/GPKG/KML/GeoJSON export
├── ui/
│   └── main_dialog.py        # Main processing panel (PyQt5)
└── rtklib_bin/               # RTKLIB binaries (auto-populated)
```

---

## Workflow Diagram

```
RINEX Files (Base + Rover)
        │
        ▼
  Input Validation
  (base_validator / ppk_validator)
        │
        ▼
  RTKLIB Processing
  (rnx2rtkp / rtkpost)
        │
        ▼
  Result Parsing (.pos)
  (pos_parser)
        │
        ├──► QGIS Layer (layer_builder)
        ├──► PDF Report (pdf_report)
        └──► Export SHP/GPKG/KML/GeoJSON (csv_exporter)
```

---

## Changelog

### v2.0.0 (2026-03-24)
- Complete rewrite with modular architecture
- PPK and PPP support via RTKLIB
- Strict geodetic base validation (UTM + Geographic + Cartesian)
- IGN Peru-style technical data sheet
- PDF fidelity reports with reportlab
- Export to SHP, GPKG, KML, GeoJSON
- Coordinate traceability and correction tracking

---

## License

This plugin is distributed under the **GNU General Public License v2** or later.  
See [LICENSE](LICENSE) for details.

---

## Contact

**Ing. Yuri Fabian Caller Cordova — CIP 214377**  
GIS Specialist | Forestry & Territorial Management | Madre de Dios, Peru  
📧 yuricaller@gmail.com  
🐛 [Report an issue](https://github.com/YuriCaller/gnss-postprocess/issues)
