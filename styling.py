# ----------------------------------------------------------------------------
# PAGE SETTINGS
# ----------------------------------------------------------------------------
app_title = 'Virginia Environmental Education Directory'
page_title = 'Virginia Environmental Education Directory'
sub_title = 'Filter on'
filter_category_1 = 'Organization Data'
filter_category_2 = 'Program Data'

# ----------------------------------------------------------------------------
# MAP SETTINGS
# ----------------------------------------------------------------------------
map_center_lat = 37.9782627
map_center_lon = -79.2605896
map_zoom = 5.905

# Column in the dataset that maps to the featureidkey of the geojson.
# This is what maps the data column to the geojson feature
# For Texas this is the column that  definse the area category of the ESC
geojson_featureidkey='properties.FID'
data_area_col = 'ESC'
state_name = 'properties.STATE'

# ----------------------------------------------------------------------------
# STYLING
# ----------------------------------------------------------------------------

# Set Color scales for Figures using the EcoRise brande color palette

fulltint = ['#173D64','#345E88', '#AB5F13', '#F88E20', '#5DA039', '#FBB041']
tint_75 = [' #5c7792','#708eab','#c48f59','#faaf62','#8dbc74','#fcc77a']
tint_50 = ['#a2b1c1','#adbecf','#ddbfa0','#fcd1a5','#bed9af','#fddfb3']
eco_color = fulltint + tint_75 + tint_50
eco_color_r = fulltint[::-1] + tint_75[::-1] + tint_50[::-1]
eco_color_desc = eco_color[::-1]
eco_color_desc_r = eco_color_r[::-1]

# Set particular color scales of elements
map_color_scale = tint_50

#STYLES
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    # "width": 0, # REMOVE THIS WHEN FILTERS WORKING
    "width": "18rem", # ADD THIS BACK WHEN FILTERS WORKING
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    # "display":'none' # REMOVE THIS WHEN FILTERS WORKING
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "20rem",# ADD THIS BACK WHEN FILTERS WORKING
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# the normal style of for the tabs. The color bar set to seea blue
TAB_STYLE = {
    'borderTop': '4px solid #00A887',

}

# the style of for the selected tabs. The font bolded and color bar seea green
TAB_SELECTED_STYLE = {
    'borderTop': '4px solid #FF8F12',
    'fontWeight': 'bold'
}
