# Astromer/Airflow

Instalar astro cli

```
astro dev init
astro dev start ou stop
```

## Airflow
Retry, Orquestração, Varios pipelines para monitorar\
Tasks na ordem correta 
- Interativo
- Escalavel 
- Customizavel 

### Componentes principais
<b> - Webserver </b>\
<b> - Scheduler </b>\
<b> - Metadata Database </b>\
<b> - Executores (<i>como </i> a task será executada) [HOW]</b>\
<b> - Worker [WHERE] </b>

### Exemplos de arquitetura
- One Node
  - Tudo dentro do mesmo nó
- Multi Node
  - Vários nós com as diversas aplicações (nesse caso, precisamos de um Redis)
  - Nós diferentes para os workers

### Conceitos principais
- DAG: pipeline
- Operators: é uma task na DAG
  - Action operator: executa algo
  - Transfer operator: permite transferir dados
  - Senson operator: sensor que aguarda algo acontecer antes de mover para a próxima ação da dag.
- Task: instancia de um operador
  - Task Instance: DAG + Task + Ponto no tempo
- Dependências: << ou >>
- Workflow: combinação de tudo 

### Interação com airflow
- UI
- CLI
- Rest API