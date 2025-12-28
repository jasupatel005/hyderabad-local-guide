
import streamlit as st
import datetime as dt
from typing import List

from context_loader import load_context, slang_map, traffic_rules, food_tips, safety_info

st.set_page_config(page_title='Hyderabad Local Guide', page_icon='🧭', layout='centered')

ctx = load_context()
slang = slang_map(ctx)
traffic = traffic_rules(ctx)
food = food_tips(ctx)
safety = safety_info(ctx)

st.title('🧭 Hyderabad Local Guide')
st.caption('Agent-steered by /.kiro/product.md — built for The Local Guide Challenge')

with st.sidebar:
    st.header('Tools')
    tool = st.radio('Choose a tool', ['Slang Translator', 'Traffic Estimator', 'Local Tips'])
    st.divider()
    st.markdown('**Context Source:** `/.kiro/product.md`')

if tool == 'Slang Translator':
    st.subheader('🗣️ Slang Translator')
    text = st.text_area('Enter Hyderabad slang or sentence:', 'That bandi has mast dosas, pakka we go tonight!')
    if st.button('Translate'):
        out_words: List[str] = []
        for w in text.split():
            key = w.strip(',.!?').lower()
            meaning = slang.get(key)
            out_words.append(meaning if meaning else w)
        st.success(' '.join(out_words))
        st.info('Translations are context-driven from `product.md`. Update the slang list there to steer outputs.')


elif tool == 'Traffic Estimator':
    st.subheader('🚦 Traffic Estimator')
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        area = st.selectbox(
            'Area',
            [
                'Hitec City','Madhapur','Gachibowli','Financial District','Kondapur',
                'Jubilee Hills','Charminar','Mehdipatnam','Nampally','Mallepally',
                'Uppal','Nacharam','Necklace Road','LB Nagar','Ameerpet','Dilsukhnagar'
            ]
        )

    # Streamlit doesn't have datetime_input; use date_input + time_input
    default_dt = dt.datetime.now()
    with col2:
        date_sel = st.date_input('Date', default_dt.date())

    with col3:
        time_sel = st.time_input('Time', default_dt.time())

    # Compose a single datetime from date + time
    when = dt.datetime.combine(date_sel, time_sel)

    def estimate(area: str, when: dt.datetime):
        dow = when.strftime('%a')
        hm = when.strftime('%H:%M')
        sev = 'low'
        notes = []
        # Peak hours
        for ph in traffic.get('peak_hours', []):
            days = ph.get('days', [])
            start = ph.get('start', '00:00')
            end = ph.get('end', '00:00')
            hotspots = ph.get('hotspots', [])
            if dow[:3] in [d[:3] for d in days] and start <= hm <= end and area in hotspots:
                sev = 'high'
                notes.append(f"Peak window: {ph['name']}")
        # Event overrides
        for ev in traffic.get('event_overrides', []):
            if area in ev.get('locations', []):
                sev = max(sev, ev.get('severity', 'medium'),
                          key=lambda x: ['low', 'medium', 'high'].index(x))
                notes.append(f"Event: {ev.get('match')} active")
        # Road notes
        for rn in traffic.get('road_notes', []):
            if area.lower() in rn.get('road', '').lower():
                notes.append(rn.get('notes'))
        return sev, notes

    if st.button('Estimate Traffic'):
        sev, notes = estimate(area, when)
        badge = {'low': '🟢 Low', 'medium': '🟡 Medium', 'high': '🔴 High'}
        st.write(f"**Severity**: {badge.get(sev, sev)}")
        if notes:
            st.write('**Notes:**')
            for n in notes:
                st.write(f"- {n}")
        st.info('Rules sourced from `product.md`. Modify YAML blocks to steer behavior.')


else:
    st.subheader('🍲 Local Tips')
    st.write('Food & culture recommendations (from `product.md`).')
    st.write('**Irani Chai Spots**')
    for s in food.get('irani_chai_spots', []):
        st.write(f"- {s}")
    st.write('**Biryani Favorites**')
    for s in food.get('biryani_favorites', []):
        st.write(f"- {s}")
    st.write('**Tiffin Centres**')
    for s in food.get('tiffins', []):
        st.write(f"- {s}")
    st.write('**Veg Options**')
    for s in food.get('veg_options', []):
        st.write(f"- {s}")
    st.divider()
    st.write('**Safety**')
    
    st.write('**Emergency Numbers**')
    emergency = safety.get('emergency_numbers', {})
    for k, v in emergency.items():
        st.write(f"- **{k.capitalize()}**: {v}")

    st.write('**Safety Notes**')
    for note in safety.get('notes', []):
        st.write(f"- {note}")

    st.caption('Edit `/.kiro/product.md` to refine tips, add places, or update safety info.')
