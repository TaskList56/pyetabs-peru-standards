def define_columns(sapmodel, cfg):
    """Crea las secciones rectangulares de columnas en ETABS."""
    default_mat = cfg.get("default_material")
    for col in cfg["items"]:
        mat = col.get("material", default_mat)
        sapmodel.PropFrame.SetRectangle(
            col["name"],
            mat,
            col["t3"],
            col["t2"],
            1,
            col.get("notes", "")
        )

def define_beams(sapmodel, cfg):
    """Crea las secciones rectangulares de vigas en ETABS."""
    default_mat = cfg.get("default_material")
    for beam in cfg["items"]:
        mat = beam.get("material", default_mat)
        sapmodel.PropFrame.SetRectangle(
            beam["name"],
            mat,
            beam["t3"],
            beam["t2"],
            1,
            beam.get("notes", "")
        )

def define_slabs(sapmodel, cfg):
    """Crea las losas aligeradas (nervadas / ribbed) en ETABS."""
    for slab in cfg["items"]:
        name = slab["name"]
        sapmodel.PropArea.SetSlab(
            name,
            2,  # 2: Ribbed (aligerada)
            1,  # 1: Shell-Thin
            slab["material"],
            slab["slab_thickness"],
            12,
            slab.get("notes", "")
        )
        sapmodel.PropArea.SetSlabRibbed(
            name,
            slab["overall_depth"],
            slab["slab_thickness"],
            slab["stem_width_top"],
            slab["stem_width_bottom"],
            slab["rib_spacing"],
            slab.get("rib_dir", 1)
        )
