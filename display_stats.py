import csv
from pathlib import Path

FNAME = "data/SteamRep_Profiles_BannedCaution_2024.csv"
FLAG_SEPARATOR = ";"


def main() -> None:
    steam_ids = set()
    summary_rep = set()
    full_rep = set()

    with Path(FNAME).open() as f:
        steamrep_reader = csv.reader(f)

        next(steamrep_reader)  # Skip the header row

        for row in steamrep_reader:
            steam_ids.add(row[0])
            summary_rep.add(row[1])

            for flag in row[2].split(FLAG_SEPARATOR):
                full_rep.add(flag)

    print(f"Steam IDs: {len(steam_ids)}")
    print(f"Summary Reputation: {len(summary_rep)} -> {summary_rep}")
    print(f"Full Reputation: {len(full_rep)} -> {sorted(full_rep)}")


if __name__ == "__main__":
    main()
