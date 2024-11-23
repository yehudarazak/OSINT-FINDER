import argparse
from quick_osint.domain import fetch_whois, fetch_dns_records
from quick_osint.email import check_breach
from quick_osint.username import search_username

def main():
    parser = argparse.ArgumentParser(description="Quick OSINT CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Domain subcommand
    domain_parser = subparsers.add_parser("domain", help="Fetch domain information")
    domain_parser.add_argument("domain", help="Domain to fetch information for")

    # Email subcommand
    email_parser = subparsers.add_parser("email", help="Check email breach status")
    email_parser.add_argument("email", help="Email address to check")

    # Username subcommand
    username_parser = subparsers.add_parser("username", help="Search for a username on social media platforms")
    username_parser.add_argument("username", help="Username to search for")
    username_parser.add_argument("platform", help="Platform to search on (e.g., twitter, instagram, github)")

    args = parser.parse_args()

    if args.command == "domain":
        print("Fetching WHOIS information...")
        whois_data = fetch_whois(args.domain)
        print(whois_data)

        print("\nFetching DNS records...")
        dns_records = fetch_dns_records(args.domain)
        print(dns_records)

    elif args.command == "email":
        print("Checking email breaches...")
        result = check_breach(args.email)
        print(result["message"])

    elif args.command == "username":
        print(f"Searching for username '{args.username}' on {args.platform}...")
        result = search_username(args.username, args.platform)
        print(result["message"])

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
