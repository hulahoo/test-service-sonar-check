import os
from setuptools import setup, find_namespace_packages

install_requires = [
    ('Flask', '2.1.0'),
    ('Flask-WTF', '1.0.1'),
]

CI_PROJECT_NAME = os.environ.get("CI_PROJECT_NAME", "test-data-service")
ARTIFACT_VERSION = os.environ.get("ARTIFACT_VERSION", "local")
CI_PROJECT_TITLE = os.environ.get("CI_PROJECT_TITLE", "Веб-сервис для предоставления тестовых данных")
CI_PROJECT_URL = os.environ.get("CI_PROJECT_URL", "https://gitlab.in.axept.com/rshb/test-data-service/")


setup(
    include_package_data=True,
    name=CI_PROJECT_NAME,
    version=ARTIFACT_VERSION,
    description=CI_PROJECT_TITLE,
    url=CI_PROJECT_URL,
    install_requires=[">=".join(req) for req in install_requires],
    python_requires=">=3.9.1",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "test_data_service.data": ["*.txt", "*.json", "*.stix2"],
    },
    entry_points={
        'console_scripts': [
            CI_PROJECT_NAME + " = " + "test_data_service.main:execute",
        ]
    }
)
