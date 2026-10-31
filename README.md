# Family Fun San Diego

A daily list of toddler-friendly events around San Diego County, in two lanes:

- **Book ahead**: ticketed shows, timed-entry holiday events and on-sale dates, ranked by urgency.
- **Next few days**: what's on between today and the end of next weekend.

Live page: https://richstoner.github.io/family_fun_sandiego/

## How it updates

A scheduled Claude task runs each morning (daily sweep) and Sunday morning (look-ahead scan). It
researches events, checks each against the venue or organizer page, updates a private board, and
then regenerates `events.json` here with `export.py` and pushes it. Events the family marked
booked or skipped are left out of the public list.

`index.html` is a static page that reads `events.json`; there's no build step.
