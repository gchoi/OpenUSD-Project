"""
Example 1: Setting a Default Prim

#usda 1.0
(
    defaultPrim = "hello"
)

def "hello"
{
    def "world"
    {
    }
}
"""

from pxr import Usd

file_path = "_assets/default_prim.usda"
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)
stage.DefinePrim("/hello")
stage.DefinePrim("/hello/world")
hello_prim: Usd.Prim = stage.GetPrimAtPath("/hello")

# Set the default primitive of the stage to the primitive at "/hello":
stage.SetDefaultPrim(hello_prim)

stage.Save()
