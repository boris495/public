# Runbook for the automatic swarm constructor

## Phase 1 — Feature extraction

Create a compact task vector:

- D: decomposability (0-2)
- C: coupling (0-2; high means workers depend heavily on each other)
- V: objective verifiability (0-2)
- A: ambiguity / number of plausible approaches (0-2)
- R: adversarial or downside risk (0-2)
- F: factual uncertainty / evidence burden (0-2)
- E: expected value of extra compute (0-2)

Record it in `topology.md` if using artifacts.

## Phase 2 — Baseline

Run a strong single-agent attempt or define a baseline from the current root attempt.
Verify it with the same acceptance criteria that will be used for swarm candidates.

Do not weaken the baseline to make the swarm look better.

## Phase 3 — Candidate topology proposal

Choose topology candidates from `topologies.md`.

Useful rules:
- D high, C low -> specialist decomposition.
- A high -> independent explorers.
- V high -> candidate tournament.
- R high -> red-team topology.
- F high -> evidence triangulation.
- D high, C high -> hierarchical decomposition with few boundaries.
- Multiple weak drafts likely to help -> layered MoA.
- Unclear and high-value -> two-topology micro-tournament.

## Phase 4 — Micro-tournament when needed

Use a representative slice:
- one failing test family,
- one difficult research subquestion,
- one customer segment,
- one valuation scenario,
- one architectural decision.

Give candidate topologies comparable budgets.
Do not scale a topology that cannot beat baseline on the slice.

## Phase 5 — Full run

Spawn only the agents required by the winning topology.
Prefer parallelism for independent work; sequence dependent work.

Each agent returns a compact artifact, not a long transcript.

## Phase 6 — Cross-critique and evolution

Critics receive committed candidate artifacts.
Generate at most two targeted mutants from the strongest candidate unless evidence justifies more.

## Phase 7 — Independent verification

Use a fresh verifier.
For code, run real tests/checks.
For research, verify critical factual claims.
For decisions, attack the assumptions and identify reversal conditions.

## Phase 8 — Learn locally

If `.swarm-lab/history.jsonl` exists or can be safely created, append only compact non-sensitive run metrics:

- task class,
- feature vector,
- topology,
- score,
- baseline score,
- agent count,
- generations,
- verification status.

Do not store user secrets, raw prompts, credentials, private source text, or hidden reasoning.

Future runs may use this history as a weak prior, never as a substitute for current-task diagnosis.
