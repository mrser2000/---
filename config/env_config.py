from dataclasses import dataclass
from typing import Optional

@dataclass
class EnvConfig:
    base_url: str = "https://www.chitai-gorod.ru/"
    ui_timeout: int = 10
    headless: bool = True
    mode: str = "ALL"  # UI, API, ALL
    token_api: Optional[str] = None  

env = EnvConfig()