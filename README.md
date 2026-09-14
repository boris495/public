# Swarm Architect

**An evidence-driven Codex skill for selecting and evaluating the smallest multi-agent topology that can materially improve a task.**

Swarm Architect helps Codex decide when parallel agents are worthwhile, which topology fits the dominant failure mode, and when a single-agent solution is the better engineering choice. It treats multi-agent work as a testable hypothesis—not a default.

## What it does

- Diagnoses decomposability, coupling, uncertainty, risk, and verification options.
- Establishes a strong single-agent baseline before claiming a swarm improves anything.
- Selects among specialist decomposition, independent exploration, red teaming, evidence triangulation, test-based tournaments, and hierarchical workflows.
- Uses an independent verifier and objective checks wherever possible.
- Records concise artifacts and measured lift without storing hidden reasoning.
- Falls back to one agent for small, tightly-coupled, or cheap-to-verify work.

The default guardrails are deliberately conservative: 2–4 concurrent subagents, at most 10 total spawned agents per task, and no automatic changes to Codex’s global concurrency configuration.

## Install

Clone this repository into Codex’s discoverable skills directory:

```bash
git clone https://github.com/boris495/public.git "${CODEX_HOME:-$HOME/.codex}/skills/swarm-architect"
```

To update an existing clone:

```bash
git -C "${CODEX_HOME:-$HOME/.codex}/skills/swarm-architect" pull --ff-only
```

## Use with Codex

Invoke the skill explicitly when topology selection matters:

```text
Use $swarm-architect to repair this flaky cross-service transaction bug. Compare a strong single-agent baseline with the smallest topology likely to improve verified correctness.
```

The skill is also available for normal automatic selection. It should be a good fit when a task benefits from independent evidence, multiple solution paths, adversarial review, or separable specialist work.

### Typical routing

| Task shape | Default approach |
| --- | --- |
| Cross-stack bug with deterministic regression tests | Specialist decomposition → integrator → verifier |
| High-ambiguity architecture decision | Independent explorers → critic → blind judge → verifier |
| Factual or regulatory assessment | Evidence triangulation → fact verifier |
| High-downside design decision | Proposal → red team → adjudicator |
| Simple rename or focused edit | One agent → focused verification |

## For agents

Start with [`SKILL.md`](SKILL.md). It is the operational entrypoint and defines the safety boundaries, stopping rules, and reporting format.

- Read [`references/topologies.md`](references/topologies.md) before choosing a multi-agent structure.
- Read [`references/evaluation.md`](references/evaluation.md) before claiming capability lift or emergence.
- Use [`references/runbook.md`](references/runbook.md) for the task-vector and run lifecycle.
- See [`references/examples.md`](references/examples.md) for concrete routing examples.
- Use [`scripts/score_run.py`](scripts/score_run.py) only to compare scorecards; it does not determine whether an effect is emergent.

## Validate

Use Codex’s bundled validator:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" .
```

The validator covers the skill frontmatter, naming, and unfinished scaffolds. Validate `agents/openai.yaml` against the current Codex skill metadata guidance as part of any change.

## Contributing

Useful contributions are concrete and testable: new topology-selection evidence, better falsification checks, small reproducible evaluation scenarios, or documentation that improves agent routing without turning every task into a swarm.

Please keep changes scoped, preserve the single-agent fallback, and avoid adding global configuration mutations. Run the validator and describe the observable behavior you tested in the pull request.

If this skill makes your Codex work more reliable, a GitHub star helps other builders discover it.
