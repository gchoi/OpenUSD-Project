"""
Example 1: Setting Start and End TimeCodes

#usda 1.0
(
    endTimeCode = 60
    startTimeCode = 1
)

def Xform "World"
{
    def Sphere "Sphere"
    {
    }

    def Cube "Backdrop"
    {
        color3f[] primvars:displayColor = [(0, 0, 1)]
        float3 xformOp:scale = (5, 5, 0.1)
        double3 xformOp:translate = (0, 0, -2)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:scale"]
    }
}
"""

from pxr import Usd, UsdGeom, Gf

stage: Usd.Stage = Usd.Stage.Open("_assets/timecode_sample.usda")
world: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")
sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, world.GetPath().AppendPath("Sphere"))
box: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world.GetPath().AppendPath("Backdrop"))
box.GetDisplayColorAttr().Set([(0.0, 0.0, 1.0)])
cube_xform_api = UsdGeom.XformCommonAPI(box)
cube_xform_api.SetScale(Gf.Vec3f(5, 5, 0.1))
cube_xform_api.SetTranslate(Gf.Vec3d(0, 0, -2))

# Set the `start` and `end` timecodes for the stage:
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(60)

# Export to a new flattened layer for this example.
stage.Export("_assets/timecode_ex1.usda", addSourceFileComment=False)
