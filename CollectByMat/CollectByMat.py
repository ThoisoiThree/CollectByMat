import c4d
from c4d import gui

def main():
    # Get all materials in the scene
    materials = doc.GetMaterials()

    # Loop through each material
    for mat in materials:
        # Select the material
        doc.SetActiveMaterial(mat)

        # Press the "Select material Tags/Objects" button
        c4d.CallCommand(16370)

        # Call the "Group Objects" command
        c4d.CallCommand(100004772)

        # Get the active object (the newly created null)
        null = doc.GetActiveObject()

        # Name the null object after the material
        null.SetName(mat.GetName())

    # Update the scene
    c4d.EventAdd()

if __name__=='__main__':
    main()