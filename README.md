
```markdown
# PCB Bill of Materials (BOM) Parser

An automated Python utility designed to clean, categorize, and validate raw Bill of Materials (BOM) exports from standard PCB CAD software. This tool eliminates the manual overhead of sorting components and proactively flags missing manufacturing data to prevent ordering errors.

## 🚀 Features
* **Intelligent Categorization:** Automatically identifies component types (Resistors, Capacitors, ICs, Diodes, etc.) using regex to parse reference designators.
* **Data Sanitization:** Strips trailing whitespaces, normalizes headers, and formats messy CSV exports into clean, readable data structures.
* **Manufacturing Validation:** Scans for missing Manufacturer Part Numbers (MPNs) and aggressively flags incomplete components to ensure manufacturing readiness.
* **Zero Dependencies:** Built entirely with Python's standard libraries (`csv`, `re`, `os`). No external packages or virtual environments required.

## 📂 Repository Structure
```text
PCB-BOM-Parser/
├── data/
│   ├── raw_bom.csv      # Input: Unformatted export from CAD software
│   └── clean_bom.csv    # Output: Generated automatically after execution
├── main.py              # Core parsing and categorization logic
└── README.md            # Project documentation

```

## ⚙️ Prerequisites

* **Python 3.x:** Ensure Python is installed and added to your system's PATH.

## 🛠️ Quick Start & Execution

1. **Clone the repository:**
```bash
git clone [https://github.com/Uchchhas4G3NT52/PCB-BOM-Parser.git](https://github.com/Uchchhas4G3NT52/PCB-BOM-Parser.git)

```


2. **Navigate to the project directory:**
```bash
cd PCB-BOM-Parser

```


3. **Provide your data:**
Place your unformatted BOM export into the `data/` folder and name it `raw_bom.csv`. Ensure it contains basic column headers like `Designator`, `Value`, and `PartNumber`.
4. **Execute the script:**
```bash
python main.py

```



## 📊 Example Workflow

**Input (`raw_bom.csv`):** Messy, unsorted, and missing crucial part numbers.

```csv
Designator, Value, Footprint, Manufacturer, PartNumber
R1, 10k, 0402, Yageo, RC0402JR-0710KL
C1, 0.1uF, 0603, Murata, GRM188R71C104KA01D
U1, NE555, SOIC-8, TI, NE555DR
R2, 4.7k, 0402, Vishay, 

```

**Output (`clean_bom.csv`):** Sorted logically by component type, with clear visual flags for missing data.

```csv
Type,Designator,Value,Footprint,PartNumber
Capacitor,C1,0.1uF,0603,GRM188R71C104KA01D
Integrated Circuit,U1,NE555,SOIC-8,NE555DR
Resistor,R1,10k,0402,RC0402JR-0710KL
Resistor,R2,4.7k,0402,⚠️ MISSING_MPN

```

```

**How to add this to your new repository:**
1. Create a new repository on GitHub named `PCB-BOM-Parser`.
2. Click **"Add a README"** or the pencil icon if one was auto-generated.
3. Paste the markdown code above into the text box.
4. Click **"Commit changes..."** to publish it.

```
