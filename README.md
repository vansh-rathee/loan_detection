# 🏦 3D Interactive Loan Approval System

A beautiful, interactive web application for loan default prediction with 3D visualizations and celebration animations.

## 🚀 Quick Start

### Easy Launch (Windows)
```bash
double-click run_app.bat
```

### Manual Launch
```bash
# Install dependencies
pip install -r requirements.txt

# Launch the 3D interface
python -m streamlit run streamlit_app.py
```

## ✨ Features

- 🎨 **3D Interactive Interface** with beautiful gradients and animations
- 🎉 **Party Celebrations** for loan approvals with confetti and balloons
- 😔 **Sympathetic Messages** for rejections with encouraging words
- 📊 **3D Risk Visualizations** with particle effects and gauges
- 🤖 **AI-Powered Predictions** using real data from 41,188 loan records
- 📱 **Mobile Responsive** design that works on all devices

## 🎯 Model Performance

- **Accuracy**: 78.8%
- **Dataset**: 41,188 real loan records
- **Default Rate**: 11.3%
- **Technologies**: Streamlit + Plotly + Pure Python

## 🎮 How to Use

1. **Open the web interface** using one of the launch methods above
2. **Fill out the loan application** using the interactive form
3. **Click "Analyze Loan Risk"** to get AI-powered assessment
4. **Watch the magic happen:**
   - ✅ **APPROVED**: Party popper celebrations! 🎉🎊🥳
   - ❌ **REJECTED**: Supportive message with tips 😔💙
5. **Explore 3D visualizations** of your risk assessment

## 📁 Files

- `streamlit_app.py` - Main 3D interactive web interface
- `simple_loan_predictor.py` - Core AI prediction engine  
- `loan_detection.csv` - Real dataset (41,188 records)
- `requirements.txt` - Dependencies
- `run_app.bat` - Quick launch script

## 🎊 Ready to Use!

Your loan approval system is production-ready with a stunning user interface! 🏆  

## Model Performance

- **Accuracy**: 78.8%
- **Dataset**: 41,188 loan records
- **Default Rate**: 11.3% (4,640 defaults)
- **Optimal Threshold**: 60%
- **No external dependencies required**
- **All code is readable and editable**

## Key Features

✓ Simple Python code (no complex libraries)  
✓ Fast predictions  
✓ Easy to understand and modify  
✓ No binary files  
✓ Works with any Python installation  

## Example Usage

```python
from simple_loan_predictor import predict_loan_default

customer = {
    'age': 35,
    'campaign': 2,
    'contact_cellular': 1,
    'job_management': 1,
    'marital_married': 1,
    'default_no': 1
}

result = predict_loan_default(customer)
print(f"Risk: {result['probability']:.1%}")
print(f"Decision: {result['recommendation']}")
```

## Risk Factors

**Increases Risk:**
- Cellular contact (+43.8%)
- March applications (+19.8%)
- October applications (+18.5%)

**Decreases Risk:**
- Recent contact (-27.9%)
- Multiple campaigns (-20.3%)



## 📚 Creator
- Vansh Rathee
- [GitHub](https://github.com/indra-hue)
