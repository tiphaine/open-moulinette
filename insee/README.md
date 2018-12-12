## Data for IRIS

This script downloads and concatenates all the features from many Insee's files in one clean csv (more than 1700 actually).

For some files, we add a feature `nb_name_of_feature` which is an aggregate of all features (example: sum all medical jobs).

The size of the output is 750 Mo.

## Dependency

- Python 3
- Pandas
- xlrd

You can install the dependencies with `pip install pandas xlrd`.

## Usage

- `make` : to automatically install dependencies, download files and process to the output csv
- `make install` : install python dependencies
- `make download` : download all files
- `make convert` : process to the concatenation and extract csv

## Format

The generated `output.csv` file will look like this:


```csv
CODGEO;LIBGEO;COM;LIBCOM;REG;DEP;ARR;CV;ZE2010;UU2010;NB_B101
010040101;Les Perouses-Triangle d'Activite;01004;Ambérieu-en-Bugey;82;01;011;0101;8201;01302;0;2;
010040102;Longeray-Gare;01004;Ambérieu-en-Bugey;82;01;011;0101;8201;01302;0;2;
010040201;Centre-St Germain-Vareilles;01004;Ambérieu-en-Bugey;82;01;011;0101;8201;01302;0;0;
```

## Reuse

Read the data in a pandas dataframe.

```
import pandas as pd
data = pd.read_csv('data/output.csv', sep=";")
```


