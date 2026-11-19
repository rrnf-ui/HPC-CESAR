## Tempos de execução

| Implementação | 1 Thread | 2 Threads | 4 Threads | 8 Threads | 16 Threads |
|---|---:|---:|---:|---:|---:|
| Serial | 0.345216 s | — | — | — | — |
| Critical | 1.271410 s | 7.052582 s | 8.739312 s | 14.615179 s | 15.511056 s |
| Atomic | 0.993854 s | 3.934233 s | 5.237284 s | 5.940768 s | 7.699373 s |
| Local + Critical | 0.341845 s | 0.454222 s | 0.507571 s | 0.630170 s | 0.414710 s |
| Local + Atomic | 0.171670 s | 0.200475 s | 0.228231 s | 0.269117 s | 0.442294 s |
| Reduction | 0.162770 s | 0.091517 s | 0.061974 s | 0.040931 s | **0.036504 s** |
| Containerized Reduction | — | — | — | — | **0.035739 s** |

## Speedup

| Implementação | Threads | Tempo de execução | Speedup |
|---|---:|---:|---:|
| Reduction | 1 | 0.162770 s | 2.12x |
| Reduction | 2 | 0.091517 s | 3.77x |
| Reduction | 4 | 0.061974 s | 5.57x |
| Reduction | 8 | 0.040931 s | 8.44x |
| Reduction | 16 | 0.036504 s | **9.46x** |
| Containerized Reduction | 16 | 0.035739 s | **9.66x** |
