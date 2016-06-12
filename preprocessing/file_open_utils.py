import zipfile


def get_file(file_name, delimiter=None, headers=None):
    """
    Read file and split on optional delimiter and zip to dict if header is provided
    :param file_name: string
    :param delimiter: string
    :param headers: optional header list, if provided result is a list of dict,
     otherwise list of list or string
    :return:
    """
    with open(file_name, 'r') as f:
        for l in f.readlines():
            line = l.strip().split(delimiter) if delimiter else l.strip()

            if headers:
                line = dict(zip(headers, line))

            yield line


def load_file(file_name, result_list, delimiter=None, headers=None):
    """
    Call get file to load contents in the file to generator and put into a list
    :param file_name:
    :param result_list: result list
    :param delimiter: string
    :param headers: optional header list, if provided result is a list of dict,
     otherwise list of list or string
    :return:
    """
    for l in get_file(file_name, delimiter, headers):
        result_list.append(l)


def load_zip(file_name, line_delimiter=None):
    """
    load content of zip file, split based on optional delimiter
    :param file_name:
    :param line_delimiter: string
    :return: generator, file name, content
    """
    if not zipfile.is_zipfile(file_name):
        raise Exception("Not valid zip file")

    archive = zipfile.ZipFile(file_name)
    for fn in archive.namelist():
        l = archive.read(fn)
        yield fn, l.strip().split(line_delimiter) if line_delimiter else l.strip()
