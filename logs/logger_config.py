import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from systemd import journal

FORMATTER = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')



def config_file_handler():
    caminho_arquivo = Path(Path.cwd() / "logs" / "files" / "processament.log")
    caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)
    file_handler = RotatingFileHandler(
        caminho_arquivo,
        maxBytes=10*1024*1024,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(FORMATTER)
    return file_handler

def config_journal_handler():
    journal_handler = journal.JournalHandler()
    journal_handler.setLevel(logging.DEBUG)
    return journal_handler

def setup_logger(level:int,file:bool = True,  jounal:bool = False):
    logging_processament = logging.getLogger("processment")
    logging_processament.setLevel(level)
    if(file):
        logging_processament.addHandler(config_file_handler())

    if(jounal):
        logging_processament.addHandler(config_journal_handler())

    logging_processament.info("Log inicializado")



if __name__ == "__main__":
    setup_logger(level, file,  jounal)
