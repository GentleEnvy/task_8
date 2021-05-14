from plotly.graph_objs import Figure, Bar


def _generate_diff(data: list[tuple[int, int]]) -> list[int]:
    diff = []
    for man, woman in data:
        if woman > man:
            diff.append(man)
        else:
            diff.append(-woman)
    return diff


class Renderer:
    def __init__(self, data: list[tuple[int, int]]):
        self._men: list[int] = [man__woman[0] for man__woman in data]
        self._women: list[int] = [man__woman[1] for man__woman in data]
        self._diff: list[int] = _generate_diff(data)

    @property
    def figure(self) -> Figure:
        ages = list(range(len(self._men)))
        fig = Figure()
        fig.add_trace(Bar(
            y=ages, x=self._women, marker=dict(color='red'), orientation='h',
            name='women', width=1
        ))
        fig.add_trace(Bar(
            y=ages, x=[-e for e in self._men], marker=dict(color='green'),
            orientation='h', name='men', width=1
        ))
        fig.add_trace(Bar(
            y=ages, x=self._diff, marker=dict(color='blue'), orientation='h',
            name='diff', width=1
        ))
        fig.update_layout(barmode='overlay')
        fig.update_xaxes(zeroline=True, zerolinewidth=4, zerolinecolor='purple')

        return fig
