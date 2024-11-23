import whois
import dns.resolver

def fetch_whois(domain):
    """Fetch WHOIS information for a domain."""
    try:
        data = whois.whois(domain)
        return data
    except Exception as e:
        return {"error": f"Failed to fetch WHOIS data: {e}"}

def fetch_dns_records(domain):
    """Fetch DNS records for a domain."""
    try:
        records = {}
        for record_type in ['A', 'MX', 'NS', 'TXT']:
            answers = dns.resolver.resolve(domain, record_type, raise_on_no_answer=False)
            records[record_type] = [str(answer) for answer in answers]
        return records
    except Exception as e:
        return {"error": f"Failed to fetch DNS records: {e}"}

