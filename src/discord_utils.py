import json
from pathlib import Path

DISCORD_FNAME = "data/profiles.json"


def load_discord_profiles() -> dict:
    with Path(DISCORD_FNAME).open("r") as file:
        return json.load(file)


def get_steam_ids_from_discord(*, verbose: bool = True) -> dict[str, str]:
    profiles = load_discord_profiles()

    steam_ids = {}
    for discord_id, discord_data in profiles.items():
        steam_id = discord_data.get("connections", {}).get("steam", {}).get("id")
        if steam_id:
            steam_ids[steam_id] = discord_id

    if verbose:
        print(f"Steam IDs: {len(steam_ids)} on Discord")

    return steam_ids
