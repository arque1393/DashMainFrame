# import dash 
# from dash import dcc
sidebar_style = {
    'display': 'flex',
    'position': 'fixed',
    'top': '40px',
    'left': '0',
    'width': '300px',
    'height': '100%',
    'background': '#100020',
    'transition': '0.2s',
    'min-width': '50px'
}
from dash import html
import dash_draggable
item_icon_list = ["fa fa-user","fa fa-qrcode","fa fa-link","fa fa-eye","fa fa-book"]
redirect_url_list = ['#','#','#','#','#']

if len(redirect_url_list) != len(item_icon_list):
    raise 'Icon url Mismatch error '

sidebar_inner = html.Div(className='sidebar_inner',children=[
    html.Ul(className="ul", children=[ 
        html.Li(children=[
            html.A( href=redirect_url_list[i],children=[
                html.Span(className= 'icon',children=[
                    html.I(className=item_icon_list[i])
                ])
            ])
        ]) for i in range(len(item_icon_list))]) ,

    html.Button( id='setting',children=[
            html.Span(className= 'icon',children=[
                html.I(className="fa fa-cog")
            ])
        ])
    ])

sidebar_content=html.Div(className='sidebar_content',children=[])

resizer = html.Div(id = 'resizer',className='resizer')

sidebar = html.Div(id='sidebar',className="sidebar", 
    children=[sidebar_inner,sidebar_content,resizer], 
    style=sidebar_style)



### Topbar 
top_navbar = html.Div(className='top_navbar',children=[
    html.Div(className='menu', children=[
        html.Button(id='hamburger',className='hamburger', children=[
            html.I(className="fas fa-bars")
        ]),
        html.Div(className='logo', children=[ "MainFrame"])
    ])
])



### Footer 
