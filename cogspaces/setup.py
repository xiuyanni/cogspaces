def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('cogspaces', parent_package, top_path)

    config.add_subpackage('input_data')
    config.add_subpackage('externals')
    config.add_subpackage('model')
    config.add_subpackage('tests')
    config.add_subpackage('datasets')

    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup

    setup(**configuration(top_path='').todict())
