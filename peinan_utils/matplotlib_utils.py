from pathlib import Path

import matplotlib
from matplotlib import font_manager


def init_matplotlib():
    FONTS_DIR = 'fonts'
    FONT_NAME = 'Noto Sans CJK JP'
    FONT_WEIGHT = 'medium'

    font_settings = {
        'family': FONT_NAME,
        'weight': FONT_WEIGHT
    }

    font_dir_path = Path(__file__).parent.resolve() / Path(FONTS_DIR)
    font_dirs = [font_dir_path, ]
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
    font_list = font_manager.createFontList(font_files)
    font_manager.fontManager.ttflist.extend(font_list)

    matplotlib.rc('font', **font_settings)
