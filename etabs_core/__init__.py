"""Paquete etabs_core para automatización de ETABS bajo normativa NTP."""

from .connection import get_etabs_model
from .materials import define_concretes, define_rebars
from .sections import define_columns, define_beams, define_slabs
from .structural import define_diaphragms, define_piers
from .loads import setup_load_patterns, setup_load_combinations, setup_mass_source

__all__ = [
    "get_etabs_model",
    "define_concretes",
    "define_rebars",
    "define_columns",
    "define_beams",
    "define_slabs",
    "define_diaphragms",
    "define_piers",
    "setup_load_patterns",
    "setup_load_combinations",
    "setup_mass_source",
]
