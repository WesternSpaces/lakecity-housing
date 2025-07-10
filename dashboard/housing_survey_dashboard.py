import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Hinsdale County Housing Survey Dashboard",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to match lakecityhousingstrategy.com design
st.markdown("""
<style>
    .stApp {
        background-color: #ffffff;
    }
    
    .main-header {
        background: linear-gradient(135deg, #2E8B57 0%, #20B2AA 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    
    .main-header h1 {
        color: white !important;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    
    .main-header p {
        color: #f0f8ff;
        font-size: 1.2rem;
        margin-bottom: 0;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-left: 4px solid #2E8B57;
        margin-bottom: 1rem;
    }
    
    .stSelectbox > div > div {
        border-color: #2E8B57;
    }
    
    .stMultiSelect > div > div {
        border-color: #2E8B57;
    }
    
    .sidebar-header {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border-left: 4px solid #2E8B57;
    }
    
    .confidence-warning {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #f39c12;
    }
    
    .confidence-success {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #2E8B57;
    }
</style>
""", unsafe_allow_html=True)

# Constants for confidentiality
MIN_SAMPLE_SIZE = 5  # Minimum number of responses to display data

@st.cache_data
def load_data():
    """Load and prepare the housing survey data"""
    try:
        # Load the raw data file
        df = pd.read_csv('dashboard/Final_HH_Export_with_all_categories.csv')
        
        # Filter for year-round and seasonal workers only
        df = df[df['residency_duration'].str.contains('Year-round|seasonal', case=False, na=False)]
        
        # Clean and prepare key variables
        df['income_numeric'] = df['income_category'].map({
            'Less than $25,000': 12500,
            '$25,000-$49,999': 37500,
            '$50,000-$74,999': 62500,
            '$75,000-$99,999': 87500,
            '$100,000-$149,999': 125000,
            '$150,000-$199,999': 175000,
            '$200,000 or more': 225000
        })
        
        # Create simplified categories
        df['housing_cost_simple'] = df['housing_cost_category'].map({
            'Less than $500': 'Low (<$1,000)',
            '$500-$999': 'Low (<$1,000)',
            '$1,000-$1,499': 'Moderate ($1,000-$1,999)',
            '$1,500-$1,999': 'Moderate ($1,000-$1,999)',
            '$2,000-$2,999': 'High ($2,000+)',
            '$3,000-$3,999': 'High ($2,000+)',
            '$4,000 or more': 'High ($2,000+)'
        })
        
        # Create employment status with better error handling
        def get_employment_status(row):
            try:
                # Helper function to safely convert to int
                def safe_int(val):
                    val_str = str(val).replace('Zero', '0').replace('nan', '0').strip()
                    if not val_str or val_str.lower() == 'nan':
                        return 0
                    try:
                        return int(float(val_str))
                    except:
                        return 0
                
                employed = safe_int(row.get('adults_employed', 0))
                self_employed = safe_int(row.get('adults_self_employed', 0))
                retired = safe_int(row.get('adults_retired', 0))
                
                if (employed > 0 or self_employed > 0) and retired == 0:
                    return 'Working Households'
                elif (employed > 0 or self_employed > 0) and retired > 0:
                    return 'Working and Retired'
                elif retired > 0:
                    return 'Retired Only'
                else:
                    return 'Not in Labor Force'
            except:
                return 'Not in Labor Force'
        
        df['employment_status'] = df.apply(get_employment_status, axis=1)
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

def check_confidentiality(data, min_size=MIN_SAMPLE_SIZE):
    """Check if data meets minimum sample size requirements"""
    if len(data) < min_size:
        return False, f"Sample size ({len(data)}) below minimum threshold ({min_size})"
    return True, f"Sample size: {len(data)}"

def create_demographic_summary(df):
    """Create demographic summary visualizations"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Ownership Status")
        try:
            ownership_data = df['own_or_rent'].value_counts()
            if len(ownership_data) > 0:
                fig = px.pie(values=ownership_data.values, names=ownership_data.index, 
                            title="Own vs Rent Distribution")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No ownership data available")
        except Exception as e:
            st.error(f"Error creating ownership chart: {str(e)}")
    
    with col2:
        st.subheader("Household Size")
        try:
            size_data = df['household_size'].value_counts().sort_index()
            if len(size_data) > 0:
                fig = px.bar(x=size_data.index.astype(str), y=size_data.values, 
                            title="Household Size Distribution")
                fig.update_xaxis(title="Number of People")
                fig.update_yaxis(title="Number of Households")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No household size data available")
        except Exception as e:
            st.error(f"Error creating household size chart: {str(e)}")

def create_economic_analysis(df):
    """Create economic analysis visualizations"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Income Distribution")
        try:
            income_order = ['Less than $25,000', '$25,000-$49,999', '$50,000-$74,999', 
                           '$75,000-$99,999', '$100,000-$149,999', '$150,000-$199,999', 
                           '$200,000 or more']
            income_data = df['income_category'].value_counts().reindex(income_order, fill_value=0)
            if income_data.sum() > 0:
                fig = px.bar(x=income_data.index, y=income_data.values, 
                            title="Annual Household Income")
                fig.update_xaxis(title="Income Range", tickangle=45)
                fig.update_yaxis(title="Number of Households")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No income data available")
        except Exception as e:
            st.error(f"Error creating income chart: {str(e)}")
    
    with col2:
        st.subheader("Housing Cost Burden")
        try:
            burden_data = df['cost_burden_category'].value_counts()
            if len(burden_data) > 0:
                colors = {'30% or less': 'green', '30-50%': 'orange', 'Over 50%': 'red'}
                fig = px.bar(x=burden_data.index, y=burden_data.values,
                            title="Housing Cost as % of Income",
                            color=burden_data.index,
                            color_discrete_map=colors)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No cost burden data available")
        except Exception as e:
            st.error(f"Error creating cost burden chart: {str(e)}")

def create_filtered_crosstab(df, row_var, col_var, min_size=MIN_SAMPLE_SIZE):
    """Create a crosstab with confidentiality protection"""
    crosstab = pd.crosstab(df[row_var], df[col_var], margins=True)
    
    # Check if any cell is below minimum
    below_min = (crosstab < min_size) & (crosstab > 0)
    
    if below_min.any().any():
        st.warning(f"Some cells have fewer than {min_size} responses and are suppressed for confidentiality")
        crosstab = crosstab.mask(below_min, f"<{min_size}")
    
    return crosstab

def main():
    # Custom header matching website design
    st.markdown("""
    <div class="main-header">
        <h1>🏠 Housing Survey Dashboard</h1>
        <p>Interactive Analysis of Housing Needs and Preferences</p>
        <p style="font-size: 1rem; margin-top: 1rem;">
            Exploring data from 80 year-round and seasonal worker residents
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    df = load_data()
    if df is None:
        st.stop()
    
    # Sidebar filters with custom styling
    st.sidebar.markdown("""
    <div class="sidebar-header">
        <h3 style="margin: 0; color: #2E8B57;">🔍 Filter Survey Data</h3>
        <p style="margin: 0.5rem 0 0 0; color: #666; font-size: 0.9rem;">
            Select demographics to explore
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Basic demographic filters
    ownership_filter = st.sidebar.multiselect(
        "Ownership Status", 
        options=df['own_or_rent'].dropna().unique(),
        default=df['own_or_rent'].dropna().unique()
    )
    
    income_filter = st.sidebar.multiselect(
        "Income Level",
        options=df['income_category'].dropna().unique(),
        default=df['income_category'].dropna().unique()
    )
    
    employment_filter = st.sidebar.multiselect(
        "Employment Status",
        options=df['employment_status'].dropna().unique(),
        default=df['employment_status'].dropna().unique()
    )
    
    # Apply filters
    filtered_df = df[
        (df['own_or_rent'].isin(ownership_filter)) &
        (df['income_category'].isin(income_filter)) &
        (df['employment_status'].isin(employment_filter))
    ]
    
    # Check confidentiality
    is_safe, message = check_confidentiality(filtered_df)
    
    if not is_safe:
        st.error(f"⚠️ {message}")
        st.info("Please adjust your filters to include more responses.")
        return
    
    st.success(f"✅ {message}")
    
    # Main dashboard tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Demographics", "💰 Economics", "🏘️ Housing", "📈 Crosstabs"])
    
    with tab1:
        st.header("Demographic Overview")
        create_demographic_summary(filtered_df)
        
        # Additional demographic details
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Households", len(filtered_df))
        
        with col2:
            try:
                avg_size = filtered_df['household_size'].astype(str).str.extract('(\d+)')[0].astype(float).mean()
                st.metric("Average Household Size", f"{avg_size:.1f}" if not pd.isna(avg_size) else "N/A")
            except:
                st.metric("Average Household Size", "N/A")
        
        with col3:
            try:
                seniors_data = filtered_df['age_65_plus'].fillna('0').astype(str).str.extract('(\d+)')[0]
                seniors_count = (seniors_data.astype(float) > 0).sum()
                st.metric("Households with 65+", seniors_count)
            except:
                st.metric("Households with 65+", "N/A")
    
    with tab2:
        st.header("Economic Analysis")
        create_economic_analysis(filtered_df)
        
        # Income vs Housing Cost scatter
        if len(filtered_df) >= MIN_SAMPLE_SIZE:
            st.subheader("Income vs Housing Cost Relationship")
            income_cost_df = filtered_df.dropna(subset=['income_numeric', 'housing_cost_category'])
            if len(income_cost_df) >= MIN_SAMPLE_SIZE:
                fig = px.scatter(income_cost_df, x='income_numeric', y='housing_cost_category',
                               color='cost_burden_category', 
                               title="Income vs Monthly Housing Cost")
                st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.header("Housing Characteristics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Housing Type")
            housing_type_data = filtered_df['home_type'].value_counts()
            if len(housing_type_data) > 0:
                fig = px.pie(values=housing_type_data.values, names=housing_type_data.index)
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Length of Residence")
            residence_data = filtered_df['years_in_home'].value_counts()
            if len(residence_data) > 0:
                fig = px.bar(x=residence_data.values, y=residence_data.index, 
                           orientation='h', title="Years in Current Home")
                st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.header("Cross-tabulation Analysis")
        
        # Select variables for crosstab
        col1, col2 = st.columns(2)
        
        with col1:
            row_var = st.selectbox(
                "Row Variable",
                options=['own_or_rent', 'income_category', 'employment_status', 'cost_burden_category']
            )
        
        with col2:
            col_var = st.selectbox(
                "Column Variable", 
                options=['income_category', 'own_or_rent', 'employment_status', 'cost_burden_category']
            )
        
        if row_var != col_var:
            st.subheader(f"{row_var} by {col_var}")
            crosstab = create_filtered_crosstab(filtered_df, row_var, col_var)
            st.dataframe(crosstab)
            
            # Create heatmap if data is numeric
            try:
                numeric_crosstab = crosstab.select_dtypes(include=[np.number])
                if not numeric_crosstab.empty:
                    fig = px.imshow(numeric_crosstab, 
                                  title=f"Heatmap: {row_var} by {col_var}")
                    st.plotly_chart(fig, use_container_width=True)
            except:
                pass
    
    # Footer
    st.markdown("---")
    st.markdown("*Data from Hinsdale County/Lake City Housing Survey 2025*")
    st.markdown("*Confidentiality protected: Cells with fewer than 5 responses are suppressed*")

if __name__ == "__main__":
    main()
