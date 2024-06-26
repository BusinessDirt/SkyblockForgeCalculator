import subprocess

def setup():
    # validate python installation and install packages
    from Setup.SetupPython import PythonConfiguration as PythonRequirements
    PythonRequirements.validate(packages=[])

    # fetch neu-repo
    print("\nUpdating submodules...")
    subprocess.call(["git", "submodule", "update", "--init", "--recursive"])