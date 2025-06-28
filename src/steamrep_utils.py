import csv
from pathlib import Path

from src.utils import FOLDER_NAME

STEAMREP_FNAME = f"{FOLDER_NAME}/SteamRep_Profiles_BannedCaution_2024.csv"


def get_steam_ids_from_steamrep(
    *,
    verbose: bool = True,
) -> tuple[dict[str, str], dict[str, str]]:
    banned_steam_ids = {}
    warned_steam_ids = {}

    with Path(STEAMREP_FNAME).open() as f:
        steamrep_reader = csv.reader(f)

        next(steamrep_reader)  # Skip the header row

        for row in steamrep_reader:
            if row[1] == "BANNED":
                banned_steam_ids[row[0]] = row[2]
            elif row[1] == "CAUTION":
                warned_steam_ids[row[0]] = row[2]
            else:
                msg = f"Unexpected status '{row[1]}' for Steam ID {row[0]}"
                raise ValueError(
                    msg,
                )

    if verbose:
        print(
            f"{len(banned_steam_ids)} banned and {len(warned_steam_ids)} warned",
        )

    return banned_steam_ids, warned_steam_ids
