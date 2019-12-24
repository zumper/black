import os
from typing import Any, Dict

USE_MYPYC = os.getenv("BLACK_USE_MYPYC", None) == "1"

mypyc_targets = [
    "black.py",
    "blib2to3/pytree.py",
    "blib2to3/pygram.py",
    "blib2to3/pgen2/parse.py",
    "blib2to3/pgen2/grammar.py",
    "blib2to3/pgen2/token.py",
    "blib2to3/pgen2/driver.py",
    "blib2to3/pgen2/pgen.py",
]


def build(setup_kwargs: Dict[str, Any]) -> None:
    if USE_MYPYC:
        from mypyc.build import mypycify

        opt_level = os.getenv("MYPYC_OPT_LEVEL", "3")
        setup_kwargs.update(ext_modules=mypycify(mypyc_targets, opt_level=opt_level))
