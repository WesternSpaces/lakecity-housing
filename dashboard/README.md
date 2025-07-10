# Housing Survey Dashboard Deployment

## Quick Deploy to Your Repository

### Step 1: Add to Your Repository
1. Copy all files from this `dashboard-deployment` folder to your `lakecity-housing` repository
2. Create a `dashboard` folder in your repo root
3. Put all these files in the `dashboard` folder

### Step 2: Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. New app → From existing repo
4. Repository: `WesternSpaces/lakecity-housing`
5. Branch: `main`
6. Main file path: `dashboard/housing_survey_dashboard.py`
7. Click "Deploy"

### Step 3: Get Your Dashboard URL
After deployment, you'll get a URL like:
`https://lakecity-housing-dashboard.streamlit.app`

### Step 4: Update Your Website
Add this HTML section to your `index.html` file (after the News & Updates section):

```html
<!-- Housing Survey Dashboard Section -->
<section class="dashboard-section" style="padding: 4rem 0; background: #f8f9fa;">
    <div class="container">
        <div class="row">
            <div class="col-lg-12 text-center">
                <h2 style="color: #2E8B57; margin-bottom: 2rem;">
                    📊 Housing Survey Results
                </h2>
                <p class="lead" style="max-width: 800px; margin: 0 auto 3rem auto; color: #666;">
                    Explore interactive findings from our comprehensive housing survey. 
                    Filter by demographics while maintaining resident confidentiality.
                </p>
            </div>
        </div>
        
        <div class="row">
            <div class="col-lg-12">
                <div style="
                    background: white; 
                    border-radius: 15px; 
                    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                    padding: 2rem;
                    margin-bottom: 2rem;
                    border-left: 5px solid #2E8B57;
                ">
                    <div class="row align-items-center">
                        <div class="col-md-8">
                            <h4 style="color: #2E8B57; margin-bottom: 1rem;">
                                Interactive Data Dashboard
                            </h4>
                            <p style="color: #666; margin-bottom: 1.5rem;">
                                • 80 year-round and seasonal worker residents surveyed<br>
                                • Filter by ownership, income, and employment status<br>
                                • Confidentiality protections built-in<br>
                                • Real-time cross-tabulation analysis
                            </p>
                            <button onclick="openDashboard()" style="
                                background: linear-gradient(135deg, #2E8B57 0%, #20B2AA 100%);
                                border: none;
                                padding: 12px 30px;
                                border-radius: 25px;
                                font-weight: bold;
                                color: white;
                                cursor: pointer;
                                transition: transform 0.2s;
                            ">
                                Launch Dashboard
                            </button>
                        </div>
                        <div class="col-md-4 text-center">
                            <div style="
                                background: linear-gradient(135deg, #2E8B57 0%, #20B2AA 100%);
                                color: white;
                                padding: 2rem;
                                border-radius: 10px;
                            ">
                                <h3 style="margin: 0; font-size: 2.5rem;">80</h3>
                                <p style="margin: 0; opacity: 0.9;">Survey Responses</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<script>
function openDashboard() {
    window.open('https://YOUR-DASHBOARD-URL.streamlit.app', 
                'HousingSurveyDashboard', 
                'width=1200,height=800,scrollbars=yes,resizable=yes');
}
</script>
```

**Replace `YOUR-DASHBOARD-URL` with your actual Streamlit app URL!**

## Files Included

- `housing_survey_dashboard.py` - Main dashboard app
- `requirements.txt` - Python dependencies  
- `streamlit_app.py` - Entry point
- `Final_HH_Export_with_all_categories.csv` - Survey data
- `.streamlit/config.toml` - Styling configuration
- `test_dashboard.py` - Test before deployment

## Test Before Deploying

Run this to make sure everything works:
```bash
python3 test_dashboard.py
```

Should show: "🎉 All tests passed! Dashboard should work correctly."

## That's It!

Your dashboard will be live and integrated with your website!