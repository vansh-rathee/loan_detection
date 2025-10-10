#!/usr/bin/env python3
"""
Streamlit Frontend for Loan Default Predictor
3D Interactive Interface with Animations
"""

import streamlit as st
import time
import math
from simple_loan_predictor import predict_loan_default
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Page configuration
st.set_page_config(
    page_title="🏦 Loan Approval System",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for 3D effects and animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        transform: perspective(1000px) rotateX(5deg);
        font-family: 'Poppins', sans-serif;
    }
    
    .main-header h1 {
        color: white;
        font-size: 3rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        font-weight: 700;
    }
    
    .main-header p {
        color: #f0f0f0;
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
        font-weight: 300;
    }
    
    .approval-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 15px 35px rgba(17, 153, 142, 0.4);
        transform: perspective(1000px) rotateY(-5deg);
        animation: approvalPulse 2s infinite;
    }
    
    .rejection-card {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 15px 35px rgba(255, 107, 107, 0.4);
        transform: perspective(1000px) rotateY(5deg);
        animation: rejectionShake 1s ease-in-out;
    }
    
    .result-text {
        color: white;
        font-size: 2rem;
        font-weight: 600;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        font-family: 'Poppins', sans-serif;
    }
    
    .party-popper {
        font-size: 4rem;
        animation: partyBounce 0.6s ease-in-out infinite alternate;
        display: inline-block;
        margin: 0 10px;
    }
    
    .sad-emoji {
        font-size: 3rem;
        animation: sadFloat 2s ease-in-out infinite;
        display: inline-block;
    }
    
    @keyframes approvalPulse {
        0%, 100% { transform: perspective(1000px) rotateY(-5deg) scale(1); }
        50% { transform: perspective(1000px) rotateY(-5deg) scale(1.02); }
    }
    
    @keyframes rejectionShake {
        0%, 100% { transform: perspective(1000px) rotateY(5deg) translateX(0); }
        25% { transform: perspective(1000px) rotateY(5deg) translateX(-5px); }
        75% { transform: perspective(1000px) rotateY(5deg) translateX(5px); }
    }
    
    @keyframes partyBounce {
        0% { transform: translateY(0) rotate(0deg); }
        100% { transform: translateY(-20px) rotate(10deg); }
    }
    
    @keyframes sadFloat {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transform: perspective(1000px) rotateX(2deg);
    }
    
    .input-section {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(240, 147, 251, 0.3);
        transform: perspective(1000px) rotateX(-2deg);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-size: 1.2rem;
        font-weight: 600;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        transform: perspective(1000px) rotateZ(-1deg);
        transition: all 0.3s ease;
        font-family: 'Poppins', sans-serif;
    }
    
    .stButton > button:hover {
        transform: perspective(1000px) rotateZ(-1deg) translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
</style>
""", unsafe_allow_html=True)

def create_3d_risk_visualization(probability, risk_level):
    """Create 3D visualization of risk assessment"""
    
    # Create 3D sphere representing risk
    fig = go.Figure()
    
    # Create sphere data
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Color based on risk level
    if risk_level == "Low Risk":
        color = "green"
        opacity = 0.3 + probability * 0.7
    elif risk_level == "Medium Risk":
        color = "orange" 
        opacity = 0.4 + probability * 0.6
    elif risk_level == "High Risk":
        color = "red"
        opacity = 0.5 + probability * 0.5
    else:  # Very High Risk
        color = "darkred"
        opacity = 0.6 + probability * 0.4
    
    fig.add_trace(go.Surface(
        x=x, y=y, z=z,
        colorscale=[[0, color], [1, color]],
        opacity=opacity,
        showscale=False
    ))
    
    # Add risk indicator particles
    n_particles = int(probability * 100)
    if n_particles > 0:
        particle_x = np.random.uniform(-2, 2, n_particles)
        particle_y = np.random.uniform(-2, 2, n_particles)
        particle_z = np.random.uniform(-2, 2, n_particles)
        
        fig.add_trace(go.Scatter3d(
            x=particle_x, y=particle_y, z=particle_z,
            mode='markers',
            marker=dict(
                size=3,
                color=color,
                opacity=0.6
            ),
            name="Risk Particles"
        ))
    
    fig.update_layout(
        title=f"3D Risk Visualization - {risk_level}",
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y", 
            zaxis_title="Z",
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.5)
            ),
            bgcolor="rgba(0,0,0,0)",
            xaxis=dict(showgrid=False, showbackground=False),
            yaxis=dict(showgrid=False, showbackground=False),
            zaxis=dict(showgrid=False, showbackground=False)
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=400
    )
    
    return fig

def create_probability_gauge(probability):
    """Create 3D-style probability gauge"""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = probability * 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Default Probability (%)"},
        delta = {'reference': 50},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 25], 'color': "lightgreen"},
                {'range': [25, 50], 'color': "yellow"},
                {'range': [50, 75], 'color': "orange"},
                {'range': [75, 100], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 60
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        height=300
    )
    
    return fig

def show_approval_animation():
    """Show party popper animation for approval"""
    st.markdown("""
    <div class="approval-card">
        <div class="party-popper">🎉</div>
        <div class="party-popper">🎊</div>
        <div class="party-popper">🥳</div>
        <div class="result-text">LOAN APPROVED!</div>
        <p style="color: white; font-size: 1.2rem; margin-top: 1rem;">
            Congratulations! Your loan application has been approved! 🎉
        </p>
        <div class="party-popper">🎈</div>
        <div class="party-popper">🍾</div>
        <div class="party-popper">✨</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add balloons effect
    st.balloons()

def show_rejection_message():
    """Show sorry message for rejection"""
    st.markdown("""
    <div class="rejection-card">
        <div class="sad-emoji">😔</div>
        <div class="result-text">LOAN NOT APPROVED</div>
        <p style="color: white; font-size: 1.2rem; margin-top: 1rem;">
            Sorry, better luck next time! 💙<br>
            Consider improving your credit profile and try again.
        </p>
        <div class="sad-emoji">🙏</div>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Main Streamlit application"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🏦 3D Loan Approval System</h1>
        <p>Advanced AI-Powered Credit Risk Assessment</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for inputs
    with st.sidebar:
        st.markdown("""
        <div class="input-section">
            <h2 style="color: white; text-align: center; margin-bottom: 1rem;">📝 Loan Application</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Customer information inputs
        age = st.slider("👤 Age", min_value=18, max_value=80, value=35, help="Applicant's age")
        campaign = st.slider("📞 Campaign Contacts", min_value=1, max_value=10, value=2, help="Number of contacts during campaign")
        pdays = st.slider("📅 Days Since Last Contact", min_value=0, max_value=999, value=999, help="Days since last contact (999 = never contacted)")
        previous = st.slider("📋 Previous Campaigns", min_value=0, max_value=5, value=0, help="Number of previous campaigns")
        
        st.markdown("### 📱 Contact Information")
        contact_cellular = st.checkbox("📱 Contacted via Cellular", value=True)
        
        st.markdown("### 🗓️ Application Month")
        month_options = {
            "January": {"month_jan": 1},
            "February": {"month_feb": 1}, 
            "March": {"month_mar": 1},
            "April": {"month_apr": 1},
            "May": {"month_may": 1},
            "June": {"month_jun": 1},
            "July": {"month_jul": 1},
            "August": {"month_aug": 1},
            "September": {"month_sep": 1},
            "October": {"month_oct": 1},
            "November": {"month_nov": 1},
            "December": {"month_dec": 1}
        }
        selected_month = st.selectbox("Select Month", list(month_options.keys()), index=4)
        
        st.markdown("### 💼 Job Information")
        job_management = st.checkbox("👔 Management Position", value=False)
        job_technician = st.checkbox("🔧 Technician Position", value=True)
        
        st.markdown("### 👨‍👩‍👧‍👦 Personal Information")
        marital_married = st.checkbox("💍 Married", value=True)
        education_university = st.checkbox("🎓 University Degree", value=True)
        
        st.markdown("### 💳 Financial History")
        default_no = st.checkbox("✅ No Previous Default", value=True)
        housing_no = st.checkbox("🏠 No Housing Loan", value=True)
        loan_no = st.checkbox("💰 No Personal Loan", value=True)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🎯 Risk Assessment Dashboard")
        
        # Predict button
        if st.button("🔮 Analyze Loan Risk", type="primary", use_container_width=True):
            # Prepare features
            features = {
                'age': float(age),
                'campaign': float(campaign),
                'pdays': float(pdays), 
                'previous': float(previous),
                'contact_cellular': float(contact_cellular),
                'month_mar': float(selected_month == "March"),
                'month_oct': float(selected_month == "October"),
                'default_no': float(default_no),
                'job_management': float(job_management),
                'job_technician': float(job_technician),
                'marital_married': float(marital_married),
                'education_university.degree': float(education_university),
                'housing_no': float(housing_no),
                'loan_no': float(loan_no)
            }
            
            # Add month features
            for month, month_dict in month_options.items():
                for key in month_dict:
                    features[key] = float(selected_month == month)
            
            # Make prediction
            with st.spinner("🤖 AI is analyzing your application..."):
                time.sleep(2)  # Dramatic pause
                result = predict_loan_default(features)
            
            # Display results
            probability = result['probability']
            risk_level = result['risk_level']
            recommendation = result['recommendation']
            
            # Show result with animation
            if recommendation == "APPROVE":
                show_approval_animation()
            else:
                show_rejection_message()
            
            # 3D Visualizations
            st.markdown("### 📊 3D Risk Analysis")
            
            # Risk visualization
            risk_fig = create_3d_risk_visualization(probability, risk_level)
            st.plotly_chart(risk_fig, use_container_width=True)
            
            # Probability gauge
            gauge_fig = create_probability_gauge(probability)
            st.plotly_chart(gauge_fig, use_container_width=True)
            
    with col2:
        st.markdown("### 📈 Model Information")
        
        st.markdown("""
        <div class="metric-card">
            <h4>🎯 Model Performance</h4>
            <p><strong>Accuracy:</strong> 78.8%</p>
            <p><strong>Dataset:</strong> 41,188 records</p>
            <p><strong>Default Rate:</strong> 11.3%</p>
            <p><strong>Threshold:</strong> 60%</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h4>🔍 Risk Factors</h4>
            <p><strong>📱 Cellular Contact:</strong> +43.8%</p>
            <p><strong>📅 Contact Days:</strong> -27.9%</p>
            <p><strong>📆 March Apps:</strong> +19.8%</p>
            <p><strong>📆 October Apps:</strong> +18.5%</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h4>💡 Tips for Approval</h4>
            <p>• Maintain good credit history</p>
            <p>• Reduce existing debt</p>
            <p>• Increase income stability</p>
            <p>• Avoid multiple applications</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()