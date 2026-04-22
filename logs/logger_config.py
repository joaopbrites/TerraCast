import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from systemd import journal


def config_journal_handler():
    journal_handler = journal.JournalHandler()
    journal_handler.setLevel(logging.DEBUG)
    return journal_handler

def setup_logger(level, jounal = True):
    logging_processament = logging.getLogger("processment")
    logging_processament.setLevel(level)
    if(jounal):
        logging_processament.addHandler(config_journal_handler())

    logging_processament.debug(f"Log de nível {level} inicializado")

    return logging_processament



if __name__ == "__main__":
    setup_logger(level, file,  jounal)
