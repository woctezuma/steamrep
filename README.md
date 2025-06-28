# SteamRep dataset

The SteamRep dataset was published by [SteamRep][steamrep-homepage] as such:

> [!NOTE]
> **SteamRep Sunset**
> 
> SteamRep sites are in the process of sunsetting. Please remove your links and API calls. Any API calls or plugins that reference steamrep.com services will cease to work at the end of August 2025.
> 
> Communities may wish to download [the CSV archive][steamrep-csv] of SteamRep and community bans and cautions.

## Data

The dataset consists of a CSV file with 53,925 rows (including the header).

Each row contains the following fields concatenated with `","` :
- `steamID64`, which [uniquely identify][steamid-doc] Steam accounts,
- `summary_rep`, either `CAUTION` or `BANNED`,
- `full_rep`, with 52 possible values, concatenated with `";"`.

`full_rep` can contain:
```
AF2 BANNED
ASBO BANNED
BAZAAR BANNED
BAZAAR CAUTION
BBG BANNED
BBG CAUTION
BPTF BANNED
BPTF CAUTION
CvG BANNED
D2T BANNED
DGN BANNED
DGN CAUTION
FoG BANNED
FoG CAUTION
FP BANNED
FP CAUTION
GoV BANNED
GoV CAUTION
HG BANNED
HG CAUTION
JAG BANNED
LZ-TRADE BANNED
MCT BANNED
R-D2TRADE BANNED
R-D2TRADE CAUTION
R-GOTRADE BANNED
R-GOTRADE CAUTION
R-TF2TRADE BANNED
R-TF2TRADE CAUTION
RAWR BANNED
REDDIT BANNED
REDDIT CAUTION
ROK BANNED
ROK CAUTION
SKIAL BANNED
SKIAL CAUTION
SMT BANNED
SMT CAUTION
SOP BANNED
SOP CAUTION
SR BANNED
SR CAUTION
TF2OP BANNED
TF2OP CAUTION
TF2R BANNED
TF2R CAUTION
TF2T BANNED
TF2T CAUTION
TF2TP BANNED
TF2TP CAUTION
UHC BANNED
UTC BANNED
```

[steamrep-homepage]: <https://steamrep.com/>
[steamrep-csv]: <https://steamrep.com/data/2024/SteamRep_Profiles_BannedCaution_2024_csv.zip>
[steamid-doc]: <https://developer.valvesoftware.com/wiki/SteamID>
