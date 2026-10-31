def setup_load_patterns(sapmodel, cfg):
    """Añade patrones estáticos"""
    dead_name = cfg.get("dead_name", "CM")
    live_name = cfg.get("live_name", "CV")

    sapmodel.LoadPatterns.ChangeName("Dead", dead_name)
    sapmodel.LoadCases.ChangeName("Dead", dead_name)
    sapmodel.LoadPatterns.ChangeName("Live", live_name)
    sapmodel.LoadCases.ChangeName("Live", live_name)

    # Añadir patrones de sismo estático (Tipo 5 = Quake)
    for quake in cfg.get("seismic", []):
        sapmodel.LoadPatterns.Add(quake["name"], 5)

def setup_load_combinations(sapmodel, cfg):
    """Creación de los combos de carga según NTP E.060 y E.030 y la envolvente de diseño"""
    # Combinaciones lineales (Tipo 0 = Linear Add)
    linear_combos = cfg.get("linear", [])
    created_combo_names = []

    for combo in linear_combos:
        c_name = combo["name"]
        sapmodel.RespCombo.Add(c_name, 0)
        for case_name, factor in combo["factors"].items():
            sapmodel.RespCombo.SetCaseList(c_name, 0, case_name, factor)
        created_combo_names.append(c_name)

    # Envolvente (Tipo 1 = Envelope)
    env_cfg = cfg.get("envelope", {})
    if env_cfg:
        env_name = env_cfg.get("name", "ENVOLVENTE")
        combos_to_include = env_cfg.get("combos", created_combo_names)
        sapmodel.RespCombo.Add(env_name, 1)
        for sub_combo in combos_to_include:
            sapmodel.RespCombo.SetCaseList(env_name, 1, sub_combo, 1.0)

def setup_mass_source(sapmodel, cfg):
    """Masa sísmica"""
    loads_dict = cfg.get("factors", {"CM": 1.0, "CV": 0.25})
    names = list(loads_dict.keys())
    factors = [float(f) for f in loads_dict.values()]

    sapmodel.PropMaterial.SetMassSource_1(
        cfg.get("include_elements", False),
        cfg.get("include_added_mass", False),
        cfg.get("include_loads", True),
        len(names),
        names,
        factors
    )
