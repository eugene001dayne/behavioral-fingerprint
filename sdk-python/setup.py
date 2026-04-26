from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="behavioralfingerprint",
    version="0.3.0",
    description="Capture how your AI agent behaves at deployment. Monitor how that behavior changes over time.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Eugene Dayne Mawuli",
    author_email="bitelance.team@gmail.com",
    url="https://github.com/eugene001dayne/behavioral-fingerprint",
    py_modules=["behavioralfingerprint"],
    install_requires=["httpx"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)