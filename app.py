import dash

# Dash App Setup
app = dash.Dash(__name__, suppress_callback_exceptions=True)
# Used for Heroku deployment
server = app.server
