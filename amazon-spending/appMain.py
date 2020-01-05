
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.graph_objs as go

from datetime import date
from datetime import time
from datetime import datetime

import dash

external_stylesheets = ['/Users/dinchaney/amazon-spending/amazon.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('/Users/dinchaney/amazon-spending/dfPivot.csv')

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['dateIndex'] = df['Order Date']
df = df.set_index('dateIndex')
df['dateOrder'] = df['Order Date'].apply(lambda x: x.strftime('%B %Y'))
df['yearMonth'] = df['Order Date'].map(lambda x: 100 * x.year + x.month)
df = df.fillna(0)
df.to_csv('formattedDF.csv')
# print(df['yearMonth'])

sliderDatesValues = df.yearMonth.to_list()
sliderDatesView = df.dateOrder.to_list()
sliderDates = df.yearMonth.unique()

sliderDatesDict = dict(zip(sliderDatesValues, sliderDatesView))


def prettyDates(x):
    print('Starting with ' + x)
    x1 = x[0:4]
    print('Extracting the year: ' + x1)
    x2 = x[4:]
    print('Extracting the month: ' + x2)
    x3 = 1
    x1 = int(x1)
    x2 = int(x2)
    x = date(x1, x2, x3)
    print('Transformed to date format: ' + str(x))
    x = x.strftime("%B %Y")
    print('The final result is ' + str(x))
    return x

testing1 = str(201711)
print(prettyDates(testing1))

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "A Look at 13 Years of Amazon Shopping Habits",
                    style={"text-align": "center"}
                )
            ]),
        html.Div(
            [
                dcc.Graph(
                    id='figure'
                ),
                html.Div(
                    dcc.RangeSlider(
                        id='yearSlider',
                        min=sliderDates[0],
                        max=sliderDates[-1],
                        step=None,
                        allowCross=False,
                        value=[sliderDates[0], sliderDates[-1]],
                        marks={
                            200603: {'label' : 'Mar 2006'},
                            200604: {'label' : 'Apr 2006'},
                            200605: {'label' : 'May 2006'},
                            200606: {'label' : 'Jun 2006'},
                            200607: {'label' : 'Jul 2006'},
                            200608: {'label' : 'Aug 2006'},
                            200609: {'label' : 'Sep 2006'},
                            200610: {'label' : 'Oct 2006'},
                            200611: {'label' : 'Nov 2006'},
                            200612: {'label' : 'Dec 2006'},

                            200701: {'label' : 'Jan 2007'},
                            200702: {'label' : 'Feb 2007'},
                            200703: {'label' : 'Mar 2007'},
                            200704: {'label' : 'Apr 2007'},
                            200705: {'label' : 'May 2007'},
                            200706: {'label' : 'Jun 2007'},
                            200707: {'label' : 'Jul 2007'},
                            200708: {'label' : 'Aug 2007'},
                            200709: {'label' : 'Sep 2007'},
                            200710: {'label' : 'Oct 2007'},
                            200711: {'label' : 'Nov 2007'},
                            200712: {'label' : 'Dec 2007'},

                            200801: {'label' : 'Jan 2008'},
                            200802: {'label' : 'Feb 2008'},
                            200803: {'label' : 'Mar 2008'},
                            200804: {'label' : 'Apr 2008'},
                            200805: {'label' : 'May 2008'},
                            200806: {'label' : 'Jun 2008'},
                            200807: {'label' : 'Jul 2008'},
                            200808: {'label' : 'Aug 2008'},
                            200809: {'label' : 'Sep 2008'},
                            200810: {'label' : 'Oct 2008'},
                            200811: {'label' : 'Nov 2008'},
                            200812: {'label' : 'Dec 2008'},

                            200901: 'Jan 2009',
                            200902: 'Feb 2009',
                            200903: 'Mar 2009',
                            200904: 'Apr 2009',
                            200905: 'May 2009',
                            200906: 'Jun 2009',
                            200907: 'Jul 2009',
                            200908: 'Aug 2009',
                            200909: 'Sep 2009',
                            200910: 'Oct 2009',
                            200911: 'Nov 2009',
                            200912: 'Dec 2009',

                            201001: 'Jan 2010',
                            201002: 'Feb 2010',
                            201003: 'Mar 2010',
                            201004: 'Apr 2010',
                            201005: 'May 2010',
                            201006: 'Jun 2010',
                            201007: 'Jul 2010',
                            201008: 'Aug 2010',
                            201009: 'Sep 2010',
                            201010: 'Oct 2010',
                            201011: 'Nov 2010',
                            201012: 'Dec 2010',

                            201101: 'Jan 2011',
                            201102: 'Feb 2011',
                            201103: 'Mar 2011',
                            201104: 'Apr 2011',
                            201105: 'May 2011',
                            201106: 'Jun 2011',
                            201107: 'Jul 2011',
                            201108: 'Aug 2011',
                            201109: 'Sep 2011',
                            201110: 'Oct 2011',
                            201111: 'Nov 2011',
                            201112: 'Dec 2011',

                            201201: 'Jan 2012',
                            201202: 'Feb 2012',
                            201203: 'Mar 2012',
                            201204: 'Apr 2012',
                            201205: 'May 2012',
                            201206: 'Jun 2012',
                            201207: 'Jul 2012',
                            201208: 'Aug 2012',
                            201209: 'Sep 2012',
                            201210: 'Oct 2012',
                            201211: 'Nov 2012',
                            201212: 'Dec 2012',

                            201301: 'Jan 2013',
                            201302: 'Feb 2013',
                            201303: 'Mar 2013',
                            201304: 'Apr 2013',
                            201305: 'May 2013',
                            201306: 'Jun 2013',
                            201307: 'Jul 2013',
                            201308: 'Aug 2013',
                            201309: 'Sep 2013',
                            201310: 'Oct 2013',
                            201311: 'Nov 2013',
                            201312: 'Dec 2013',

                            201401: 'Jan 2014',
                            201402: 'Feb 2014',
                            201403: 'Mar 2014',
                            201404: 'Apr 2014',
                            201405: 'May 2014',
                            201406: 'Jun 2014',
                            201407: 'Jul 2014',
                            201408: 'Aug 2014',
                            201409: 'Sep 2014',
                            201410: 'Oct 2014',
                            201411: 'Nov 2014',
                            201412: 'Dec 2014',

                            201501: 'Jan 2015',
                            201502: 'Feb 2015',
                            201503: 'Mar 2015',
                            201504: 'Apr 2015',
                            201505: 'May 2015',
                            201506: 'Jun 2015',
                            201507: 'Jul 2015',
                            201508: 'Aug 2015',
                            201509: 'Sep 2015',
                            201510: 'Oct 2015',
                            201511: 'Nov 2015',
                            201512: 'Dec 2015',

                            201601: 'Jan 2016',
                            201602: 'Feb 2016',
                            201603: 'Mar 2016',
                            201604: 'Apr 2016',
                            201605: 'May 2016',
                            201606: 'Jun 2016',
                            201607: 'Jul 2016',
                            201608: 'Aug 2016',
                            201609: 'Sep 2016',
                            201610: 'Oct 2016',
                            201611: 'Nov 2016',
                            201612: 'Dec 2016',

                            201701: 'Jan 2017',
                            201702: 'Feb 2017',
                            201703: 'Mar 2017',
                            201704: 'Apr 2017',
                            201705: 'May 2017',
                            201706: 'Jun 2017',
                            201707: 'Jul 2017',
                            201708: 'Aug 2017',
                            201709: 'Sep 2017',
                            201710: 'Oct 2017',
                            201711: 'Nov 2017',
                            201712: 'Dec 2017',

                            201801: 'Jan 2018',
                            201802: 'Feb 2018',
                            201803: 'Mar 2018',
                            201804: 'Apr 2018',
                            201805: 'May 2018',
                            201806: 'Jun 2018',
                            201807: 'Jul 2018',
                            201808: 'Aug 2018',
                            201809: 'Sep 2018',
                            201810: 'Oct 2018',
                            201811: 'Nov 2018',
                            201812: 'Dec 2018',

                            201901: 'Jan 2019',
                            201902: 'Feb 2019',
                            201903: 'Mar 2019',
                            201904: 'Apr 2019',
                            201905: 'May 2019',
                            201906: 'Jun 2019',
                            201907: 'Jul 2019',
                            201908: 'Aug 2019',
                            201909: 'Sep 2019'},
                        included=False
                    ),
                    style={"margin": 20, "padding": 30})
            ])
    ])
print(sliderDates)


@app.callback(
    dash.dependencies.Output('figure', 'figure'),
    [dash.dependencies.Input('yearSlider', 'value')]
)
def update_figure(dateSelect):
    pd.options.mode.chained_assignment = None  # controls 'SettingWithCopyWarning'
    dff = df[(df.yearMonth >= dateSelect[0]) & (df.yearMonth <= dateSelect[1])]
    dff['dateOrderSelect'] = dff['Order Date'].apply(lambda x: x.strftime('%B-%Y'))
    dff.to_csv('reviewingDates.csv')

    firstSelection = str(dateSelect[0])
    secondSelection = str(dateSelect[1])
    titleDate1 = prettyDates(firstSelection)
    titleDate2 = prettyDates(secondSelection)

    trace1 = go.Scatter(
        y=dff['0'],
        x=dff['dateOrder'],
        mode='lines+markers',
        marker={"size": 5.5},
        name='Uncategorized')

    trace2 = go.Scatter(
        y=dff['Accessory'],
        x=dff['dateOrder'],
        mode='markers',
        marker={"size": 6},
        name='Accessories')

    trace3 = go.Scatter(
        y=dff['Apparel'],
        x=dff['dateOrder'],
        mode='lines',
        marker={"size": 5},
        name='Apparel')

    trace4 = go.Scatter(
        y=dff['Automotive'],
        x=dff['dateOrder'],
        mode='lines+markers',
        marker={'size': 5.5},
        name='Automotive')

    trace5 = go.Scatter(
        y=dff['Baby Product'],
        x=dff["dateOrder"],
        mode='markers',
        marker={"size": 6},
        name='Baby Products')

    trace6 = go.Scatter(
        y=dff['Blu-ray'],
        x=dff["dateOrder"],
        mode='lines',
        marker={"size": 5},
        name='Blue-ray')

    trace7 = go.Scatter(
        y=dff['Board book'],
        x=dff["dateOrder"],
        mode='lines+markers',
        marker={"size": 5.5},
        name='Board book')

    trace8 = go.Scatter(
        y=dff['CD-ROM'],
        x=dff["dateOrder"],
        mode='markers',
        marker={"size": 6},
        name='CD-ROM')

    trace9 = go.Scatter(
        y=dff['Calendar'],
        x=dff["dateOrder"],
        mode='lines',
        marker={"size": 5},
        name='Calendar')

    trace10 = go.Scatter(
        y=dff['Camera'],
        x=dff["dateOrder"],
        mode='lines+markers',
        marker={"size": 5.5},
        name='Camera')

    trace11 = go.Scatter(
        y=dff['Card Book'],
        x=dff["dateOrder"],
        mode='markers',
        marker={"size": 6},
        name='Card Book')

    trace12 = go.Scatter(
        y=dff['DVD'],
        x=dff["dateOrder"],
        mode='lines',
        marker={"size": 5},
        name='DVD')

    trace13 = go.Scatter(
        y=dff['Diary'],
        x=dff["dateOrder"],
        mode='lines+markers',
        marker={"size": 5.5},
        name='Diary')

    trace14 = go.Scatter(
        y=dff['Ecard Gift Certificate'],
        x=dff["dateOrder"],
        mode='markers',
        marker={"size": 6},
        name='Ecard Gift Certificate')

    trace15 = go.Scatter(
        y=dff['Electronics'],
        x=dff["dateOrder"],
        mode='lines',
        marker={"size": 5},
        name='Electronics')

    trace16 = go.Scatter(
        y=dff['Grocery'],
        x=dff["dateOrder"],
        mode='lines+markers',
        marker={"size": 5.5},
        name='Grocery')

    trace17 = go.Scatter(
        y=dff['Hardcover'],
        x=dff["dateOrder"],
        mode='markers',
        marker={"size": 6},
        name='Hardcover')

    trace18 = go.Scatter(
        y=dff['Health and Beauty'],
        x=dff["dateOrder"],
        mode='lines',
        marker={"size": 5},
        name='Health and Beauty')

    trace19 = go.Scatter(
        y=dff['Home'],
        x=dff["dateOrder"],
        mode='lines+markers',
        marker={"size": 5.5},
        name='Home')

    trace20 = go.Scatter(
        y=dff['Jewelry'],
        x=dff["dateOrder"],
        mode='markers',
        marker={"size": 6},
        name='Jewelry')

    trace21 = go.Scatter(
        y=dff['Kitchen'],
        x=dff["dateOrder"],
        mode='lines',
        marker={"size": 5},
        name='Kitchen')

    trace22 = go.Scatter(
        y=dff['Lawn & Patio'],
        x=dff["dateOrder"],
        mode='lines+markers',
        marker={"size": 5.5},
        name='Lawn & Patio')

    trace23 = go.Scatter(
        y=dff['Luggage'],
        x=dff["dateOrder"],
        mode='markers',
        marker={"size": 6},
        name='Luggage')

    trace24 = go.Scatter(
        y=dff['Mass Market Paperback'],
        x=dff["dateOrder"],
        mode='lines',
        marker={"size": 5},
        name='Mass Market Paperback')

    trace25 = go.Scatter(
        y=dff['Misc.'],
        x=dff["dateOrder"],
        mode='lines+markers',
        marker={"size": 5.5},
        name='Misc.')

    trace26 = go.Scatter(
        y=dff['Office Product'],
        x=dff["dateOrder"],
        mode='markers',
        marker={"size": 6},
        name='Office Product')

    trace27 = go.Scatter(
        y=dff['Pamphlet'],
        x=dff["dateOrder"],
        mode='lines',
        marker={"size": 5},
        name='Pamphlet')

    trace28 = go.Scatter(
        y=dff['Paperback'],
        x=dff["dateOrder"],
        mode='lines+markers',
        marker={"size": 5.5},
        name='Paperback')

    trace29 = go.Scatter(
        y=dff['Personal Computers'],
        x=dff["dateOrder"],
        mode='markers',
        marker={"size": 6},
        name='Personal Computers')

    trace30 = go.Scatter(
        y=dff['Print Magazine'],
        x=dff["dateOrder"],
        mode='lines',
        marker={"size": 5},
        name='Print Magazine')

    trace31 = go.Scatter(
        y=dff['Shoes'],
        x=dff["dateOrder"],
        mode='lines+markers',
        marker={"size": 5.5},
        name='Shoes')

    trace32 = go.Scatter(
        y=dff['Single Issue Magazine'],
        x=dff["dateOrder"],
        mode='markers',
        marker={"size": 6},
        name='Single Issue Magazine')

    trace33 = go.Scatter(
        y=dff['Spiral-bound'],
        x=dff["dateOrder"],
        mode='lines',
        marker={"size": 5},
        name='Spiral-bound')

    trace34 = go.Scatter(
        y=dff['Sports'],
        x=dff["dateOrder"],
        mode='lines+markers',
        marker={"size": 5.5},
        name='Sports')

    trace35 = go.Scatter(
        y=dff['Tools & Home Improvement'],
        x=dff["dateOrder"],
        mode='markers',
        marker={"size": 6},
        name='Tool & Home Improvement')

    trace36 = go.Scatter(
        y=dff['Toy'], x=dff["dateOrder"],
        mode='lines',
        marker={"size": 5},
        name='Toy')

    trace37 = go.Scatter(
        y=dff['Unknown Binding'],
        x=dff["dateOrder"],
        mode='lines+markers',
        marker={"size": 5.5},
        name='Unknown Binding')

    trace38 = go.Scatter(
        y=dff['Video Game'],
        x=dff["dateOrder"],
        mode='markers',
        marker={"size": 6},
        name='Video Game')

    trace39 = go.Scatter(
        y=dff['Wireless Phone Accessory'],
        x=dff["dateOrder"],
        mode='lines',
        marker={"size": 5},
        name='Wireless Phone Accessory')

    return {
        'data': [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9,
                 trace10, trace11, trace12, trace13, trace14, trace15, trace16, trace17,
                 trace18, trace19, trace20, trace21, trace22, trace23, trace24, trace25,
                 trace26, trace27, trace28, trace29, trace30, trace31, trace32, trace33,
                 trace34, trace35, trace36, trace37, trace38, trace39],
        'layout': go.Layout(
            title="Amount Spent on Amazon from " + str(titleDate1) + ' - ' + str(titleDate2),
            yaxis={
                'title': 'Amount Spent',
                'range': [0, 550],
                'tick0': 0,
                'dtick': 50
            },
            xaxis={
                'tickangle': 60
            },
            height=900,
            plot_bgcolor="rgb(105, 105, 105)",
            paper_bgcolor="rgb(105, 105, 105)",
            font={'color': '#eff4f4'}
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
