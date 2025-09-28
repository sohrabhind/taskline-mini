from setuptools import setup
import py2exe

main_script = 'taskline.pyw'
icon_file = 'icon.ico'

setup(
    name="Task Manager",
    version="1.0.1",
    author="Sohrab Ahmed",
    author_email="sohrabhind@gmail.com",
    windows=[{'script': main_script, "icon_resources": [(1, icon_file)]}],
    options={'py2exe': {'bundle_files': 3, 'compressed': True}},
    zipfile=None,
    data_files=[('.', [icon_file])]
)
