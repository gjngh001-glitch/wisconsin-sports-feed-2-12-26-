base = args.fallback_base_url.rstrip("/") if args.fallback_base_url else ""

logo_urls = {}
if base:
    logo_urls = {
        "Packers": f"{base}/img/packers.jpg",
        "Bucks": f"{base}/img/bucks.jpg",
        "Brewers": f"{base}/img/brewers.jpg",
        "Badgers": f"{base}/img/badgers.jpg",
        "Wisconsin": f"{base}/img/badgers.jpg",
    }
