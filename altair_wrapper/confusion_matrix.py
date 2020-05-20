import altair as alt

def confusion_matrix(data_frame,x_axis,y_axis,color,with_text = True):
    base = alt.Chart(data_frame).encode(x = x_axis , y = y_axis)
    heatmap = base.mark_rect().encode(color = color)
    text = base.mark_text(baseline="middle").encode(color = color)
    return heatmap + text if with_text else heatmap