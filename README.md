# Lead Research Agent

**Author:** Wajahat Irfan, BS Computer Science student (7th semester), GPGC No. 1 Abbottabad

## What it does
Produces a structured **lead sheet** for a company from just its name and
website: industry guess (from keywords in the name), likely needs, a
suggested outreach angle, and next steps.

> **Demo data only.** This agent does **not** scrape any real website and
> does not call any API. The industry, needs, and angle are guesses from
> built-in keyword rules — they must be verified with real research before
> any outreach.

## How to run
```bash
cd lead-research-agent
python agent.py --demo
python agent.py --company "SliceHouse Pizza" --website "https://slicehouse.example"
python agent.py --company "SliceHouse Pizza" --website "https://slicehouse.example" --save
```
`--save` also writes the sheet to `lead_sheet.md`.

## Example output
```
# Lead Sheet (Demo Data Only)

**Company:** SliceHouse Pizza
**Website:** https://slicehouse.example
**Industry (guessed from name):** Food & Beverage / Restaurant

## Likely needs
- online ordering
- WhatsApp order taking
- customer replies after hours

## Suggested outreach angle
Offer a WhatsApp ordering assistant that takes orders, confirms them, and
answers menu questions automatically.

## Next steps
1. Verify the company is real and find a real contact person (owner/manager).
2. Check their current website / social pages for what they already automate.
3. Send a short, personal message using the outreach angle above.
4. Offer a small free demo before discussing price.
```

## Skills shown
- Python, `argparse` CLI design
- Rule-based classification from keywords
- Structured report generation (Markdown output)
- Honest demo-data design: no scraping, no fake "research"
