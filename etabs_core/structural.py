def define_diaphragms(sapmodel, cfg):
    """Diafragmas rígidos o semi-rígidos para los pisos del modelo"""
    prefix = cfg.get("prefix", "Piso")
    semi_rigid = cfg.get("semi_rigid", False)

    stories_data = sapmodel.Story.GetStories()
    # Buscar si se recuperó la lista de nombres de pisos
    story_names = next((item for item in stories_data if isinstance(item, (tuple, list)) and item and isinstance(item[0], str)), None)

    if story_names:
        for name in story_names:
            sapmodel.Diaphragm.SetDiaphragm(f"Diaf_{name}", semi_rigid)
    else:
        num_stories = stories_data[0] if isinstance(stories_data[0], int) else 4
        for i in range(1, num_stories + 1):
            sapmodel.Diaphragm.SetDiaphragm(f"{prefix}-{i}", semi_rigid)

def define_piers(sapmodel, cfg):
    """Registra etiquetas de elementos Pier (muros de corte)."""
    count = cfg.get("count", 4)
    prefix = cfg.get("prefix", "Muro")
    for i in range(1, count + 1):
        sapmodel.PierLabel.SetPier(f"{prefix}-{i}")
