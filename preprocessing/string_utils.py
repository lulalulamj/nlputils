import re

greek_symbol = re.compile(ur"[\u0391-\u03C9]", flags=re.U)
roman_number = re.compile("^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$")
common_scientific_measurements = {
    "rad", "ohm", "j", "v", "w", "Hz", "F", "T", "H"
}

# kilo, mu, micro, nano, giga
common_measure = re.compile(
    ur"[\u03bcmkng]?([amgsnl]|mol)(\^(\+|\-)?[1-9]+)?(/[\u03bcmkn]?([amgsnl]|mol)(\^(\+|\-)?[1-9]+)?)?$",
    flags=re.U)

unit_comp_pat = "(\+|-)?[0-9]+((\.?[0-9]+)|(\,[0-9]{3,3})+)?"
compound_num = "{}(\^{})?".format(unit_comp_pat, unit_comp_pat)
number_pat = re.compile("({}( ?[xX] ?{})?)".format(compound_num, compound_num))
skip_alnum_number_pat = re.compile("[a-zA-Z]")


def contains_greek(token):
    return bool(greek_symbol.search(token))


def contains_roman_numeral(token):
    return bool(roman_number.match(token.upper()))


def is_common_measurement(token):
    """
    Requires the tokenization not insert space at "/",
    which should probably be the standard ...
    :param token:
    :return:
    """
    return bool(common_measure.match(token.lower()))


def single_digit_normalization(string, replace="X"):
    """
    replace very digit with pattern specified in replace
    E.g.  "Model3 has a unit price of $699.0" => "ModelX has a unit price of $XXX.X"
    :param string:
    :param replace: pattern to normalize the digit to
    :return:
    """
    new_str = []
    for i in string:
        if str(i).isdigit():
            new_str.append(replace)
        else:
            new_str.append(i)
    return "".join(new_str)


def num_token_normalization(string, replace="X", skip_alnum=False):
    """
    Replace a whole number into the patten
    E.g. "Model3 has sold 2.5 x 10^8 devices with unit price of $699.0"
    => "ModelX has sold X devices with unit price of $X"
    :param string:
    :param replace:
    :param skip_alnum: skip the replacement of alphanumeric token
    :return:
    """
    if skip_alnum:
        new_l = []
        for l in string.strip().split():
            if skip_alnum_number_pat.search(l):
                new_l.append(l)
            else:
                new_l.append(number_pat.sub(replace, l))
        return " ".join(new_l)

    return number_pat.sub(replace, string)

# print contains_greek(u"abc\u03b1we 1983 best")
# print contains_greek(u"abcwe 1983 best")
# print contains_roman_numeral("abc XXI")
# print contains_roman_numeral("MCDVIIi")
# print num_normalization1("Iphone3 has a unit price of $699.0")
# print num_normalization2("Iphone3 has a unit price of $699.0")
# num_normalization2("Iphone3 has a 13 price of $699.0")
# num_normalization2("Iphone3 has a -15,987 price of $699.0")
# num_normalization2("Iphone3 has a -159,87 price of $699.0")
# num_normalization2("Iphone3 has a -15,987,987 price of $699.0")
# print num_token_normalization("Model3 has sold 2.5 x 10^8 devices with unit price of $699.0")
# print num_token_normalization("Model3 has sold 2.5 x 10^8 devices with unit 3Mn4SO6 of $699.0", skip_alnum=False)
# print single_digit_normalization("Model3 has sold 2.5 x 10^8 devices with unit 3Mn4SO6 of $699.0")
# print num_token_normalization("22.987654^-0.9")
# print num_token_normalization("Iphone3")
