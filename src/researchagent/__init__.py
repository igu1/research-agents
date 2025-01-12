__version__ = "0.0.1.dev"

from typing import TYPE_CHECKING

from transformers.utils import _LazyModule
from transformers.utils.import_utils import define_import_structure

if TYPE_CHECKING:
    from .agents import *
    from .default_tools import *
    from .e2b_executor import *
    from .gradio_ui import *
    from .local_python_executor import *
    from .models import *
    from .monitoring import *
    from .prompts import *
    from .tools import *
    from .types import *
    from .utils import *


else:
    import sys

    _file = globals()["__file__"]
    import_structure = define_import_structure(_file)
    import_structure[""] = {"__version__": __version__}
    sys.modules[__name__] = _LazyModule(
        __name__,
        _file,
        import_structure,
        module_spec=__spec__,
        extra_objects={"__version__": __version__},
    )
