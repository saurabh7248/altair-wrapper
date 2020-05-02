import altair as alt

def multi_line_chart(data_frame,x_axis,lines,value):
    return alt.Chart(data_frame).mark_line().encode(x=x_axis,
                                                    y=value,
                                                    color=lines)