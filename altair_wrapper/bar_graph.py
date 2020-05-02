import altair as alt

def bar_chart(data_frame,x_column,y_column):
    return alt.Chart(data_frame).mark_bar().encode(x=x_column,y=y_column)

def stacked_bar_chart(data_frame,x_column,y_column,stacking_column):
    return alt.Chart(data_frame).mark_bar().encode(x=x_column,y=y_column,color=stacking_column)

def grouped_bar_chart(data_frame,x_column,y_column,grouping_column,col_header_type,col_header_format):
    head = alt.Header(labelOrient="bottom")
    if col_header_type is not None:
        head.formatType = col_header_type
        head.format = col_header_format
    col = alt.Column(grouping_column,header=head)
    return alt.Chart(data_frame).mark_bar().encode(x=alt.X(x_column,axis=None),
                                                   y=alt.Y(y_column,axis=alt.Axis(grid=True)),
                                                   color=x_column,
                                                   column=col)