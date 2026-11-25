
## 1. Resultados MPI


| Implementação | 1 processo (serial) | 2 processos | 4 processos | 8 processos | 10 processos |
|---|---:|---:|---:|---:|---:|
| Serial (`letters.c`) | 0.223273 s | — | — | — | — |
| MPI coletivas (`mpi-letters-coletivas.c`) | — | 0.149235 s | 0.071553 s | 0.053642 s | 0.049955 s |
| MPI ponto a ponto (`mpi-letters-p2p.c`) | — | 0.145575 s | 0.114728 s | 0.059340 s | 0.050065 s |
| MPI coletivas conteinerizado | — | 0.079962 s | 0.054902 s | 0.028559 s | **0.025524 s** |

### Análise dos resultados MPI

- O melhor resultado MPI foi obtido pela implementação coletiva conteinerizada, com **10 processos**, em **0.025524 s**.
- Entre as versões MPI não conteinerizadas, a implementação com operações coletivas foi mais rápida que a versão ponto a ponto para 4, 8 e 10 processos.
- A conteinerização apresentou os menores tempos em todas as quantidades de processos medidas.

## 2. Comparação: MPI conteinerizado vs. OpenMP conteinerizado


| Implementação | Processos/Threads | Tempo de execução |
|---|---:|---:|
| MPI coletivas conteinerizado | 10 processos | **0.025524 s** |
| OpenMP Reduction conteinerizado | 16 threads | 0.035739 s |

A implementação MPI conteinerizada executou em aproximadamente **28,6% menos tempo** que a implementação OpenMP conteinerizada.
