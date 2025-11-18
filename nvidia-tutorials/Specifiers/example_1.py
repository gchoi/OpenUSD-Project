"""
Example 1: Authoring defs and a class in a Base Layer

#usda 1.0
(
    defaultPrim = "World"
)

def Xform "World"
{
    def Cube "Box"
    {
        double size = 2
    }

    def Cube "Box_2"
    {
        double size = 2
        double3 xformOp:translate = (5, 0, 0)
        uniform token[] xformOpOrder = ["xformOp:translate"]
    }

    def "_Look"
    {
        class "_green"
        {
            color3f[] primvars:displayColor = [(0.1, 0.8, 0.2)]
        }
    }
}
"""

from pxr import Usd, UsdGeom, Sdf, Gf

base_file_path = "_assets/specifiers_base.usda"

stage = Usd.Stage.CreateNew(base_file_path)

# Create a simple scene with two cubes
world = UsdGeom.Xform.Define(stage, "/World")
stage.SetDefaultPrim(world.GetPrim())

box_prim_cube = UsdGeom.Cube.Define(stage, world.GetPath().AppendChild("Box"))
box_prim_cube.GetSizeAttr().Set(2.0)

box_2_prim_cube = UsdGeom.Cube.Define(stage, world.GetPath().AppendChild("Box_2"))
box_2_prim_cube.GetSizeAttr().Set(2.0)
box_2_api = UsdGeom.XformCommonAPI(box_2_prim_cube)
box_2_api.SetTranslate(Gf.Vec3d(5, 0, 0))

# Define a class prim with a displayColor primvar
class_prim = stage.CreateClassPrim(world.GetPath().AppendPath("_Look/_green"))
class_prim_primvar_api = UsdGeom.PrimvarsAPI(class_prim)
class_prim_primvar_api.CreatePrimvar("displayColor", Sdf.ValueTypeNames.Color3fArray).Set([Gf.Vec3f(0.1, 0.8, 0.2)])

# Inspect specifiers
print("box specifier:", box_prim_cube.GetPrim().GetSpecifier())  # Sdf.SpecifierDef
print("box_2 specifier:", box_2_prim_cube.GetPrim().GetSpecifier())  # Sdf.SpecifierDef
print("class_prim specifier:", class_prim.GetSpecifier())  # e.g. Sdf.SpecifierClass

stage.Save()
