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

### Comandos úteis
executar o bash em um container
`$ docker exec -it e23c9fd919ac /bin/bash`

no airflow
```
airflow db init
airflow db up
airflow db reset (remove tudo do db)
airflow webserver
airflow scheduler
airflow celery worker
airflow dags pause ou unpause (semelhante ao botão da UI)
airflow dags trigger
airflow dags list
airflow dags list <nome>
airflow tasks test (executar um teste em task específica)
airflow dags backfill -s[start] -e[end] <nome/id da dag>(rerun as dags que não foram pausadas) 
``` 