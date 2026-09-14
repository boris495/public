# Evaluation and emergence criteria

## Artifact contract

Each candidate artifact should contain:

- `objective`
- `candidate`
- `reasoning_summary`
- `assumptions`
- `evidence`
- `tests_or_checks`
- `known_weaknesses`
- `uncertainty`
- `confidence_0_to_1`
- `recommended_next_step`

Do not store hidden chain-of-thought.

## Default scorecard

Use hard constraints first. A candidate that violates a hard constraint cannot win.

For remaining candidates, score 0-100:

- task quality / correctness: 35%
- independent verification evidence: 30%
- robustness / failure resistance: 20%
- useful diversity / novelty: 10%
- efficiency: 5%

Change weights when the task clearly demands it, but define them before judging candidate identities.

For coding tasks, objective test results can override the generic rubric.

## Baseline

At minimum compare the swarm against one normal strong single-agent run.

For high-value or research-grade claims, use multiple independent single-agent baselines under comparable conditions.

Track when available:

- pass/fail against acceptance criteria,
- tests passed,
- defects found,
- judge score,
- elapsed time,
- token/cost estimate,
- number of agents,
- number of generations.

## Capability lift

Let:

`lift = verified_swarm_score - verified_best_single_score`

The absolute score matters more than lift if both results still fail the task.

### Classification

**No demonstrated lift**
- swarm does not beat the best single-agent result after verification.

**Ensemble/compute gain**
- swarm improves score, confidence, or reliability, but the improvement is consistent with more search/compute and does not cross a new task-success boundary.

**Verified collective improvement**
- swarm materially improves an objective success measure, fixes failures that survive the baseline, or produces a more robust verified solution.

**Emergent-capability candidate**
Use this label only if all are true:
1. There is a predefined binary or clearly objective capability criterion.
2. Every comparable individual candidate tested fails that criterion.
3. The assembled multi-agent system passes it.
4. An independent verifier confirms the pass.
5. The effect depends on interaction/topology, not merely selecting the best independent sample.

**Replicated emergent-capability candidate**
- the previous result repeats in at least two independent trials or on more than one representative instance.

Do not claim AGI, consciousness, or a new general capability from a local task-level effect.

## Correlated-error controls

Use at least two where practical:
- independent candidate generation before sharing,
- different decompositions or hypotheses,
- independent evidence collection,
- blind or identity-neutral judging,
- deterministic tests,
- separate verifier,
- explicit counterexample search,
- preservation of minority hypotheses until evidence rejects them.

## Stopping rules

Stop when any applies:
- success criteria are met and verifier passes,
- two successive mutations fail to improve verified score,
- the swarm does not beat baseline on the representative slice,
- agent/token/time budget is exhausted,
- additional agents are repeating existing hypotheses,
- remaining uncertainty requires user input or unavailable evidence.
