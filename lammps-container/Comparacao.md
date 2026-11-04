

# Comparação de Desempenho

O arquivo de entrada utilizado em todos os cinco testes foi o `in.friction`

## Resultados de Desempenho

| Ambiente de execução | Tempo do loop (s) ↓ | Timesteps/s ↑ | Matom-step/s ↑ | Redução do tempo em relação ao nativo | Aumento de throughput em relação ao nativo |
|---|---:|---:|---:|---:|---:|
| LAMMPS nativo (sem container) | 1.50547 | 13,284.887 | 22.903 | +0.00% | +0.00% |
| Apptainer (configuração manual) | 1.45820 | 13,715.536 | 23.646 | +3.24% | +3.24% |
| Docker (configuração manual) | 1.44147 | 13,874.762 | 23.920 | +4.44% | +4.44% |
| Apptainer (gerado pelo HPCCM) | 1.41944 | 14,090.096 | 24.291 | +6.06% | +6.06% |
| Docker (gerado pelo HPCCM) | 1.36682 | 14,632.464 | 25.226 | +10.14% | +10.14% |

## Interpretação dos resultados

O Docker gerado pelo HPCCM apresentou o melhor desempenho entre os ambientes avaliados, registrando o menor tempo de execução (*loop time*), de 1.36682 segundos, e a maior taxa de processamento (*throughput*), de 14,632.464 timesteps/s.

Em comparação com a execução nativa do LAMMPS, essa configuração apresentou uma redução de aproximadamente **9,21% no tempo de execução** e um aumento de **10,14% na taxa de processamento**.

As imagens de Docker e Apptainer construídas manualmente também apresentaram resultados superiores aos da execução nativa, embora com ganhos mais modestos. Já as imagens geradas pelo HPCCM demonstraram ganhos de desempenho ainda maiores.

De maneira geral, todos os ambientes conteinerizados apresentaram desempenho superior ao LAMMPS executado diretamente no sistema, sem container. Entre as configurações testadas, o Docker gerado pelo HPCCM obteve os melhores resultados.

# Comparação do Tamanho das Imagens

| Ambiente de execução | Método de construção | Tamanho da imagem |
|---|---|---:|
| Apptainer | Arquivo `.def` escrito manualmente | 454.060 bytes (≈ 443,42 KiB) |
| Apptainer | Arquivo `.def` gerado pelo HPCCM | 454.068 bytes (≈ 443,43 KiB) |
| Docker | Dockerfile escrito manualmente | 1,98 GB |
| Docker | Dockerfile gerado pelo HPCCM | 1,98 GB |
