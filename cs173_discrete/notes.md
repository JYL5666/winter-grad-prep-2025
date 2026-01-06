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

# Implication (P -> Q) & Proof Skeleton

## Meaning
- P -> Q means: if P is true, then Q must be true.
- The standard direct proof structure:
  - Assume P.
  - ...
  - Therefore Q.
  - So P -> Q.

## Template (Direct Proof: Assume/Show)
Assume P.
(Use definitions / algebra / logic steps.)
Therefore Q.
So P -> Q.

## Useful equivalence
- (P -> Q) is equivalent to (~Q -> ~P)  (contrapositive)

## Example 1 (Direct)
Claim: If n is even, then n^2 is even.

Proof:
Assume n is even.
Then n = 2k for some integer k.
So n^2 = (2k)^2 = 4k^2 = 2(2k^2).
Therefore n^2 is even.
So if n is even, then n^2 is even.

## Example 2 (Direct)
Claim: If n is divisible by 4, then n is divisible by 2.

Proof:
Assume n is divisible by 4.
Then n = 4k for integer k.
So n = 2(2k)
Therefore n is divisible by 2.
So if n is divisible by 4.