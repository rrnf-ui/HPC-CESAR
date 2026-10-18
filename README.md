# Desafio 1

## Área de aplicação
Física e Química Computacional

## Software escolhido
LAMMPS (*Large-scale Atomic/Molecular Massively Parallel Simulator*)

## Qual problema ele resolve?
O LAMMPS é um software de simulação de dinâmica molecular utilizado para modelar o movimento e as interações entre grandes quantidades de átomos e partículas. Ele permite que pesquisadores investiguem as propriedades e o comportamento de materiais em escala atômica, contribuindo para estudos em áreas como ciência dos materiais, física e química.

## Como o HPC é utilizado nele?
O LAMMPS utiliza computação de alto desempenho (HPC) para acelerar simulações computacionalmente intensivas. Para isso, distribui os cálculos entre múltiplos núcleos de processamento, processadores e, quando disponíveis, GPUs ou diferentes computadores conectados em um cluster. Essa abordagem permite executar simulações mais rapidamente e trabalhar com sistemas compostos por um número maior de partículas.

## Por que o problema se beneficia de HPC?
Simulações em escala atômica exigem um grande volume de cálculos para determinar as posições, velocidades e interações das partículas ao longo do tempo. À medida que o número de partículas e a duração da simulação aumentam, o custo computacional também cresce significativamente. O HPC permite paralelizar esses cálculos, reduzindo o tempo de execução e possibilitando o estudo de sistemas maiores e mais complexos, com maior eficiência computacional.

## Bibliotecas, frameworks e tecnologias utilizadas
- **MPI (Message Passing Interface):** permite a comunicação e a coordenação entre processos executados em diferentes núcleos ou computadores.
- **OpenMP:** possibilita o paralelismo por meio de múltiplas threads em processadores com memória compartilhada.
- **GPUs:** tecnologias como CUDA, HIP, OpenCL e SYCL podem ser utilizadas para acelerar determinadas partes das simulações, conforme o suporte disponível na versão e na configuração do software.
- **CMake:** ferramenta utilizada para configurar e gerenciar o processo de compilação do software.
- **C++:** linguagem de programação utilizada na implementação do LAMMPS.

## Como o software explora o paralelismo?
O LAMMPS utiliza principalmente a técnica de **decomposição espacial (*spatial decomposition*)**, na qual o domínio da simulação é dividido em sub-regiões, distribuídas entre diferentes processos. Cada processo calcula o movimento e as interações das partículas presentes em sua região, comunicando-se com os demais quando necessário, especialmente para tratar interações entre partículas próximas às fronteiras dos subdomínios.

Além disso, o software pode combinar diferentes estratégias de paralelismo, como MPI, OpenMP e processamento em GPU. Essa combinação permite aproveitar melhor os recursos de hardware disponíveis, aumentando a escalabilidade e o desempenho das simulações.

## Testes de desempenho

Foram realizados testes com o **LAMMPS** utilizando o arquivo de entrada `examples/melt/in.melt`, com o objetivo de avaliar o impacto do paralelismo no tempo de execução de uma simulação de dinâmica molecular.

### Ambiente de teste

- **Núcleos físicos:** 8
- **Threads por núcleo:** 2
- **Total de threads de hardware:** 16
- **Arquivo de entrada:** `examples/melt/in.melt`
- **Tamanho da simulação:** 4.000 átomos
- **Passos de simulação:** 250

### Resultados

| Processos MPI | Threads OpenMP | Tempo (s) | Passos/s | Matom-step/s |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0,364760 | 685,382 | 2,742 |
| 2 | 1 | 0,287332 | 870,074 | 3,480 |
| 4 | 1 | 0,222932 | 1.121,417 | 4,486 |
| 8 | 1 | 0,118161 | 2.115,761 | 8,463 |
| 8 | 2 | 0,111517 | 2.241,804 | 8,967 |

### Análise

Os resultados demonstram uma redução no tempo de execução à medida que o número de processos MPI aumenta. A configuração com 8 processos MPI e 1 thread por processo apresentou um tempo de execução aproximadamente **67,6% menor** que a configuração sequencial.

Ao utilizar 8 processos MPI com 2 threads OpenMP por processo, houve uma redução adicional de aproximadamente **5,6%** no tempo de execução em relação à configuração com 8 processos MPI e 1 thread por processo.

Esses resultados demonstram como o paralelismo pode melhorar o desempenho de simulações científicas. Entretanto, como os testes utilizaram um sistema de 4.000 átomos e 250 passos, os resultados representam uma avaliação inicial e podem variar em simulações maiores.

### Conclusão

O experimento evidencia a utilidade da computação de alto desempenho (HPC) no LAMMPS, permitindo acelerar simulações por meio da distribuição dos cálculos entre múltiplos processos e threads. Os resultados também mostram que o ganho de desempenho depende da configuração de paralelismo utilizada e das características da simulação.
