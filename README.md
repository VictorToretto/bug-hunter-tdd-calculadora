# Bug Hunter & TDD Calculator

Atividade da disciplina **Alta Qualidade em Software** (Ciência de Dados e Inteligência Artificial).

Objetivo: analisar uma calculadora científica simples em Python, encontrar e documentar os defeitos, e corrigir um deles usando **TDD** (Test-Driven Development) com o framework `unittest`, com versionamento no Git/GitHub.

## Estrutura

| Arquivo | Conteúdo |
|---------|----------|
| `Calculadora.py` | Código da calculadora (com o Bug #1 corrigido) |
| `test_calculadora.py` | Testes automatizados com `unittest` (13 testes) |
| `Bugs.md` | Relatório detalhado de cada bug encontrado |
| `evidencias/` | Vídeo e print do Bug #1 e saídas dos testes em cada fase do TDD |
| `requirements.txt` | Dependências (NumPy) |

## Como rodar

```bash
pip install -r requirements.txt
python Calculadora.py
```

Para rodar os testes:

```bash
python -m unittest -v
```

(os testes também rodam com `pytest`, se estiver instalado)

## Andamento

- [x] Copiar o código para o repositório local
- [x] Identificar os bugs e criar o relatório (`Bugs.md`): 9 bugs encontrados
- [x] Preparar o código para os testes (importar as funções sem abrir o menu)
- [x] Escrever um teste que falha para o bug escolhido (Bug #1, adição): 7 testes, 7 falhas
- [x] Corrigir o bug (teste passando): 7 de 7
- [x] Refatorar e rodar todos os testes: 13 de 13
- [x] Documentar a correção e fazer a reflexão com Scrum

## TDD aplicado ao Bug #1 (adição)

O bug: `adicao(x, y)` fazia `return x + np.add(x, y)`, ou seja, somava o `x` duas vezes (`2 + 3 = 7`). Detalhes no [Bugs.md](Bugs.md#bug-1-adição-soma-o-primeiro-número-duas-vezes).

| Fase | O que eu fiz | Resultado | Commit |
|------|--------------|-----------|--------|
| Preparação | Adicionei `if __name__ == "__main__":` no final do arquivo, porque sem isso o menu abria quando o teste importava as funções | Import funciona sem abrir o menu | `test: prepara o código para os testes` |
| 🔴 Vermelho | Escrevi 7 testes em `TestAdicao` com o comportamento esperado, **sem mexer no código** | 7 falhas (`7 != 5`) ([log](evidencias/tdd_vermelho.txt)) | `test(red): ...` |
| 🟢 Verde | Correção mínima: `return np.add(x, y)` | 7 de 7 passando ([log](evidencias/tdd_verde.txt)) | `fix(green): ...` |
| 🔵 Refatorar | Troquei por `return x + y` (igual à `subtracao`), coloquei docstring e criei testes de regressão das outras operações | 13 de 13 passando ([log](evidencias/tdd_refatoracao.txt)) | `refactor: ...` |

O histórico de commits mostra essa ordem: `git log --oneline`.

**Por que refatorar para `x + y`?** O `np.add` não era necessário para somar dois números, e ele devolvia tipos do NumPy (`np.float64`) em vez do `float` normal do Python, diferente da `subtracao`. Com `x + y` o código fica mais simples e consistente. Os testes garantiram que o comportamento não mudou.

**Testes de regressão:** para garantir que a correção não introduziu novos bugs, adicionei testes para subtração, multiplicação, divisão (com divisor diferente de zero), potência e raiz quadrada de número positivo. Não testei as operações que ainda têm bug (fatorial, logaritmos, trigonometria), porque elas continuam abertas no relatório e falhariam por outro motivo.

**Revisão de código:** a atividade era individual, então não tive um colega para revisar. No lugar, conferi este checklist:
- [x] O teste falhou antes da correção e passou depois
- [x] Só a função `adicao` foi alterada no código da calculadora
- [x] Todos os testes passam depois da refatoração
- [x] O programa continua funcionando pelo menu (`1`, `2`, `3` → `Resultado: 5.0`)

## Reflexão usando o framework Scrum

Mesmo trabalhando sozinho, tentei organizar a atividade como se fosse um Scrum em miniatura. Assumi os três papéis: Product Owner (decidir o que é mais importante), Scrum Master (cuidar do processo) e time de desenvolvimento.

**Product Backlog:** a lista de bugs do `Bugs.md` virou o backlog. Cada bug tem severidade, e usei isso para priorizar. Os críticos (log natural, cosseno, tangente) quebram o programa. Escolhi a adição porque é a operação mais básica e usada da calculadora e dá resultado errado *sem avisar*, o que é perigoso. Também é um bug pequeno e bem delimitado, bom para praticar o ciclo de TDD do começo ao fim.

**Sprint:** a sprint teve três blocos de trabalho:
1. **Bloco 1:** montar o repositório e fazer a caça aos bugs com o relatório (o "refinamento" do backlog).
2. **Bloco 2:** preparar o ambiente de testes e escrever os testes vermelhos.
3. **Bloco 3:** corrigir, refatorar e documentar.

**Meta da sprint:** "A soma da calculadora está correta e coberta por testes automatizados."

**Daily:** antes de cada bloco eu revisava o que já tinha feito e o que faltava. O que me travou foi na hora de rodar os testes: quando o teste importava a calculadora, o menu abria e ficava esperando eu digitar. Pesquisei e descobri que dava pra resolver colocando a chamada do menu dentro de `if __name__ == "__main__":`.

**Definition of Done:** considerei o Bug #1 pronto quando: (1) existe teste automatizado que reproduz o bug; (2) o teste passa; (3) todos os outros testes passam; (4) o relatório foi atualizado com o status; (5) o código está no GitHub.

**Sprint Review:** o incremento entregue foi a adição corrigida, 13 testes automatizados e um relatório com 9 bugs documentados. O bug escolhido foi resolvido; os outros 8 continuam no backlog para as próximas sprints.

**Retrospectiva:**
- *O que funcionou:* escrever o teste antes ajudou a ter certeza do que era "certo" antes de mexer no código. Ver os testes passarem de vermelho para verde dá confiança de que a correção resolveu mesmo. Fazer commits pequenos deixou o histórico fácil de entender.
- *O que poderia melhorar:* eu poderia ter usado o GitHub Issues para cada bug em vez de só um arquivo Markdown, o que deixaria o acompanhamento mais parecido com um time real. Também faltou revisão por outra pessoa.
- *Aprendizado:* o código original não foi pensado para ser testado (o menu abria quando o arquivo era importado). Pensar em testes desde o começo influencia como o código é escrito.

**Próximas sprints (backlog restante, por prioridade):** Bugs #4, #7 e #8 (críticos, derrubam o programa) → #2, #3 e #5 (resultados errados ou travamento) → #6 e #9.
