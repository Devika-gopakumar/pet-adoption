# Pet Adoption Management System

A small full-stack project for managing pet donations and adoptions, built to practice relational schema design and SQL querying with a Flask front end.

## Tech Stack
- **Backend:** Python (Flask)
- **Database:** MySQL
- **Frontend:** Jinja2 templates (HTML)

## Schema

Three normalized tables, related by foreign keys:

```
Donor (donor_id PK, donor_name, donor_phone)
Pet   (pet_id PK, pet_species, pet_breed, donor_id FK -> Donor, available)
Adopter (adopter_id PK, adopter_name, adopter_phone, pet_id FK -> Pet)
```

- Each **Pet** references the **Donor** who gave it up.
- Each **Adopter** references the **Pet** they adopted.
- `Pet.available` is a flag flipped to `0` once a pet is adopted, so the app can distinguish pets still up for adoption from ones already placed.

The schema is in [3NF](https://en.wikipedia.org/wiki/Third_normal_form) — no repeating groups, every non-key attribute depends only on its table's primary key, and donor/adopter contact details are stored once each rather than duplicated across pet rows.

## Features
- **Donate** (`/donate`) — register a new donor and the pet they're giving up for adoption
- **Adopt** (`/adopt`) — register an adopter against an available pet; marks the pet unavailable on success
- **View** (`/view`) — lists all currently available pets, joined with their donor's details

## Sample Queries

See [`queries.sql`](./queries.sql) for example JOIN and aggregate queries against this schema (e.g. listing adopters with their pet's details, counting donations per donor).

## Setup
1. Run `pet_adoption_schema.sql` against a MySQL instance to create `projectdb` and its tables.
2. Set your DB credentials as environment variables (see `.env.example`) rather than hardcoding them.
3. `pip install -r requirements.txt`
4. `python app.py`
