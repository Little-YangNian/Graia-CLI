from setuptools import setup
import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
setup(
            name="graiax_cli",
            version="0.7",
            author="Chase杨念",
            install_requires="typer",
            author_email="2544704967@qq.com",
            entry_points='''[console_scripts]
                    graiax=graiax_cli.graia_cli:app'''
            ,description="OwO Graia CLI App",
            licence = "AGPL-3.0" ,
            long_description=long_description,
            
            long_description_content_type="text/markdown",
            
            url="https://github.com/Little-YangNian/Graia-CLI",
            
            packages=setuptools.find_packages(),
            
            classifiers=[
                "Programming Language :: Python :: 3",
                
                "Operating System :: OS Independent",    ],
                

        python_requires='>=3.8', )
