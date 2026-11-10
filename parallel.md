# Desafio 01: Pensando em paralelo

```
/* Reset the histogram */
for (int j=0; j<ALPHA_LEN; j++) {
    hist[j] = 0;
}

/* Count occurrences in parallel */
int len = TEXT_LEN / WORKER_COUNT;

parallel for(int i = 0; i < WORKER_COUNT; i++) {
    int start = i * len;
    for(int j = 0; j < len; j++) {
        const char c = text[j + start];
        if (isalpha(c)) {
            const int idx = tolower(c) - 'a';

            critical {
                nlet++;
                hist[idx]++;
            }
        }
    }
}

for(int i = len * WORKER_COUNT; i < TEXT_LEN; i++) {
    const char c = text[i];
    if (isalpha(c)) {
        const int idx = tolower(c) - 'a';
        nlet++;
        hist[idx]++;
    }
}
```
### 1. Decomposição

O texto é dividido em quatro partes, cada uma atribuída a um trabalhador. Dessa forma, os quatro trabalhadores podem percorrer suas respectivas partes simultaneamente, contabilizando as ocorrências de cada letra.

Caso o tamanho do texto não seja divisível pelo número de trabalhadores, os caracteres restantes são processados posteriormente, de forma sequencial.

### 2. Dependências e sincronização

Os trabalhadores podem executar suas tarefas de maneira independente, pois cada um é responsável por uma parte diferente do texto.

Entretanto, todos acessam as mesmas estruturas de dados (`hist` e `nlet`). Caso dois ou mais trabalhadores tentem modificar essas variáveis simultaneamente, podem ocorrer condições de corrida (*race conditions*), comprometendo o resultado da execução.

Portanto, é necessário utilizar mecanismos de sincronização para controlar o acesso a essas variáveis compartilhadas.

### 3. Desempenho

Neste problema, não seria esperado obter um ganho de desempenho de quatro vezes ao utilizar quatro trabalhadores.

Isso ocorre porque o acesso às variáveis compartilhadas (`hist` e `nlet`) pode exigir sincronização, fazendo com que alguns trabalhadores tenham que esperar enquanto outros realizam suas operações.
