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

Each row contains:
- `steamID64`, which [uniquely identify][steamid-doc] Steam accounts,
- `summary_rep`, either 'CAUTION' or 'BANNED',
- `full_rep`.

[steamrep-homepage]: <https://steamrep.com/>
[steamrep-csv]: <https://steamrep.com/data/2024/SteamRep_Profiles_BannedCaution_2024_csv.zip>
[steamid-doc]: <https://developer.valvesoftware.com/wiki/SteamID>
