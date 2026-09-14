---
name: swarm-architect
description: Automatically design, test, select, and run bounded multi-agent Codex topologies for complex tasks. Use when independent approaches, decomposition, adversarial critique, verification, or evolutionary improvement may outperform a single agent; includes a single-agent fallback and measures capability lift against a baseline.
---

# Swarm Architect

Build the smallest multi-agent topology that is likely to improve the current task, then verify that it actually does.

Do not treat more agents as inherently better. Do not claim "emergence" merely because several agents were used.

## Operating loop

1. **Diagnose the task.**
   Estimate:
   - decomposability,
   - coupling between subtasks,
   - need for independent solution diversity,
   - objective verifiability,
   - adversarial/risk level,
   - uncertainty,
   - cost/latency sensitivity.

2. **Run or define a single-agent baseline first** unless the task is already clearly beyond a useful baseline or the user explicitly asks to skip it.
   Record the baseline outcome and verification evidence.

3. **Select candidate topologies.**
   Read `references/topologies.md`.
   Usually choose one topology. If uncertainty about topology is high and the task is important, pilot the two most plausible topologies on a representative slice before scaling.

4. **Bound the swarm.**
   - Prefer 2–4 subagents at once.
   - Respect the runtime's effective concurrency limit.
   - Do not modify Codex concurrency/configuration automatically.
   - Default total spawned agents per task: <= 10.
   - Default evolutionary generations: <= 2 after the initial candidate generation.
   - Avoid recursive spawning unless it materially improves decomposition and remains within the same global budget.
   - Stop when marginal verified improvement is small or negative.

5. **Create independent candidates before cross-contamination.**
   Explorers must commit their candidate artifact before reading another explorer's conclusions.
   Prompts must encode genuinely different search strategies, assumptions, decompositions, or objectives rather than cloning the same role.

6. **Use structured artifacts.**
   For important tasks create:
   `.swarm-lab/<run-id>/`
   and store compact artifacts using the contract in `references/evaluation.md`.
   Never store hidden chain-of-thought. Store concise reasoning summaries, evidence, tests, assumptions, uncertainty, and decisions.

7. **Cross-critique only after candidates exist.**
   Critics should first identify defects, counterexamples, missing evidence, and failure modes. They should not silently replace the candidate with their own answer.

8. **Judge independently.**
   Define the rubric before seeing candidate identities when practical.
   Prefer objective tests, benchmarks, primary evidence, and falsifiable checks over persuasiveness or verbosity.
   If the task is coding, tests/runtime/type checks/security constraints dominate stylistic preference.

9. **Evolve only promising candidates.**
   Mutation means targeted change, not random rewriting:
   - preserve validated strengths,
   - repair specific weaknesses,
   - vary one or two important dimensions,
   - re-run the relevant verification.
   Do not restart from scratch unless all candidates fail for the same structural reason.

10. **Run an independent verifier.**
    The verifier must not be the author of the winning candidate.
    Ask it to falsify the result and report concrete evidence.

11. **Measure lift.**
    Read `references/evaluation.md`.
    Distinguish:
    - compute/ensemble gain,
    - verified collective improvement,
    - an emergent-capability candidate.

12. **Synthesize at the root.**
    The root agent owns the final decision and consequential side effects.
    Do not let multiple workers concurrently edit the same files.
    Use read-only workers for exploration/review where possible; isolate parallel implementations before integration.

## Automatic topology selection

Use this mapping as a starting heuristic, not a rigid rule:

- High decomposability + low coupling -> **specialist decomposition**.
- High ambiguity + high solution diversity -> **independent explorers + blind judge**.
- High factual uncertainty -> **independent research + evidence verifier**.
- High risk/adversarial pressure -> **proposal + red team + adjudicator**.
- Strong objective tests -> **candidate tournament + test-based selector**.
- Long dependency chain -> **hierarchical plan -> workers -> integrator**.
- Need to refine weak drafts through perspectives -> **layered mixture-of-agents**.
- Unknown topology / high-value task -> **micro-tournament of two topologies**, then scale the winner.
- Low complexity or poor expected value from delegation -> **single-agent fallback**.

## Side-effect policy

Subagents should be read-only unless writing is necessary for an isolated candidate.
Only the root should merge, deploy, publish, send messages, spend money, delete important data, or perform irreversible actions.

If the task requires an external side effect, complete analysis and verification first, then follow the normal permission/approval rules of the environment.

## Final report

Keep it short. State:
- selected topology and why,
- agents/generations actually used,
- baseline result,
- swarm result,
- verification performed,
- measured lift,
- whether this is merely ensemble gain, verified collective improvement, or an emergent-capability candidate,
- remaining uncertainty.

Do not call an effect "emergent" without the criteria in `references/evaluation.md`.
