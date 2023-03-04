



def coords_dms_to_dec(coordinate_dms):
    """ Docstring """

    # Formula: coord_dec = deg + (min / 60) + (sec / 3600)

    if coordinate_dms is not None:
        degree, minute, second = tuple(coordinate_dms)

        coordinate_dec = round(degree + (minute / 60) + (second / 3600), ndigits=6)

        return coordinate_dec
