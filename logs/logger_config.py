import logging
from logging import FileHandler
from logging.handlers import RotatingFileHandler
from pathlib import Path
from systemd import journal

FORMATTER = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


    
## Novo nivel e handler para registrar os arquivos que vão ser processados 
# configura nivel e adiciona a classe Logger
AUDIT = 15
logging.addLevelName(AUDIT, "AUDIT")
#adiciona uma função a classe logger para lidar com a chamada .audit
def audit(self, message, *args, **kwargs):
    if self.isEnabledFor(AUDIT):
        self._log(AUDIT, message, args, **kwargs)
logging.Logger.audit = audit

# FUNÇÃO GAMBIARRA PRO LOG PRINCIPAL NÃO PEGAR AUDDIT
def filter_no_audit():  
        return lambda record: record.levelno != AUDIT

#configura arquivo separado para gravação dos arquivos que serão processados
def config_audit_handler():
    """Handler separado só para nível AUDIT — grava em arquivo dedicado."""
    caminho_arquivo = Path(__file__).resolve().parent / "files" / "products_audit.log"
    caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)
    audit_handler = FileHandler(
        caminho_arquivo,
        mode='w',           # <-- 'w' sobrescreve; 'a' (default) faz append
        encoding='utf-8'
    )
    audit_handler.setLevel(AUDIT)
    # Filtro para aceitar SOMENTE nível AUDIT
    audit_handler.addFilter(lambda record: record.levelno == AUDIT)
    audit_handler.setFormatter(FORMATTER)
    return audit_handler
    # Filtro para excluir logs AUDIT de handlers que não são do audit

def config_file_handler():
    caminho_arquivo = Path(Path(__file__).resolve().parent.parent / "logs" / "files" / "processament.log")
    caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)
    file_handler = RotatingFileHandler(
        caminho_arquivo,
        maxBytes=10*1024*1024,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.addFilter(filter_no_audit())
    file_handler.setFormatter(FORMATTER)
    return file_handler

def config_journal_handler():
    journal_handler = journal.JournalHandler()
    journal_handler.setLevel(logging.DEBUG)
    journal_handler.addFilter(filter_no_audit())
    return journal_handler

def setup_logger(level, file = True, jounal = False):
    logging_processament = logging.getLogger("processment")
    logging_processament.setLevel(level)
    if(file):
        logging_processament.addHandler(config_file_handler())
    if(jounal):
        logging_processament.addHandler(config_journal_handler())

    logging_processament.addHandler(config_audit_handler())

    logging_processament.info(f"Log de nível {level} inicializado")

    return logging_processament



if __name__ == "__main__":
    setup_logger(level, file,  jounal)
