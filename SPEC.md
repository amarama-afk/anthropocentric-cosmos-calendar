# ACC Specification

## Core Principles
- Forward from **0 ACC** (Big Bang origin).
- Uncertainty-first: Precision ≤ stated uncertainty (round aggressively).
- Two certainties separated:
  - Index/label: Exact (±0 for convention, e.g., now = …312 026 ACC ±0).
  - Physical mapping: Carries cosmological uncertainty (±23 Myr under Planck18).
- Epoch tags for updates (head changes; tail stable).
- Mnemonic tail (...312 026):
  - 3 → ~300 kyr Homo sapiens emergence window
  - 1 → ~10–12 kyr Holocene/agriculture pivot
  - 2026 → current-year echo

## Anchor & Epoch
Current: **ACC-Planck18**  
Base age: 13.797 ± 0.023 Gyr (Planck 2018, primary fit).  
Physical now → present: **13 797 312 026 ACC ±0** (label) / ±~23 Myr (mapping).  
(Note: Minor source variations exist ~13.787–13.799 Gyr; all within error bar. Future epochs update head only.)

## Companion Notation
Holocene Era (HE): Gregorian + 10,000 → 2026 = 12026 HE (ideal for historical band).

## Sub-Year Notation & Hybrid with HE
For deep-time events (pre-~12 ka), use integer ACC only—no sub-year needed, as uncertainties dominate.  
For recent/human-scale (post-~12 ka), prefer **HE** for precision:  
- Format: YYYY-MM-DD [HE] (e.g., February 12, 2026 = **12026-02-12 HE**).  
- Time optional: **12026-02-12T14:30:00Z HE** (UTC example).  

Optional hybrid for ACC continuity (display/convention only; not core label):  
- Append sub-tail: [ACC head + tail]-[MM-DD]  
- Example (February 12, 2026): **13 797 312 926-02-12 ACC** (±0 label; sub-tail "926" as mnemonic day/month concat—e.g., 9 for September-like offset or day-of-year proxy; adjust logic as needed).  
- Time: **13 797 312 926-02-12T14:30:00Z ACC**.  
This keeps ACC linear but defers fine-grained to HE to avoid precision illusions.

## Anchor Points
See [anchors.md](anchors.md) for full table with values, uncertainties, rounding, and ≈ glosses.

## Future Updates
When consensus shifts > ~0.05 Gyr (e.g., from DESI, next CMB, JWST refinements), create ACC-[NewAnchor] tag, update head digits, keep tail fixed.

Philosophy: One continuous, honest timeline — cosmology to tweets — without illusions.
