import logging
import azure.functions as func
import os

app = func.FunctionApp()

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger_hello(myTimer: func.TimerRequest) -> None:
    servidor = os.getenv("SQL_HOST")
    banco_dados = os.getenv("SQL_DATABASE")
    usuario = os.getenv("SQL_USER")
    senha = os.getenv("SQL_PASSWORD")

    logging.info(f"Servidor: {servidor}")
    logging.info(f"Banco de Dados: {banco_dados}")
    logging.info(f"Usuário: {usuario}")




