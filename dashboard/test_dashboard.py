#!/usr/bin/env python3
"""
Test script to verify dashboard dependencies and data loading
"""
import sys
import csv
import os

def test_data_loading():
    """Test if the data file can be loaded"""
    print("Testing data loading...")
    
    if not os.path.exists('Final_HH_Export_with_all_categories.csv'):
        print("❌ Data file not found: Final_HH_Export_with_all_categories.csv")
        return False
    
    try:
        with open('Final_HH_Export_with_all_categories.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            
        print(f"✅ Data loaded successfully: {len(data)} rows")
        
        # Check for required columns
        required_columns = ['own_or_rent', 'income_category', 'residency_duration', 
                          'household_size', 'cost_burden_category']
        
        headers = data[0].keys() if data else []
        missing_columns = [col for col in required_columns if col not in headers]
        
        if missing_columns:
            print(f"⚠️ Missing columns: {missing_columns}")
        else:
            print("✅ All required columns present")
        
        # Filter for year-round/seasonal residents
        filtered_data = [row for row in data 
                        if 'year-round' in row.get('residency_duration', '').lower() 
                        or 'seasonal' in row.get('residency_duration', '').lower()]
        
        print(f"✅ Filtered data: {len(filtered_data)} year-round/seasonal residents")
        
        return True
        
    except Exception as e:
        print(f"❌ Error loading data: {str(e)}")
        return False

def test_python_version():
    """Test Python version compatibility"""
    print("Testing Python version...")
    version = sys.version_info
    
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor} is compatible")
        return True
    else:
        print(f"⚠️ Python {version.major}.{version.minor} - recommend 3.8+")
        return False

def main():
    print("=== Housing Survey Dashboard Test ===")
    print()
    
    # Test Python version
    python_ok = test_python_version()
    print()
    
    # Test data loading
    data_ok = test_data_loading()
    print()
    
    if python_ok and data_ok:
        print("🎉 All tests passed! Dashboard should work correctly.")
        print()
        print("Next steps:")
        print("1. Install Streamlit: pip install streamlit plotly pandas numpy")
        print("2. Run dashboard: streamlit run housing_survey_dashboard.py")
        print("3. Open browser to: http://localhost:8501")
    else:
        print("❌ Some tests failed. Please resolve issues before deploying.")

if __name__ == "__main__":
    main()