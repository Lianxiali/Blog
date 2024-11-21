import os
import gmsh

def mesh_stl_file(input_file, output_file, characteristic_length_factor=0.2, scaling_factor=0.001):
    """
    Mesh a single STL file using Gmsh and save the output.
    """
    # Initialize Gmsh
    gmsh.initialize()
    
    try:
        gmsh.option.setNumber("General.Terminal", 0)  # Suppress Gmsh terminal output
        
        # Load the STL file
        gmsh.merge(input_file)

        # Set mesh density
        gmsh.option.setNumber("Mesh.CharacteristicLengthFactor", characteristic_length_factor)

        # Set mesh scaling factor
        gmsh.option.setNumber("Mesh.ScalingFactor", scaling_factor)

        # Classify surfaces and create geometry
        angle = 40 * 3.14159265359 / 180  # Convert angle to radians
        gmsh.model.mesh.classifySurfaces(angle, True, False)
        gmsh.model.mesh.createGeometry()

        # Synchronize the OpenCASCADE kernel
        gmsh.model.occ.synchronize()

        # Generate the 2D mesh
        gmsh.model.mesh.generate(2)

        # Save the resulting mesh
        gmsh.write(output_file)
        print(f"Processed and saved: {output_file}")

    except Exception as e:
        print(f"Failed to process {input_file}: {e}")
    
    finally:
        # Finalize Gmsh for this file
        gmsh.finalize()


def process_stl_files_recursively(root_folder, characteristic_length_factor=0.2, scaling_factor=0.001):
    """
    Traverse the folder structure recursively, locate STL files, and mesh them.
    """
    i = 0
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            # print(filename)
            if filename.endswith('.stl') and not filename.startswith("remeshed"):
                input_file = os.path.join(dirpath, filename)
                output_file = os.path.join(dirpath, f"remeshed_{filename}")
                i = i + 1
                print(i, end =": ")
                # Mesh the STL file
                mesh_stl_file(input_file, output_file, characteristic_length_factor, scaling_factor)


# Main execution
if __name__ == "__main__":
    cases = ["0528C2-D7", "0528C2-D21", "0828C1-D7", "0828C1-D21", "0925C2-D21"]
    for i, case in enumerate(cases):
        print(f"{i} case : {case}")
        root_folder = rf"/mnt/c/Drives/E/work/2023/project/kidney/Segmentations07032024/Segmentations/cut/{case}/crossSectionData/STL/"
        process_stl_files_recursively(root_folder)
