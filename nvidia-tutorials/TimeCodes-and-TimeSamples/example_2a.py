
"""
Example 2: Setting TimeSamples for Attributes

#usda 1.0
(
    endTimeCode = 60
    startTimeCode = 1
)

def Xform "World"
{
    def Sphere "Sphere"
    {
        double3 xformOp:translate.timeSamples = {
            1: (0, 5.5, 0),
            30: (0, -4.5, 0),
            45: (0, -5, 0),
            50: (0, -3.25, 0),
            60: (0, 5.5, 0),
        }
        uniform token[] xformOpOrder = ["xformOp:translate"]
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

stage.SetStartTimeCode(1)
stage.SetEndTimeCode(60)

# Grab the translate
if translate_attr := sphere.GetTranslateOp().GetAttr():
    translate_attr.Clear()

# Create XformCommonAPI object for the sphere
sphere_xform_api = UsdGeom.XformCommonAPI(sphere)

# Set translation of the sphere at time 1
sphere_xform_api.SetTranslate(Gf.Vec3d(0,  5.50, 0), time=1)
# Set translation of the sphere at time 30
sphere_xform_api.SetTranslate(Gf.Vec3d(0, -4.50, 0), time=30)
# Set translation of the sphere at time 45
sphere_xform_api.SetTranslate(Gf.Vec3d(0, -5.00, 0), time=45)
# Set translation of the sphere at time 50
sphere_xform_api.SetTranslate(Gf.Vec3d(0, -3.25, 0), time=50)
# Set translation of the sphere at time 60
sphere_xform_api.SetTranslate(Gf.Vec3d(0,  5.50, 0), time=60)

# Export to a new flattened layer for this example.
stage.Export("_assets/timecode_ex2a.usda", addSourceFileComment=False)
