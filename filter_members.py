from src.discord_utils import get_steam_ids_from_discord
from src.steamrep_utils import get_steam_ids_from_steamrep
from src.utils import compute_intersection


def main() -> None:
    steam_ids = get_steam_ids_from_discord()
    banned_steam_ids, warned_steam_ids = get_steam_ids_from_steamrep()

    compute_intersection(steam_ids, banned_steam_ids)
    compute_intersection(steam_ids, warned_steam_ids)


if __name__ == "__main__":
    main()
