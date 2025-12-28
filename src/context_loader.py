
import re
import yaml
from pathlib import Path
from typing import Any, Dict, List

PRODUCT_MD = Path(__file__).resolve().parent.parent / '.kiro' / 'product.md'

YAML_BLOCK_RE = re.compile(r"```yaml\s*(.*?)\s*```", re.DOTALL)

class LocalContext:
    def __init__(self, raw_md: str, parts: Dict[str, Any]):
        self.raw_md = raw_md
        self.parts = parts

    def get(self, key: str, default=None):
        return self.parts.get(key, default)


def _parse_yaml_blocks(md: str) -> Dict[str, Any]:
    blocks = YAML_BLOCK_RE.findall(md)
    merged: Dict[str, Any] = {}
    for b in blocks:
        data = yaml.safe_load(b) or {}
        # merge top-level keys
        for k, v in data.items():
            if k in merged and isinstance(merged[k], list) and isinstance(v, list):
                merged[k].extend(v)
            elif k in merged and isinstance(merged[k], dict) and isinstance(v, dict):
                merged[k].update(v)
            else:
                merged[k] = v
    return merged


def load_context() -> LocalContext:
    md = PRODUCT_MD.read_text(encoding='utf-8')
    parts = _parse_yaml_blocks(md)
    return LocalContext(md, parts)


def slang_map(ctx: LocalContext) -> Dict[str, str]:
    slang_items = ctx.get('slang', [])
    mapping = {}
    for item in slang_items:
        w = str(item.get('word', '')).strip().lower()
        meaning = str(item.get('meaning', '')).strip()
        if w:
            mapping[w] = meaning
    return mapping


def traffic_rules(ctx: LocalContext) -> Dict[str, Any]:
    return ctx.get('traffic', {})


def food_tips(ctx: LocalContext) -> Dict[str, Any]:
    return ctx.get('food', {})


def safety_info(ctx: LocalContext) -> Dict[str, Any]:
    return ctx.get('safety', {})
