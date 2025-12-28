
from src.context_loader import load_context, slang_map, traffic_rules

def test_context_parsing():
    ctx = load_context()
    assert 'slang' in ctx.parts
    assert slang_map(ctx).get('pakka') == 'sure'
    assert isinstance(traffic_rules(ctx).get('peak_hours'), list)
