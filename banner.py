def banner(title, author):
    title_length = len(title)
    byline = f"By {author}"
    byline_length = len(byline)
    banner_length = max(title_length, byline_length) + 8
    print("=" * banner_length)
    print(f"{title:^{banner_length}}")
    print(f"{byline:^{banner_length}}")
    print(f"{'=' * banner_length}")
    print("")


if __name__ == "__main__":
    banner("BANNER", "Samuel")
    name = input("What is your name? ")
    title = input("What is your quest? ")
    banner(title, author)