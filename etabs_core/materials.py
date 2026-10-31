import math

def define_concretes(sapmodel, cfg):
    """Define los materiales de concreto"""
    weight = cfg.get("weight", 2.4)
    poisson = cfg.get("poisson", 0.20)
    thermal_coef = cfg.get("thermal_coef", 0.0000099)

    for item in cfg["grades"]:
        name = item["name"]
        fc = item["fc"]
        # E.060/ACI-318: Ec = 15000 * sqrt(f'c) [kg/cm2] * factor 10 para Tonf/m2
        e_modulus = 15000 * math.sqrt(fc) * 10

        sapmodel.PropMaterial.SetMaterial(name, 2)  # 2: Concreto
        sapmodel.PropMaterial.SetWeightAndMass(name, 1, weight)
        sapmodel.PropMaterial.SetMpIsotropic(name, e_modulus, poisson, thermal_coef)
        sapmodel.PropMaterial.SetOConcrete(
            name,
            fc * 10,       # Resistencia en Tonf/m2
            False,         # IsLightweight
            0,             # FcsFactor
            2,             # Mander
            4,             # Concrete Hysteretic
            0.002219,      # Deformación en fc
            0.005          # Deformación última
        )

def define_rebars(sapmodel, cfg):
    """Rebar Grado 60"""
    name = cfg["name"]
    sapmodel.PropMaterial.SetMaterial(name, 6)  # 6: Rebar
    sapmodel.PropMaterial.SetWeightAndMass(name, 1, cfg["weight"])
    sapmodel.PropMaterial.SetORebar_1(
        name,
        cfg["fy"],
        cfg["fu"],
        cfg["fye"],
        cfg["fue"],
        1,
        1,
        0.01,
        0.09,
        -0.1,
        False
    )
    sapmodel.PropMaterial.SetMPUniaxial(name, cfg["e_modulus"], cfg["thermal_coef"])
