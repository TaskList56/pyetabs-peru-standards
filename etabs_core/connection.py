import comtypes.client

def get_etabs_model():
    """Obtiene la referencia a SapModel de la instancia activa de ETABS"""
    helper = comtypes.client.CreateObject("ETABSv1.Helper")
    helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)
    etabs_object = helper.GetObject("CSI.ETABS.API.ETABSObject")
    if etabs_object is None:
        raise RuntimeError("No se encontró una instancia activa de ETABS")
    return etabs_object.SapModel
