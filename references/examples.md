# Examples

## Example A — architecture redesign

Prompt:
"Use $swarm-architect to find a better architecture for this repository."

Likely behavior:
1. baseline architecture proposal,
2. task vector shows high ambiguity and moderate verification,
3. independent explorers propose conservative, modular, and performance-first designs,
4. critic finds migration and failure risks,
5. judge selects one,
6. verifier checks repository constraints and test implications,
7. root reports measured lift.

## Example B — difficult bug

Prompt:
"Use $swarm-architect to diagnose this intermittent production bug."

Likely behavior:
- code-path explorer,
- logs/evidence specialist,
- concurrency/race hypothesis explorer,
- red-team falsifier,
- root synthesizes,
- reproduction/test verifier.

If one clear deterministic failure is already identified, fall back to a smaller topology.

## Example C — factual research

Prompt:
"Use $swarm-architect to assess whether this claim is true."

Likely behavior:
- primary-source researcher,
- independent confirmation researcher,
- skeptic/counterevidence researcher,
- fact verifier,
- root synthesis.

## Example D — simple task

Prompt:
"Use $swarm-architect to rename this variable."

Expected result:
The skill diagnoses low complexity and falls back to one agent. No swarm is spawned.

## Example E — topology competition

Prompt:
"Use $swarm-architect in research-grade mode. I care more about correctness than token cost."

Expected result:
- stronger multi-run baseline,
- two-topology micro-tournament,
- objective/independent scoring,
- scale winning topology,
- replicate any claimed emergent-capability effect before labelling it replicated.
