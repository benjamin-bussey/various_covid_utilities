import matplotlib.pyplot as plt
import constants
from scrapers.worldometer_scraping import get_worldometer_world_data, get_worldometer_us_data

plt.figure(figsize=(20, 10))


def generate_countries_scatterplot(df=get_worldometer_world_data(), data_filter=constants.G7_COUNTRIES,
                                   title_modifier='G7 Country'):

    plot_df = df[df['Country/Entity'].isin(data_filter)]

    ax1 = plot_df.plot.scatter(
        x='Tot Cases per 1M pop',
        y='Deaths per 1M pop',
        c='Total Cases',
        colormap='YlOrRd',
    )

    ax1.set_facecolor('xkcd:black')

    for x, y, z in zip(plot_df['Tot Cases per 1M pop'], plot_df['Deaths per 1M pop'], plot_df['Country/Entity']):
        label = f"{z} \n {round(x)} , {round(y)}"

        plt.annotate(
            label,
            xy=(x, y),
            textcoords="offset points",
            xytext=(18, 4),
            ha='center',
            color='white'
        )

    plt.axis([0.0, 14000.0, 0.0, 800.0])
    plt.title(f'Deaths/M and Cases/M per {title_modifier}')
    plt.show()


def generate_state_scatterplot(df=get_worldometer_us_data(), data_filter=constants.US_STATES,
                                   title_modifier='US State'):

    plot_df = df

    ax2 = plot_df.plot.scatter(
        x='Tot Cases per 1M pop',
        y='Deaths per 1M pop',
        c='Total Cases',
        colormap='YlOrRd',
    )

    ax2.set_facecolor('xkcd:black')

    for x, y, z in zip(plot_df['Tot Cases per 1M pop'], plot_df['Deaths per 1M pop'], plot_df['State']):
        label = f"{z}"

        plt.annotate(
            label,
            xy=(x, y),
            textcoords="offset points",
            xytext=(18, 4),
            ha='center',
            color='white'
        )

    plt.axis([0.0, 24000.0, 0.0, 2000.0])
    plt.title(f'Deaths/M and Cases/M per {title_modifier}')
    plt.show()


def main():
    generate_countries_scatterplot()
    generate_state_scatterplot()


if __name__ == '__main__':
    main()
