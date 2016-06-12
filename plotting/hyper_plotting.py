from matplotlib import pyplot as plot
from plotting_utils import generate_colors


def plot_histogram(data_series, title=None, num_bins=None, labels=None, colors=None,
                   histype="stepfilled", normed=False, gray_scale=False, stacked=False, plot_num=1):
    """
    Plot multiple histograms
    :param data_series: list of iterable
    :param title:
    :param num_bins:
    :param labels:
    :param colors:
    :param histype:
    :param normed:
    :param gray_scale:
    :param stacked:
    :param plot_num:
    :return:
    """
    plot.figure(plot_num)
    if title:
        plot.title(title)

    yd = len(data_series)

    if (labels and len(labels) != yd) or (num_bins and len(num_bins) != yd) \
            or (colors and len(colors) != yd):
        raise Exception("labels/bins/colors has different dimensions as data series")

    if not colors:
        colors = generate_colors(yd, gray_scale)
    for i in xrange(yd):
        plot.hist(data_series[i], bins=num_bins[i] if num_bins else 20, histtype=histype, normed=normed,
                  label=labels[i] if labels else None, alpha=0.7, color=colors[i], stacked=stacked)

    plot.legend(loc='upper right')


def plot_scatter(data_series, title=None, labels=None, colors=None, gray_scale=False, size=None, plot_num=1):
    """
    Plot scatter plot for multiple data series
    :param data_series: list of tuple (x,y)
    :param title:
    :param labels:
    :param colors:
    :param gray_scale:
    :param size:
    :param plot_num:
    :return:
    """
    plot.figure(plot_num)
    if title:
        plot.title(title)

    yd = len(data_series)

    if (labels and len(labels) != yd) or (size and len(size) != yd) \
            or (colors and len(colors) != yd):
        raise Exception("sizes/colors has different dimensions as data series")

    if not colors:
        colors = generate_colors(yd, gray_scale)

    for i in xrange(yd):
        x, y = data_series[i]
        plot.scatter(x, y, alpha=0.8, c=colors[i], s=size[i] if size else 15, label=labels[i] if labels else None)
