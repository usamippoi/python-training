# from mypackage.mod1 import double as double
# from mypackage.mod2 import square as square

# __all__ = ["mod1", "mod2"]

## https://qiita.com/suzuki-kei/items/8fea67655abf216a5013
import os, glob

__all__ = [
    os.path.split(os.path.splitext(file)[0])[1]
    for file in glob.glob(os.path.join(os.path.dirname(__file__), '[a-zA-Z0-9]*.py'))
]