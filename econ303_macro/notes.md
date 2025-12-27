# ECON 303 — Macro Notes
Winter prep starts on 12/21. This folder tracks pre-study for ECON 303.

# Solow Model
- Source: MIT OCW / lecture notes (Solow)

## Key concepts & variables

### Variables
- **k = K/L**: capital per worker
- **y = Y/L = f(k)**: output per worker
- **c**: consumption per worker
- **i**: investment per worker
- **s**: saving rate
- **δ**: depreciation
- **n**: population growth

### Core mechanism
- **Resource constraint:**  c + i = f(k)  
- **Saving rule:** i = s f(k)  
- **Law of motion:** k_{t+1} = s f(k_t) + (1 - δ - n) k_t

## Conslusions
- **Steady state:** there exists a unique k*; the economy converges to it. 
    - The steady state is where sf(k) = (δ + n)k. Uniqueness and convergence come from diminishing returns (concavity of f) versus linear break-even investment: below k*, k rises; above k*, k falls.
- **Comparative statics:**  
  - s ↑ ⇒ k*, y* ↑  
  - δ ↑ or n ↑ ⇒ k*, y* ↓ 

## Common pitfalls
- Confusing **level effect** vs **growth rate effect** (Solow raises level y*, not permanent growth rate without tech progress).
    - Higher saving raises the steady-state level of output per worker, but it does not generate permanent per-capita growth; growth is only temporarily higher during the transition.
- Forgetting that **population growth dilutes capital per worker**.