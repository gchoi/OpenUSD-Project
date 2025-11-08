"""
Example 1: Adding a Reference

#usda 1.0

def Xform "World"
{
    def Sphere "Sphere"
    {
    }

    def "Cube_Ref" (
        prepend references = @./cube.usda@
    )
    {
        double3 xformOp:translate = (5, 0, 0)
        uniform token[] xformOpOrder = ["xformOp:translate"]
    }
}
"""

from pxr import Usd, UsdGeom, Gf

# Create a new stage and define a cube:
file_path = "_assets/cube.usda"
stage = Usd.Stage.CreateNew(file_path)
cube = UsdGeom.Cube.Define(stage, "/Cube")
stage.SetDefaultPrim(cube.GetPrim())
stage.Save()

# Create a second file path and stage, define a world and a sphere:
second_file_path = "_assets/shapes.usda"
stage = Usd.Stage.CreateNew(second_file_path)
world = UsdGeom.Xform.Define(stage, "/World")
UsdGeom.Sphere.Define(stage, world.GetPath().AppendPath("Sphere"))

# Define a reference prim and set its translation:
reference_prim = stage.DefinePrim(world.GetPath().AppendPath("Cube_Ref"))

# Add a reference to the "cube.usda" file:
reference_prim.GetReferences().AddReference("./cube.usda")
# Position the cube
UsdGeom.XformCommonAPI(reference_prim).SetTranslate(Gf.Vec3d(5, 0, 0))

stage.Save()
