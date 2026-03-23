from datetime import date, timedelta, datetime
from pathlib import Path
import json


class ControllerProducts:
    """Gerencia estado de arquivos processados/falhados."""

    def __init__(self, days_to_load: int = 3):
        self.base_path = Path(__file__).resolve().parent.parent
        self.log_dir = self.base_path / "logs" / "files"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        self.days_to_load = days_to_load
        self.processed: dict[str, float] = {}  # key -> timestamp
        self.failed: dict[str, dict] = {}

        
        self._load_recent_days()

    def _processed_path(self, d: date) -> Path:
        return self.log_dir / f"processed_{d.isoformat()}.json"

    def _failed_path(self, d: date) -> Path:
        return self.log_dir / f"failed_{d.isoformat()}.json"

    def _load_recent_days(self):
        """Carrega últimos N dias em memória."""
        today = date.today()
        for i in range(self.days_to_load):
            d = today - timedelta(days=i)
            
            # Carrega processados
            p = self._processed_path(d)
            if p.exists():
                with open(p, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.processed.update(data)

            # Carrega falhados
            failed_path = self._failed_path(d)
            if failed_path.exists():
                with open(failed_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.failed.update(data)
            

    def _save_processed_today(self):
        """Persiste dict de processados do dia atual."""
        today = date.today()
        p = self._processed_path(today)

        # Filtra apenas entradas de hoje
        today_data = {
            key: value
            for key, value in self.processed.items()
            if isinstance(value, (int, float)) and datetime.fromtimestamp(value).date() == today
        }
        
        # Para simplificar, salva tudo que foi adicionado durante esta execução
        if p.exists():
            with open(p, "r", encoding="utf-8") as f:
                existing = json.load(f)
            existing.update(today_data)
            today_data = existing
        
        with open(p, "w", encoding="utf-8") as f:
            json.dump(today_data, f, indent=2)

    def _save_failed_today(self):
        """Persiste dict de falhados do dia atual."""
        today = date.today()
        p = self._failed_path(today)
        failed = dict(self.failed)

        if p.exists():
            with open(p, "r", encoding="utf-8") as f:
                existing = json.load(f)
            existing.update(failed)
            failed = existing
        
        with open(p, "w", encoding="utf-8") as f:
            json.dump(failed, f, indent=2)

    def is_processed(self, key: str) -> bool:
        """Verifica se arquivo já foi processado. O(1)."""
        return key in self.processed


    def mark_processed(self, key: str):
        """Marca arquivo como processado e persiste."""
        self.processed[key] = datetime.now().timestamp()
        
        # Remove de failed se existia
        if key in self.failed:
            del self.failed[key]
        
        self._save_processed_today()

    def mark_failed(self, key: str, error: str = ""):
        """Marca arquivo como falhado com contexto de erro."""
        self.failed[key] = {
            "timestamp": datetime.now().timestamp(),
            "error": error
        }
        self._save_failed_today()






    


