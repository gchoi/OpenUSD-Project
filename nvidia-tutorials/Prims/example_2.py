"""
Example 2: Defining a Sphere Prim

#usda 1.0

def Sphere "hello"
{
    double radius = 2
}
"""

from pxr import Usd, UsdGeom

file_path = "_assets/sphere_prim.usda"
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

# Define a prim of type `Sphere` at path `/hello`:
sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, "/hello")
sphere.CreateRadiusAttr().Set(2)

# Save the stage:
stage.Save()
