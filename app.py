#%%
import dash 
from dash import dcc,html
from components.extraUI import sidebar,top_navbar
from dash.exceptions import PreventUpdate
from dash.dependencies import Input,Output,State,ClientsideFunction
import dash_draggable

#%%
app = dash.Dash(__name__,external_scripts=[{'src':"https://kit.fontawesome.com/b99e675b6e.js"}])
server = app.server
app.layout =html.Div(className="wrapper hover_collapse",children=[top_navbar,sidebar])

@app.callback(

    Output(component_id='sidebar', component_property='style'),
    Input(component_id='hamburger', component_property='n_clicks'),
    Input(component_id='sidebar', component_property='style')
)
def update(n_clicks,style):
    if n_clicks is None:
        raise PreventUpdate
    else:
        width=  int( style['width'][0:-2])
        if width<300 :
            style['width'] = '300px'
        else :
            style['width'] = '50px'

        return style



# @app.callback(
#     Output(component_id='sidebar', component_property='style'),
#     Input(component_id='resizer', component_property='n_clicks') )
# def update(n_clicks):
#     if n_clicks is None:
#         print("Dracula")
#         raise PreventUpdate
#     else:
#         print(n_clicks)


def main():
    # app.run_server(debug=True)
    app.run_server(port=8051)

if __name__ == '__main__':
    main()
# %%
