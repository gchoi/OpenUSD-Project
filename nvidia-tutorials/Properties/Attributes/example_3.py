"""
Example 3: Setting Attribute Values

==== Before Changing Attribute Values ====
Size: 2.0
Display Color: None
Extent: [(-1, -1, -1), (1, 1, 1)]
==== After Changing Attribute Values ====
Size: 4.0
Display Color: [(0, 1, 0)]
Extent: [(-2, -2, -2), (2, 2, 2)]

#usda 1.0

def Xform "World"
{
    def Sphere "Sphere"
    {
    }

    def Cube "Cube"
    {
        float3[] extent = [(-2, -2, -2), (2, 2, 2)]
        color3f[] primvars:displayColor = [(0, 1, 0)]
        double size = 4
        double3 xformOp:translate = (5, 0, 0)
        uniform token[] xformOpOrder = ["xformOp:translate"]
    }
}
"""

from pxr import Usd, UsdGeom, Gf

file_path = "_assets/attributes_ex3.usda"
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")

sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, world_xform.GetPath().AppendPath("Sphere"))
cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Cube"))
UsdGeom.XformCommonAPI(cube).SetTranslate(Gf.Vec3d(5,0,0))

# Get the size, display color, and extent attributes of the sphere
cube_size: Usd.Attribute = cube.GetSizeAttr()
cube_displaycolor: Usd.Attribute = cube.GetDisplayColorAttr()
cube_extent: Usd.Attribute = cube.GetExtentAttr()

print("==== Before Changing Attribute Values ====")
print(f"Size: {cube_size.Get()}")
print(f"Display Color: {cube_displaycolor.Get()}")
print(f"Extent: {cube_extent.Get()}")

# Modify the radius, extent, and display color attributes:
cube_size.Set(cube_size.Get() * 2)
cube_extent.Set(cube_extent.Get() * 2)
cube_displaycolor.Set([(0.0, 1.0, 0.0)])

print("==== After Changing Attribute Values ====")
print(f"Size: {cube_size.Get()}")
print(f"Display Color: {cube_displaycolor.Get()}")
print(f"Extent: {cube_extent.Get()}")

stage.Save()
