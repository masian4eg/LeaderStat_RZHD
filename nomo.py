import plotly.graph_objects as go
import numpy as np  

KilometryX = np.arange(100) 
fig = go.Figure()
fig.add_trace(go.Scatter(
        x=KilometryX[1:],
        y=np.zeros(100),
        error_y=dict(
            type='data',
            symmetric=False,
            array=np.zeros(100),
            arrayminus=np.full(100, -1))
        )
)
for i in range(1, 100, 1):
 reference_line = go.Scatter(x=[i, i+19],
                            y=[1, 20],
                            mode="lines",
                            line=go.scatter.Line(color="gray"),
                            showlegend=False)
 fig.add_trace(reference_line)                            
#From = 1To = 100Step = 1
#KilometryX = np.arange(100) #np.arange(From, To, Step)
#fig.add_trace(go.Scatter(x=KilometryX[1:], y=np.ones(100), mode='lines'))
#for i in range(1, 100, 1):
#  fig.add_trace(go.Scatter(
#    x=[i, i+10],
#    y=[1, 20],
#    name = '<b>Ли</b>нейка', # Style name/legend entry with html tags
#    connectgaps=False # override default to connect the gaps
#  ))

#fig.add_trace(go.Scatter(
#        x=[1,10],  #KilometryX[1:],
#        x0=[1,10],
#        y=[1,20],        #np.ones(100),
#        dx=10,
#        error_y=dict(
#            type='data',
#            symmetric=False,
#            array=np.zeros(100),
#            arrayminus=np.full(100, -20))
#        )
#)

#fig = go.Figure(data=go.Scatter(
#        x=[1, 2, 3, 4],
#        y=[1, 1, 1, 1],
#        error_y=dict(
#            type='data',
#            symmetric=False,
#            array=[0,0,0,0],
#            arrayminus=[-20, -20, -20, -20])
#        ))
#fig.update_yaxes(type="log", range=[10, 10])
fig.show()
