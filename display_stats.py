from src.steamrep_utils import get_steam_ids_from_steamrep

FLAG_SEPARATOR = ";"


def main() -> None:
    banned_steam_ids, warned_steam_ids = get_steam_ids_from_steamrep()

    steam_ids = set(banned_steam_ids.keys()).union(warned_steam_ids.keys())

    full_rep = set()
    for d in [banned_steam_ids, warned_steam_ids]:
        for v in d.values():
            for flag in v.split(FLAG_SEPARATOR):
                full_rep.add(flag)

    print(f"Steam IDs: {len(steam_ids)}")
    print(f"Full Reputation: {len(full_rep)} -> {sorted(full_rep)}")


if __name__ == "__main__":
    main()
