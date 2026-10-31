import sys
import yaml
from etabs_core.connection import get_etabs_model
from etabs_core.materials import define_concretes, define_rebars
from etabs_core.sections import define_columns, define_beams, define_slabs
from etabs_core.structural import define_diaphragms, define_piers
from etabs_core.loads import setup_load_patterns, setup_load_combinations, setup_mass_source

def run_pipeline(config_path: str = "config.yaml"):
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    sapmodel = get_etabs_model()
    sapmodel.SetPresentUnits(cfg.get("units", 12))

    # Definición de materiales
    define_concretes(sapmodel, cfg["materials"]["concrete"])
    define_rebars(sapmodel, cfg["materials"]["rebar"])

    # Secciones de pórticos y losas
    define_columns(sapmodel, cfg["sections"]["columns"])
    define_beams(sapmodel, cfg["sections"]["beams"])
    define_slabs(sapmodel, cfg["sections"]["slabs"])

    # Diafragmas y piers de muros
    define_diaphragms(sapmodel, cfg["structural"]["diaphragms"])
    define_piers(sapmodel, cfg["structural"]["piers"])

    # Patrones de carga, combos y masa sísmica
    setup_load_patterns(sapmodel, cfg["loads"]["patterns"])
    setup_load_combinations(sapmodel, cfg["loads"]["combinations"])
    setup_mass_source(sapmodel, cfg["loads"]["mass_source"])

    print("Configuración de materiales, secciones y cargas completada con éxito en ETABS")

if __name__ == "__main__":
    config_file = sys.argv[1] if len(sys.argv) > 1 else "config.yaml"
    run_pipeline(config_file)