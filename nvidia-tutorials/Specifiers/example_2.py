"""
Example 2: Non‑destructive over Edits and class Inherit

#usda 1.0
(
    subLayers = [
        @specifiers_base.usda@
    ]
)

over "World"
{
    over "Box" (
        prepend inherits = </World/_Look/_green>
    )
    {
        double size = 4
    }
}
"""

from pxr import Usd, UsdGeom, Sdf

new_file_path = "_assets/specifiers_over_base.usda"
base_file_path = "specifiers_base.usda"  # path relative to the new file

stage = Usd.Stage.CreateNew(new_file_path)

# Base is weaker than the root layer (root opinions are strongest)
stage.GetRootLayer().subLayerPaths = [base_file_path]

prim_path = "/World/Box"

# Author an override for the same prim
stage.OverridePrim(prim_path)

# Get the cube and change its size
box_prim_cube = UsdGeom.Cube.Get(stage, prim_path)
box_prim_cube.GetSizeAttr().Set(4.0)

# Compose the class onto the box using an inherit arc
box_prim_cube.GetPrim().GetInherits().AddInherit(Sdf.Path("/World/_Look/_green"))

# SdfPrimSpec handles, ordered strong to weak
for prim_spec in box_prim_cube.GetPrim().GetPrimStack():
    print(" - layer:", prim_spec.layer.identifier.split('/')[-1], "specifier:", prim_spec.specifier)

stage.Save()
