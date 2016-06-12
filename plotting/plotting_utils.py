def generate_colors(dim, gray_scale=False):
    """
    Helper function to generate colors for multiple series plot
    :param dim: number of types of data
    :param gray_scale: gray scale colors
    :return:
    """
    if gray_scale:
        return [str(i * 1. / (dim + 1)) for i in xrange(1, dim + 1)]

    if dim < 4:
        return ['r', 'b', 'g'][:dim]

    increment = 1000 / dim
    color_bins = []
    for i in xrange(1, dim + 1):
        idxs = str(i * increment) + "00"
        color_bins.append((0.1 * int(idxs[0]), 0.1 * int(idxs[1]), 0.1 * int(idxs[2])))
    return color_bins
