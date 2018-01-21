from setuptools import setup

setup(name="Bwb",
      packages=["orangebiodepot"],
      package_data={"orangebiodepot": ["icons/*.svg"]},
      classifiers=["Example :: Invalid"],
      # Declare orangedemo package to contain widgets for the "BioDepot" category
      entry_points={"orange.widgets": "Bwb = orangebiodepot"},
      )
