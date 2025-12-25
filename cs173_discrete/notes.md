# CS 173 — discrete Notes
Winter prep starts on 12/21. This folder tracks proof language and basic discrete topics

## Propositions & Connectives
### Key definitions (copy 1-2 lines)
- Proposition: a statement that is either True or False.
- Connectives: not (¬), and (∧), or (∨), implies (→), iff (↔).

### One proposition + proof language practice

**Proposition** If (p ∧ (p → q)), then q.

**Proof**
Assume p ∧ (p → q).  
Then p is true, and (p → q) is true.  
Since p is true and (p → q) is true, it follows that q is true.  
Therefore, q.

### Proof language mini-template
- Assume ...
- We know ...
- Therefore ...
- Conclude ...

Example sentence bank:
- Assume p.
- From p and (p → q), we derive q.  (modus ponens)
- Therefore, ...
- Hence/Thus, ...

### Glossary
- proposition: statement with a truth value (T/F)
- truth value: True/False
- connetions: ¬, ∧, ∨, →, ↔
- implication (p → q): “if p then q”
- modus ponens: from p and (p → q), conclude q