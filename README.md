# Ecorise Dashboard - dash application repository
This repository stores the codebase to build the Plotly Dash dashboard for the EcoRise Gen:Thrive iniatitive. The data collected for Gen:Thrive contains information on Organizations within the state of Texas and the programs they run, and displays that information in a dashboard with a mapping feature and assorted charting elements, including bar, pie and treemap charts.

## Application description
This dashboard is designed to be somewhat dynamic, with the data displayed and dropdown options driven by the contents of the data files in the data folder. Data records are collected in 2 tables: 'Organizations' and 'Programs', where Organizations are the top level, and the Programs table contains information on the specific programs run by given programs. These tables are stored in a 'data_records.xls' excel file. The data dictionary file (data_dictionary.xls) provides the meta data that explains the data collected in the data records and how this data should be used in the dashboard.  This file consists of 3 sheets: a sheet to explain the data dictionary itself, a sheet to describe the fields collected in the Organization and Program tables, and a sheet to describe the controlled terms for any fields that will only contain specified values. This file also provides a translation should the term in the data records differ from the term users wish to display.  

The data loading and processing workflow is described in the data_processing.py (functions) and data_load.py (actual data loading) files, which takes these data files and performs any necessary data wrangling and cleaning, including at this point the assignment of unique identifiers to both data tables, and the assignment of the Organization ID to Program records using a text match on the 'Organization' field. Once the data is in the proper format, the dash application (app.py) uses the data and any custom functions described in make_components.py to generate the application layout and callbacks to provide the desired user interactivity.

Finally, a geojson file provides the geospatial regions for the regions defined in the dataset and is used to generate a choropleth map in the dashboard.

## Technology Description
The Ecorise dashboard is written in python using the [Plotly Dash](https://dash.plotly.com/) application library and hosted on Heroku (https://genthrive2021.herokuapp.com/). Excluding the Data files in the data folder which will necessarily differ between projects, the bulk of this codebase is designed to easily transition between groups using the same basic data structure with only minor changes.  The main o

=======
This repository stores the codebase to build the Plotly Dash dashboard for Ecorise. It is currently building a dashboard for TX 2021 data.
>>>>>>> ec232027aa72ca82fcb1e1678c30297c83bbfcbc

## Content Directory
### Code files and folders in main directory
#### Data folder
* **data_dictionary.xls**: file with meta-data that describes how the data on Organizations and Programs should be used in the dashboard, and any transformations required in terms of displaying the data in data_records.xls
* **data_records.xls**: the actual data records collected
* **regions_simplified.geojson**: the geospatial file that defines the regions for the map. For LDOE this describes the Educational Service Centers. The file has been processed to produce simplified geometries that are faster to display in a web application.

#### Code Files
* **app.py**: the file that builds the actual dash application
* **data_processing.py**: a file with the necessary functions for data loading and cleaning processes
* **environment.yml**: file that provides Conda compliant instructions to build virtual environment
* **load_data.py**: the file that loads data from the data folder and uses the functions in data_processing.py to put the data in the proper form for the Dashboard
* **make_components.py**: functions to take in dataframes and variables and return dash compliant components  
* **Procfile**: a file used if deploying the application to Heroku
* **README.md**: the file you are reading that describes the contents of this repository
* **requirements.txt**: file that provides pip compliant instructions to build virtual environment
* **styling.py**: file to set certain styling settings and user defined terms such as page title, color scales for charts, etc.

#### Other folders
* assets: folder for assets such as css files and images used by the Application


### Branch Directory
The purpose of assorted branches of this repository are as follows:
* Main = Production Branch
* Development = Development Branch
* All Others = temporary work branches.  (Periodically review if these are ready for deletion)


### Heroku Installation instructions
Instructions for launching dash applications on Heroku are outlined in the [Plotly Dash documentation](https://dash.plotly.com/deployment) or at this [dash-heroku-deployment repository](https://github.com/drstarson/dash-heroku-app/blob/master/README.md)
