
# Hyderabad Local Context — product.md

> Primary file used to steer Kiro about Hyderabad. The app **must** read this file
> to shape its behavior. Update carefully; the YAML blocks are parsed by the tool.

## Version
v1.0 (2025-12-28)

## City Meta
- name: Hyderabad
- tz: Asia/Kolkata
- language: English, Telugu, Urdu, Hindi (mixed usage)

## Slang & Colloquialisms (YAML)
```yaml
slang:
  - word: pakka
    meaning: sure
    notes: used widely across Telangana
  - word: timepass
    meaning: casual hangout / low-effort activity
  - word: full meals
    meaning: thali-style meal; rice-centric
  - word: bandi
    meaning: food cart/stall
  - word: dabba
    meaning: lunch box; sometimes used as generic container
  - word: irani chai
    meaning: strong sweet tea served in cafés; cultural staple in old city
  - word: idly-vada
    meaning: South Indian breakfast combo; idly (steamed rice cake) + vada (fried)
  - word: set dosa
    meaning: mini stack of 2–3 soft dosas; typical breakfast
  - word: tiffin center
    meaning: quick-service breakfast/snack eatery
  - word: pataka
    meaning: firecracker; also colloquial for impressive/glamorous (context-dependent)
  - word: mast
    meaning: great / awesome
```

## Traffic Heuristics (YAML)
```yaml
traffic:
  peak_hours:
    - name: office_morning
      days: [Mon, Tue, Wed, Thu, Fri]
      start: '08:00'
      end: '11:00'
      hotspots: [Hitec City, Madhapur, Gachibowli, Financial District, Kondapur]
    - name: office_evening
      days: [Mon, Tue, Wed, Thu, Fri]
      start: '17:00'
      end: '20:30'
      hotspots: [Hitec City, Madhapur, Gachibowli, Financial District, Jubilee Hills]
    - name: old_city_nights_ramzan
      days: [Fri, Sat, Sun]
      months: [Mar, Apr]
      start: '20:00'
      end: '01:00'
      hotspots: [Charminar, Mehdipatnam, Nampally, Mallepally]
  event_overrides:
    - match: cricket_match_uppal
      locations: [Uppal, Nacharam]
      start: '15:00'
      end: '23:00'
      severity: high
      notes: Match days cause spillover on NH163
    - match: metro_disruption
      locations: [Ameerpet, Dilsukhnagar, Miyapur, LB Nagar]
      severity: medium
      notes: If metro services delayed, expect elevated road traffic
  road_notes:
    - road: ORR
      notes: Fast but watch for ongoing ramp closures; toll applies
    - road: Necklace Road
      notes: Congestion around evenings; leisure traffic
    - road: Mehdipatnam Flyover
      notes: Occasional maintenance closures; diversions via Tolichowki
```

## Food & Culture Tips (YAML)
```yaml
food:
  irani_chai_spots: [Nimrah Cafe & Bakery, Café Niloufer, Shadab, Alpha Hotel]
  biryani_favorites: [Shah Ghouse, Bawarchi RTC X Roads, Shadab, Paradise Secunderabad]
  tiffins: [Govind Dosa, Ram Ki Bandi, Chutneys]
  veg_options: [Chutneys, Ohris Jiva, Minerva]
  notes:
    - Late nights in old city during Ramzan are vibrant but crowded; plan parking.
    - Many places closed mid-afternoon; check hours.
```

## Safety & Practical (YAML)
```yaml
safety:
  emergency_numbers:
    police: 100
    ambulance: 102
    women_help: 181
  notes:
    - Prefer prepaid autos or app cabs near transit hubs.
    - Keep cash for small vendors (bandis), though UPI is widely accepted.
```

## Formatting Rules
- All times local
- Use severity levels: low/medium/high for traffic
- Default language: English; preserve original slang in quotes when translating

