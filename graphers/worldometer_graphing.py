import constants
from scrapers.worldometer_scraping import get_worldometer_world_data, get_worldometer_us_data
import plotly.express as px


def generate_countries_scatterplot(func=get_worldometer_world_data, data_filter=constants.G7_COUNTRIES,
                                   title_modifier='G7 Country Analysis'):
    df = func()

    plot_df = df[df['Country/Entity'].isin(data_filter)]

    fig = px.scatter(
        data_frame=plot_df,
        x="Tot Cases per 1M pop",
        y="Deaths per 1M pop",
        color=[int(x) for x in plot_df['Tests per 1M pop'].tolist()],
        text="Country/Entity",
        title=f"Cases/M and Deaths/M per {title_modifier}"
    )

    fig.update_traces(textposition='top center')

    fig.show()


def generate_countries_scatterplot3d(func=get_worldometer_world_data, data_filter=None,
                                     title_modifier='G7 Country Analysis'):
    df = func()
    plot_df = df[df['Country/Entity'].isin(data_filter)] if data_filter is not None else df

    plotlyfig = px.scatter_3d(plot_df,
                              x='Tot Cases per 1M pop', y='Deaths per 1M pop', z='Tests per 1M pop',
                              color='Population',
                              symbol='Country/Entity',
                              color_continuous_scale='Inferno',
                              title='Cases, Deaths, and Testing per 1M Population Analysis')

    plotlyfig.show()


def generate_state_scatterplot(func=get_worldometer_us_data, data_filter=constants.US_STATES,
                               title_modifier='US State'):
    df = func()

    plot_df = df

    fig = px.scatter(
        data_frame=plot_df,
        x="Tot Cases per 1M pop",
        y="Deaths per 1M pop",
        text="State",
        title=f"Cases/M and Deaths/M per {title_modifier}"
    )

    fig.update_traces(textposition='top center')

    fig.show()


def generate_state_cases_boxplot(func=get_worldometer_us_data, data_filter=constants.US_STATES):
    df = func()

    fig = px.box(
        df,
        hover_name='State',
        y='Tot Cases per 1M pop',
        points='all',
        title='State Cases per 1M Pop'
    )

    fig.show()

    fig = px.box(
        df,
        hover_name='State',
        y='Deaths per 1M pop',
        points='all',
        title='State Deaths per 1M Pop'
    )

    fig.show()


# ToDo generate dynamic quartile calculation and mapping for state full name -> abbrev
def generate_us_state_cases_impact_chart():
    locations = ["LA", "MS", "FL", "AL", "ND", "GA", "AZ", "TN", "SC", "IA", "AR", "TX", "SD"]

    fig = px.choropleth(
        locations=locations,
        locationmode="USA-states",
        scope="usa",
        title='USA Quartile 4 Cases per 1M Pop States'
    )

    fig.show()


def main():
    # Country comparisons
    generate_countries_scatterplot()
    generate_countries_scatterplot(data_filter=constants.EUROPE,
                                   title_modifier='Europe Country Analysis')
    generate_countries_scatterplot(data_filter=constants.BENS_COUNTRIES,
                                   title_modifier='Ben Country Analysis')

    # All Countries 3d Scatterplot
    generate_countries_scatterplot3d()

    # State comparison
    generate_state_scatterplot()
    generate_state_cases_boxplot()

    generate_us_state_cases_impact_chart()


if __name__ == '__main__':
    main()
