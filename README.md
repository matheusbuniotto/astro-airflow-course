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

### Dags Exemplos
Por deafult o período da DAG é rodar diariamente (a cada 24h)
2 Parâmetros que obrigatóriamente precisamos definir
``` 
- start_date
- schedule_interval
- (opcional) end_date
``` 
Exemplo:\
<code>
<b>Primeira execução = start_date + schedule_interval</b>\
start_date: 01/01/2022 às 10h \
schedule_interval: 10 min\
A primeira execução será no dia 01/01 às 10h10\
- Novas DAGS Runs
Então o start_date se torna o execution_date e o 01/01 10h10 se torna o start_date
</code>

Os datetime por padrão são em UTC.
Por padrão todas as dags não executadas entre o dia atual e o start date serão executadas quando o start_date for no passado. 
Não devemos colocar uma data dinâmica, exemplo datetime.now()


### Schedule
Padrões do airflow:
- "@daily"
- "@weekly"
- "@monthly"
- None (nunca é ativada automaticamente, somente manual ou por algum operador externo)

#### Cron Ref.
https://crontab.guru/

#### Time Delta
Define a exeução a cada intervalo RELATIVO, exemplo: schedule_interval = timedelta(hours=1)
- Executa a DAG a cada 7h

### Backfill 
Por padrão o airflow irá executar as DAGs que não foram executadas entre o start_date e a data atual.
``` 
catchup=False or True
``` 
Podemos limitar o número de dags runs ativas. com max_active_runs = N

#### Best Pratices
Catchup False e usar backfill com terminal 

 ou

Catchup True com max dags runs 

### Operators
Dividir as tasks entre operadores diferentes, removendo as dependências em caso de falha em uma das tasks.

1 operador -> 1 task 
Todas tasks precisam ter um ID único
Retry N vezes antes de considerar a dag falha

Definir os args para todos os operadores

### Executando funções Python 
`from airflow.operators.python import PythonOperator`

acessar o contexto da execução:
**kwargs


### Bash Operator
`from airflow.operators.bash import BashOperator`


## Orquestração

### Sensor
`from airflow.sensors.filesystem import FileSensor`

### Dependências
```
upstream = X.set_upstream(Y) -> execute Y antes de X\
downstream = X.set_downstream(Y)-> execute X antes de Y\
```

<b>Outra opção mais fácil e clara:</b>

```
X >> Y = execute X depois Y
X << Y 
X >> [Y, Z] = Eecute X antes de Y e Z
```

#### Helpers:
`from airflow.models.baseoperator import chain, cross_downstream`

- Chain: 
  - chain(X,Y,Z) = x >> y >> z

- Cross_downstream
  - cross_downstream([X,Y], [Z,K])\
Não é possível usar [X,Y] >> [Z,K]