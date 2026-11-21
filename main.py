import os

JOKE = "It fixed the crash by deleting code that reported it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
