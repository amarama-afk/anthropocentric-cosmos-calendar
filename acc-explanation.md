I’m publishing **ACC (Anthropocentric Cosmos Calendar)**: a versioned calendar and notation convention for agents, creators, and systems that need to represent timelines spanning cosmology, Earth history, evolution, and recorded history, without letting artificial precision creep in. The goal is to keep the physics honest while keeping human history intuitive and forward-counting.

ACC counts **forward** from the beginning of the universe: **0 ACC** at the origin, increasing up to the present. For this release, the present label is **13 797 312 026 ACC**.

The “head” of ACC is anchored to an explicit reference cosmology: **Planck 2018, flat ΛCDM**, with universe age **13.797 ± 0.023 billion years (1σ)**. ACC doesn’t invent ages. It declares its reference frame and uncertainty up front, and it is designed to be revised: improved measurements become explicit epoch-tag updates (for example **ACC-Planck18**, later **ACC-PlanckXX**), rather than silent drift.

The rule that matters is **uncertainty-first**: if the evidence is broad, the number must look broad too. A renderer must round the displayed value so precision never outruns the stated uncertainty.

ACC also separates two kinds of certainty that are usually tangled together:

1. **Index certainty (labels):** an ACC label can be exact as a label. That’s why “now” can be written **13 797 312 026 ACC ± 0**: the ±0 refers to the label being exact in the convention.

2. **Physical mapping uncertainty (interpretation):** whenever you interpret ACC as physical “years since Big Bang,” you must carry an uncertainty band. Under the Planck18 anchor, the origin mapping at **0 ACC** is physically uncertain by **±23 Myr (1σ)** relative to the present mapping.

The “tail” of the current-year label, **…312 026**, is openly declared convention and mnemonic, not extra cosmological measurement. It is intentionally **stable across epochs**: when the anchor is updated, the head changes under a new epoch tag, but the tail remains as a human-facing constant. The fine-grained digits must not be interpreted as physical resolution finer than the epoch mapping allows; under **ACC-Planck18**, that physical mapping uncertainty is **±23 Myr (1σ)**.

When improved cosmology revises the universe-age estimate, ACC updates the **leading digits** (the cosmology-anchored head) under a new epoch tag, while the tail keeps a stable human anchor so posters, datasets, and citations don’t churn with every revision. In this release, the mnemonic tail is:

* **3** → ~300 kyr Homo sapiens emergence (human-scale anchor window)
* **1** → ~10–12 kyr transition into settlement/agriculture (Holocene pivot)
* **2026** → the current year echo (present-reference readability)

For near-present dating, the best companion is **Holocene Era (HE)**: the same underlying dates as Gregorian, but with **10,000 added to the year**, so **2026 = 12026 HE**. People can still write “2026” when they want; HE is simply the cleaner forward-counting habit for the historical band.

## ACC in practice: 15 anchor points (chronological)

Each entry is written as value ± uncertainty (1σ where sourced; otherwise explicitly marked as illustrative), then rounded so displayed precision ≤ uncertainty, plus a plain-language (≈ years ago) gloss derived under the declared epoch.

1. Big Bang (Planck18 physical mapping): **~0 ACC ± 23 Myr (1σ)** *(≈ 13.797 Ga ago)*
2. First stars ignite (cosmic dawn; intentionally coarse): **~150 000 000 ACC ± 50 Myr (1σ, illustrative)** *(≈ 13.65 Ga ago)*
3. Solar System forms (CAIs; tight lab chronology): **~9 230 000 000 ACC ± 160 000 (1σ)** *(≈ 4.57 Ga ago)*
4. Great Oxidation Event onset (interval-style; midpoint + half-width shown as a band): **~11 354 000 000 ACC ± 17 000 000 (1σ-equivalent)** *(≈ 2.44 Ga ago)*
5. Cambrian boundary / “Cambrian explosion” era marker (strat boundary; uncertainty varies by source): **~13 258 500 000 ACC ± 200 000 (1σ)** *(≈ 539 Ma ago)*
6. Permian–Triassic boundary: **~13 545 410 000 ACC ± 24 000 (1σ)** *(≈ 252 Ma ago)*
7. Chicxulub impact (K–Pg): **~13 731 270 000 ACC ± 11 000 (1σ)** *(≈ 66.0 Ma ago)*
8. Human–chimpanzee divergence (illustrative band; commonly cited ~6–8 Ma): **~13 791 000 000 ACC ± 1 000 000 (1σ, illustrative)** *(≈ 6–8 Ma ago)*
9. Earliest widely accepted Oldowan stone tools (illustrative band; commonly cited ~2.6 Ma): **~13 794 700 000 ACC ± 50 000 (1σ, illustrative)** *(≈ 2.6 Ma ago)*
10. Early Homo sapiens (Jebel Irhoud): **~13 796 997 000 ACC ± 34 000 (1σ)** *(≈ 315 ka ago)*
11. Holocene transition / early settlement & agriculture (zoom anchor; illustrative band unless tied to a specific proxy): **~13 797 300 000 ACC ± 500 (1σ, illustrative)** *(≈ 12.0 ka ago)*
12. Invention of writing (Mesopotamia/Egypt broad window; illustrative band unless pinned to a specific corpus/date): **~13 797 307 000 ACC ± 200 (1σ, illustrative)** *(≈ 5.0 ka ago)*
13. Great Pyramid of Giza (Khufu; historical-band example; band illustrative unless tied to a specific chronology): **~13 797 307 500 ACC ± 5 (1σ, illustrative)** *(≈ 4.5 ka ago)*
14. Industrial Revolution (steam power scaling; illustrative band): **~13 797 311 800 ACC ± 50 (1σ, illustrative)** *(≈ 230 ya)*
15. Now (index label, convention): **13 797 312 026 ACC ± 0** *(0 ya)*

ACC is about treating the universe as **one real, forward-running timeline** you can actually use: everything on the same axis, from cosmology to history, without illustrative compression. Uncertainty is explicit, precision is enforced by rounding, and the anchor can evolve via epoch tags when better measurements arrive.
