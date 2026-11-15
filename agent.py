#!/usr/bin/env python3
"""
lead-research-agent -- build a structured lead sheet for a company (DEMO DATA ONLY).

This agent does NOT scrape any real website and does NOT call any API.
It builds a lead sheet from the company name + website you give it, using
built-in demo rules and templates (industry guessed from keywords in the name).

Usage:
    python agent.py --demo
    python agent.py --company "SliceHouse Pizza" --website "https://slicehouse.example"
    python agent.py --company "SliceHouse Pizza" --website "https://slicehouse.example" --save
"""

import argparse
import sys

# keyword -> (industry, likely needs, outreach angle)
INDUSTRY_RULES = [
    (["pizza", "restaurant", "cafe", "coffee", "bakery", "food", "burger", "diner"],
     "Food & Beverage / Restaurant",
     ["online ordering", "WhatsApp order taking", "customer replies after hours"],
     "Offer a WhatsApp ordering assistant that takes orders, confirms them, and answers menu questions automatically."),
    (["tech", "software", "app", "saas", "it ", "digital", "cloud", "data"],
     "Technology / Software",
     ["lead follow-up", "support ticket triage", "demo booking"],
     "Offer an AI agent that qualifies inbound leads and books demos while the team is offline."),
    (["clinic", "hospital", "dental", "medical", "health", "pharmacy"],
     "Healthcare",
     ["appointment booking", "patient reminders", "answering common questions"],
     "Offer an appointment-booking assistant that answers patient questions and sends reminders."),
    (["school", "academy", "college", "institute", "tuition", "education"],
     "Education",
     ["admission enquiries", "student support", "fee reminders"],
     "Offer an enquiry-handling assistant that answers admission questions instantly."),
    (["shop", "store", "retail", "mart", "boutique", "fashion"],
     "Retail",
     ["order updates", "product questions", "abandoned-cart follow-up"],
     "Offer a support assistant that answers product questions and sends order updates automatically."),
    (["gym", "fitness", "salon", "spa", "beauty"],
     "Health & Wellness",
     ["class bookings", "membership questions", "reminders"],
     "Offer a booking assistant that handles class bookings and membership questions."),
]

GENERIC = (
    "General / Small Business",
    ["replying to customer messages", "follow-up", "booking/scheduling"],
    "Offer a simple AI assistant that replies to common customer messages instantly and hands over to a human when needed.",
)


def guess_industry(company, website):
    """Guess the industry from keywords in the company name + website."""
    text = (company + " " + website).lower()
    for keywords, industry, needs, angle in INDUSTRY_RULES:
        if any(kw in text for kw in keywords):
            return industry, needs, angle
    return GENERIC


def build_lead_sheet(company, website):
    industry, needs, angle = guess_industry(company, website)
    lines = [
        "# Lead Sheet (Demo Data Only)",
        "",
        "This lead sheet is generated from built-in demo rules. No website was scraped and no real data was fetched.",
        "",
        f"**Company:** {company}",
        f"**Website:** {website}",
        f"**Industry (guessed from name):** {industry}",
        "",
        "## Likely needs",
    ]
    for need in needs:
        lines.append(f"- {need}")
    lines += [
        "",
        "## Suggested outreach angle",
        angle,
        "",
        "## Next steps",
        "1. Verify the company is real and find a real contact person (owner/manager).",
        "2. Check their current website / social pages for what they already automate.",
        "3. Send a short, personal message using the outreach angle above.",
        "4. Offer a small free demo before discussing price.",
        "",
        "## Notes",
        "- Demo data only: industry, needs and angle are guesses from keywords, not research.",
        "- Do not treat this as verified company information.",
    ]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Build a lead sheet from demo rules (no scraping, no API).")
    parser.add_argument("--company", help="Company name, e.g. 'SliceHouse Pizza'.")
    parser.add_argument("--website", default="", help="Company website URL.")
    parser.add_argument("--save", action="store_true", help="Also save the lead sheet to lead_sheet.md.")
    parser.add_argument("--demo", action="store_true", help="Run with the sample company SliceHouse Pizza.")
    args = parser.parse_args()

    if args.demo:
        company, website = "SliceHouse Pizza", "https://slicehouse.example"
    elif args.company:
        company, website = args.company, args.website or "(not given)"
    else:
        parser.print_help()
        print("\nTip: try: python agent.py --demo")
        return 0

    sheet = build_lead_sheet(company, website)
    print(sheet)

    if args.save:
        with open("lead_sheet.md", "w", encoding="utf-8") as f:
            f.write(sheet)
        print("Saved to lead_sheet.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
