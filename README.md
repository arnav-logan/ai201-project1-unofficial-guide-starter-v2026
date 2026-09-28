# The Unofficial Guide

<!-- Corpus: city_guides -->

---

# Unit 1

## What This Does

This RAG system answers question about the corpus ```city_guides```. This corpus contains information for travelers wanting to visit the various cities described. There is information for how to get to, what to see, places to eat, and places to stay for every city. The corpus also includes information on how the cities are connected to each other to help travelers plan a trip visiting multiple cites. The RAG system aims to pull relevant information to answer any user questions about the cities.

## Chunking Strategy

**Chunk size: 800**
**Overlap: 75**

I kept the chunk size the same as the default because each chunk captured key ideas of a city without being too long. However, I did make my chunker create smaller chunks when it detected more than 6 paragraphs to try to bundle different, smaller paragraphs together. I made the overlap quite small as each the corpus often contains somewhat granular information through small paragraphs. 

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

**Chunk 1** — source: ``guide_accessibility.md#0 — produced by: chunker.py::split_documents``

```
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

## Straightforward

**Thornby Wells** is the easiest town in the region. It is flat, compact, and
everything is within three minutes of everything else. Parking is free for two
hours anywhere in town and the station is central. The pump room and gardens
are level throughout.

**Marchwood** has a modern tram network with level boarding on all four lines,
running every 8 minutes on weekdays. The city museum and covered market are both
step-free. The distances between districts are the main consideration.

**Brightwater** is level along the river and through the centre. The mill museum
is step-free. The station is a 15-minute wal

```

**Chunk 2** — source: ``guide_corry_vale.md#1 — produced by: chunker.py::split_documents``

```
it must be booked a day ahead. Most visitors drive between villages and walk the footpaths in between.

## Eat and drink

One pub in the largest village serves food seven days a week. A second, in the third village, opens Thursday to Sunday. There is a farm shop at the valley mouth that sells bread,alley beyond a school bus that will carry passengers if there is room. Driving from Brightwater takes 35 minutes on a good road as far as the valley mouth and then 20 more on a poor one. Cycling in is a serious undertaking; the road climbs 400 metres in the first four miles.

## Getting around

Nothing within the valley is walkable from anything else — the villages are two to four miles apart. There is one taxi, based in the largest village, and it must be booked a day ahead. Most visitors drive between v

```

**Chunk 3** — source: ``guide_givens_mill.md#0 — produced by: chunker.py::split_documents``

```
# Givens Mill

Givens Mill is a village of 700 built around a working watermill that still grinds flour commercially. It is the sort of place people visit for an afternoon and then talk about for longer than the visit lasted.

## Getting there

No station and no bus on Sundays; four buses a day from Brightwater on weekdays, taking 30 minutes. Driving is 20 minutes. The village car park holds about forty cars and is full by 11am on summer Saturdays.

## Getting around

Everything is on one street along the river. The mill is at one end and the church at the other, eight minutes apart. The riverside path continues in both directions for as far as you want to walk.

## Eat and drink

```

**Chunk 4** — source: ``guide_kestrelford.md#2 — produced by: chunker.py::split_documents``

```
modation of any kind within four miles of the town in either direction.

## When to go

Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-trackapproach road is genuinely difficult in snow and theand the trackbed is now a walking route. Buses run from Brightwater roughly hourly on weekdays, every two hours on Saturdays, and not at all on Sundays. Driving takes 55 minutes and the last eight are on a single-track road with passing places.

## Getting around

Everything is within a ten-minute walk of the market square. The town is built on a slope and the walk up from the lower car park is steeper than it looks on a map. There is no local bus service within the town itself.

## Eat and drink

Four pu

```

**Chunk 5** — source: ``guide_regional_transport.md#0 — produced by: chunker.py::split_documents``

```
# Getting around the region

## The railway

The line runs along the river valley, connecting Brightwater to the regional
hub in 50 minutes. Eleven services a day on weekdays, six on Sundays. The line
north of Brightwater closed in 1963 and everything beyond it is bus or car.

Tickets are cheaper booked the day before than on the day, and considerably
cheaper than that booked a week ahead. There is no ticket office at
Brightwater station outside weekday mornings; the machine on the platform takes
cards only.

## Buses

Three operators run in the region and they do not accept each other's tickets,
which is the single most common source of confusion for visitors. Services
concentrate on weekday daytimes. Sunday service is minimal to non-existent
outside the Brightwater town routes.

The Kestrelford se
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
Where are some good places to eat in Thornby Wells?

**Answer:**

```
Based on the provided documents, Thornby Wells is known for doing "Sunday lunch as a local institution and it needs booking a week ahead" (*guide_eating.md*).
```

**My relevance cutoff:**

I decided to use a cutoff of 0.65 (0.05 higher than the original) because the original cutoff already worked almost all of the time and was in-between the related question and unrelated question averages (0.4082 to 0.8912). I decided to slightly increase the cutoff to accept more general questions.

| Question | In corpus? | Best distance |
|---|---|---|
| What times are Brightwater's markets open? | Yes | 0.436 |
| When should I go to visit Kestrelford and what can I do there? | Yes | 0.491 |
| How long does it take to drive from Brightwater to Pellew Sands and where can I park? | Yes | 0.389 |
| What is the capital of Mongolia? | No | 0.944 |
| How do I change the oil in a diesel engine? | No | 0.862 |
| Who won the 1994 World Cup? | No | 1.002 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.829 |
| How do I write a for loop in Rust? | No | 0.819 |

## How I Used AI

**1.**
I asked Claude if making a chunker that had a variable chunk length for this corpus was ideal. It said that it could be helpful so I made my chunker create smaller chunks when needed.

**2.**
I asked Claude to compute the average distances of the measured distances of the in corpus and out of corpus questions. I used the computed averages.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 3/5 | 3/5 | 3/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks pertain to a specific topic in a select city and should not contain information about another city.  | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 5. The system should not refuse questions that ask about a location without naming a city. | 3 of 5 | 4/5 | 4/5 | 4/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Criterion 1 - Retrieved chunk contains the answer
(All of the following text from ``results\run_2026-09-23_1914_before.md`` produced by ``run_eval.py::run_once``)

**Question 1 - What times are Brightwater's markets open? (Fail)**
```
Based on the provided documents, there is no mention of Brightwater's markets or their opening times. Therefore, I do not have enough information to answer this question.
```

**Question 2 - When should I go to visit Kestrelford and what can I do there? (Fail)**
```
According to `guide_seasons.md`, Kestrelford fills with walkers in July and August, and its Saturday market "builds back to full size through April." Additionally, `guide_kestrelford.md` notes that the town is charming to explore on foot since "everything is within a ten-minute walk of the market square," and the old railway trackbed running from Kestrelford provides "the best walking in the region for the effort involved" (`guide_regional_transport.md`).
```

**Question 3 - How long does it take to drive from Brightwater to Pellew Sands and where can I park? (Pass)**
```
According to `guide_pellew_sands.md`, "Driving is 50 minutes from Brightwater." 

For parking, "Seafront parking is metered and expensive; the free lot behind the station is a four-minute walk and almost always has space."
```

**Question 4 - Where are the best places to eat in Marchwood located? (Pass)**
```
According to `guide_eating.md`, the good district in Marchwood—Northgate—is located "a tram ride away rather than a street away".
```

**Question 5 - What is there to see in Givens Mill? (Pass)**
```
Based on `guide_givens_mill.md`, Givens Mill features a "working watermill that still grinds flour commercially" and a church, which are located at opposite ends of the village's single street. Visitors can also enjoy a "riverside path [that] continues in both directions" and a "tearoom attached to the mill" that sells bread made from the locally ground flour.
```

## Criterion 2 - Every answer names a source
(All of the following text from ``results\run_2026-09-23_1914_before.md`` produced by ``run_eval.py::run_once``)

**Question 1 - What times are Brightwater's markets open? (Pass)**
```
Based on the provided documents, there is no mention of Brightwater's markets or their opening times. Therefore, I do not have enough information to answer this question.
```

**Question 2 - When should I go to visit Kestrelford and what can I do there? (Pass)**
```
According to `guide_seasons.md`, Kestrelford fills with walkers in July and August, and its Saturday market "builds back to full size through April." Additionally, `guide_kestrelford.md` notes that the town is charming to explore on foot since "everything is within a ten-minute walk of the market square," and the old railway trackbed running from Kestrelford provides "the best walking in the region for the effort involved" (`guide_regional_transport.md`).
```

**Question 3 - How long does it take to drive from Brightwater to Pellew Sands and where can I park? (Pass)**
```
According to `guide_pellew_sands.md`, "Driving is 50 minutes from Brightwater." 

For parking, "Seafront parking is metered and expensive; the free lot behind the station is a four-minute walk and almost always has space."
```

**Question 4 - Where are the best places to eat in Marchwood located? (Pass)**
```
According to `guide_eating.md`, the good district in Marchwood—Northgate—is located "a tram ride away rather than a street away".
```

**Question 5 - What is there to see in Givens Mill? (Pass)**
```
Based on `guide_givens_mill.md`, Givens Mill features a "working watermill that still grinds flour commercially" and a church, which are located at opposite ends of the village's single street. Visitors can also enjoy a "riverside path [that] continues in both directions" and a "tearoom attached to the mill" that sells bread made from the locally ground flour.
```

## Criterion 3 - Gate stops out-of-corpus questions
(All of the following text from ``results\run_2026-09-23_1914_before.md`` produced by ``run_eval.py::check_out_of_scope``)

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.890 | refused |
| How do I change the oil in a diesel engine? | 0.862 | refused |
| Who won the 1994 World Cup? | 1.002 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.829 | refused |
| How do I write a for loop in Rust? | 0.819 | refused |

## Criterion 4 - Sampled chunks pertain to a specific topic in a select city and should not contain information about another city.
(All of the following text from printing to terminal, produced by ``chunker.py::split_documents``)
```
======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents (Fail)
======================================================================
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

## Straightforward

**Thornby Wells** is the easiest town in the region. It is flat, compact, and
everything is within three minutes of everything else. Parking is free for two
hours anywhere in town and the station is central. The pump room and gardens
are level throughout.

**Marchwood** has a modern tram network with level boarding on all four lines,
running every 8 minutes on weekdays. The city museum and covered market are both
step-free. The distances between districts are the main consideration.

**Brightwater** is level along the river and through the centre. The mill museum
is step-free. The station is a 15-minute wal

======================================================================
Chunk 2  |  source: guide_corry_vale.md#2  |  produced by: chunker.py::split_documents (Pass)
======================================================================
alley, spread across two pubs and a handful of farmhouse rooms. In summer these are booked months ahead. Camping is permitted on two marked fields and nowhere else.

## When to go

May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and severaalley beyond a school bus that will carry passengers if there is room. Driving from Brightwater takes 35 minutes on a good road as far as the valley mouth and then 20 more on a poor one. Cycling in is a serious undertaking; the road climbs 400 metres in the first four miles.

## Getting around

Nothing within the valley is walkable from anything else — the villages are two to four miles apart. There is one taxi, based in the largest village, and it must be booked a day ahead. Most visitors drive between v

======================================================================
Chunk 3  |  source: guide_givens_mill.md#2  |  produced by: chunker.py::split_documents (Pass)
======================================================================
come for a half day.

## When to go

The mill runs March to November and is closed entirely in winter. Late spring is the best time. Summer Saturdays are busy enough that the car park becomes the limiting factor; come on a weekday if you can.

## Practical notes

Cash is still useful at the market Brightwater on weekdays, taking 30 minutes. Driving is 20 minutes. The village car park holds about forty cars and is full by 11am on summer Saturdays.

## Getting around

Everything is on one street along the river. The mill is at one end and the church at the other, eight minutes apart. The riverside path continues in both directions for as far as you want to walk.

## Eat and drink



======================================================================
Chunk 4  |  source: guide_marchwood.md#1  |  produced by: chunker.py::split_documents (Pass)
======================================================================
ares and nobody tells you this at the machine. The centre is walkable but the interesting districts are not adjacent to each other.

## Eat and drink

The best eating is in the Northgate district, a 12-minute tram ride from the station, where about thirty restaurants sit within four streets. The aree in the region meets here, which is the city's defining feature. Trains to Brightwater run every 40 minutes until 11pm. The airport is 20 minutes out by a dedicated bus that runs every 15 minutes and costs more than the equivalent taxi shared between three people.

## Getting around

A tram network of four lines, running every 8 minutes on weekdays and every 15 at weekends, until midnight. A day ticket costs less than two single fares and nobody tells you this at the machine. The centre is walkable but t

======================================================================
Chunk 5  |  source: guide_regional_transport.md#2  |  produced by: chunker.py::split_documents (Pass)
======================================================================
our miles upstream on a good surface. The
old railway trackbed from Kestrelford runs six miles on an easy gradient and is
the best walking in the region for the effort involved. The coastal path from
Halden Bay is more serious — exposed, and closed in high wind.

Cycling is pleasant on the river patoked the day before than on the day, and considerably
cheaper than that booked a week ahead. There is no ticket office at
Brightwater station outside weekday mornings; the machine on the platform takes
cards only.

## Buses

Three operators run in the region and they do not accept each other's tickets,
which is the single most common source of confusion for visitors. Services
concentrate on weekday daytimes. Sunday service is minimal to non-existent
outside the Brightwater town routes.

The Kestrelford se
```

## Criterion 5 - The system should not refuse questions that ask about a location without naming a city.
**Question 1 - What city should I visit to buy pastries? (Pass)**
```
(best distance 0.611, cutoff 0.65)
Based on the provided document (`guide_eating.md`), Kestrelford's bakery "sells out by 11am and is the reason a lot of people return."
```

**Question 2 - Where should I visit to go on a hike? (Pass)**
```
(best distance 0.587, cutoff 0.65)

Based on the documents, you can visit the **Corry Vale circuit**, which is about nine miles with 500 metres of ascent and takes in three of the four villages (from `guide_walking.md`). You can also walk the **Brightwater river path**, the **Kestrelford trackbed**, or the route from **Givens Mill** to Brightwater (from `guide_walking.md`).
```

**Question 3 - Where is a nice place to stay the night? (Pass)**
```
(best distance 0.632, cutoff 0.65)

Based on the provided documents, there is no mention of "nice" places to stay, only that accommodations book up for the migration seasons a year ahead in *guide_elder_ness.md*, and that rooms in Corry Vale are "spread across two pubs and a handful of farmhouse rooms" which are booked months ahead in summer (*guide_corry_vale.md*). 
```

**Question 4 - What is the best city to relax in? (Fail)**
```
(best distance 0.660, cutoff 0.65)

I don't have enough information about that.
```

**Question 5 - Which city should I visit in the summer? (Pass)**
```
(best distance 0.557, cutoff 0.65)

According to `guide_seasons.md`, **June** is described as "excellent everywhere." However, in July and August, the documents note that "Halden Bay becomes very busy," "Kestrelford fills with walkers," and "Brightwater goes quiet to the point of dullness."
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
