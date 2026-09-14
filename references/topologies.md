# Topology library

Use the smallest topology that attacks the task's dominant failure mode.

## 0. Single-agent baseline

**Use when:** task is simple, tightly coupled, cheap to verify, or delegation overhead is likely to exceed benefit.

**Flow:** root -> solution -> verification.

This is also the control condition for measuring multi-agent lift.

## 1. Independent explorers + blind judge

**Use when:** ambiguity is high and multiple fundamentally different solutions are plausible.

**Flow:**
root -> explorer A
     -> explorer B
     -> explorer C
all commit candidates -> independent critic(s) -> blind judge -> verifier -> root

Make explorer prompts deliberately different. Examples:
- minimal/simple solution,
- performance-first solution,
- risk-first solution,
- first-principles redesign,
- conservative compatibility-preserving solution.

Do not let explorers see each other's conclusions before they commit.

## 2. Specialist decomposition

**Use when:** the problem splits into relatively independent domains.

**Flow:**
root planner -> specialist A/B/C in parallel -> integrator -> verifier

Examples:
- code: architecture / tests / security / API compatibility,
- business: customer / competition / economics / execution,
- research: primary sources / counterevidence / quantitative analysis.

Avoid this topology when subtasks are tightly coupled and every worker needs the same evolving global state.

## 3. Proposal -> red team -> adjudicator

**Use when:** downside risk, hidden assumptions, or adversarial failure matters.

**Flow:**
proposer -> red team
         -> evidence checker
red-team findings + proposal -> adjudicator -> verifier

The red team should try to falsify, not merely polish.

## 4. Layered Mixture-of-Agents

**Use when:** a draft can be improved by successive independent perspectives.

**Flow:**
layer 1: 2-3 independent drafts
layer 2: 1-2 refiners receive all committed layer-1 artifacts
layer 3: synthesizer
then verifier

Use sparingly: it consumes tokens quickly and can converge toward bland consensus.
Preserve minority hypotheses that have strong evidence.

## 5. Candidate tournament

**Use when:** objective tests or benchmarks exist.

**Flow:**
N candidates -> deterministic tests -> survivors -> targeted mutation -> retest -> winner

Prefer this over model-judging for coding, algorithms, data transformations, and other objectively testable work.

## 6. Evolutionary repair loop

**Use when:** an initial candidate is promising but fails on identifiable dimensions.

**Flow:**
candidate -> critic/test failures -> 2 targeted mutants -> selector -> verifier

Mutation should be local and hypothesis-driven.
Default to at most two generations.

## 7. Hierarchical decomposition

**Use when:** the task contains a genuine dependency tree.

**Flow:**
root decomposer -> subtask owners -> leaf workers -> owner synthesis -> root integration

Avoid deep recursive spawning. If a hierarchy can be flattened without losing necessary context, flatten it.

## 8. Evidence triangulation

**Use when:** factual correctness is the main bottleneck.

**Flow:**
researcher A (primary sources)
researcher B (independent confirmation)
skeptic (counterevidence)
synthesizer -> fact verifier

Separate source collection from conclusion writing.

## 9. Two-topology micro-tournament

**Use when:** it is unclear which swarm structure fits a high-value task.

1. Choose the two most plausible topologies.
2. Run each on the same representative slice or acceptance test.
3. Score both with the same rubric and similar budget.
4. Scale only the winner.
5. If neither beats the single-agent baseline, fall back to single-agent.

This is the core "automatic swarm constructor" mechanism.

# Selection heuristic

Score each candidate topology from 0-2 on:

- Fit to decomposability
- Fit to verification method
- Independence/diversity benefit
- Ability to expose correlated errors
- Context-sharing burden (reverse scored)
- Cost/latency burden (reverse scored)

Choose the highest-scoring topology.
If the top two are within 2 points on an important task, run a micro-tournament.
