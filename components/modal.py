import streamlit as st
from config.apps_config import CATEGORY_COLORS

@st.dialog("App Details", width="large")
def show_details_modal(app_data):
    """
    Clean, professional details modal.
    """
    
    # Header
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 24px;">
        <div style="width: 56px; height: 56px; background: #fafafa; border: 1px solid #eaeaea; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 28px;">
            {app_data['icon']}
        </div>
        <div>
            <h2 style="margin: 0; font-size: 20px; font-weight: 600; color: #171717;">{app_data['name']}</h2>
            <p style="margin: 4px 0 0 0; font-size: 14px; color: #666666;">{app_data['category']} · {app_data['difficulty']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Description
    st.markdown(f"""
    <div style="margin-bottom: 24px;">
        <h4 style="font-size: 12px; font-weight: 600; color: #888888; text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 8px 0;">About</h4>
        <p style="font-size: 14px; color: #444444; line-height: 1.6; margin: 0;">{app_data['detailed_description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tech Stack
    st.markdown(f"""
    <div style="margin-bottom: 24px;">
        <h4 style="font-size: 12px; font-weight: 600; color: #888888; text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 12px 0;">Technologies</h4>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            {"".join([f'<span style="font-size: 12px; font-weight: 500; color: #666; background: #f5f5f5; padding: 6px 12px; border-radius: 6px; border: 1px solid #eaeaea;">{tech}</span>' for tech in app_data['tech_stack']])}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Metadata
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div style="background: #fafafa; border: 1px solid #eaeaea; border-radius: 8px; padding: 12px;">
            <p style="font-size: 11px; color: #888; text-transform: uppercase; margin: 0 0 4px 0;">Added</p>
            <p style="font-size: 14px; color: #171717; font-weight: 500; margin: 0;">{app_data['date_added']}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div style="background: #fafafa; border: 1px solid #eaeaea; border-radius: 8px; padding: 12px;">
            <p style="font-size: 11px; color: #888; text-transform: uppercase; margin: 0 0 4px 0;">Updated</p>
            <p style="font-size: 14px; color: #171717; font-weight: 500; margin: 0;">{app_data['last_updated']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)
    
    # Launch button
    launch_url = app_data['launch_url']
    if launch_url.startswith('http'):
        st.link_button("Open Application →", launch_url, use_container_width=True)
    else:
        if st.button("Open Application →", key=f"modal_launch_{app_data['id']}", use_container_width=True):
            st.switch_page(launch_url)
