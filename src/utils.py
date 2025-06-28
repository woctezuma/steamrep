FOLDER_NAME = "data"


def compute_intersection(
    steam_ids: dict[str, str],
    banned_steam_ids: dict[str, str],
) -> set[str]:
    detected = set(steam_ids).intersection(banned_steam_ids)
    print(f"Detected: {len(detected)}")

    for i in detected:
        print(f"1. <@{steam_ids[i]}> -> {banned_steam_ids[i]}")

    return detected
