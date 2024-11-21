from setuptools import find_packages, setup

setup(
    name="log_event",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi[standard]",
        "SQLAlchemy",
        "pytest",
        "pytest-asyncio",
        "pytest-tornasync",
        "pytest-trio",
        "pytest-twisted",
        "pytz",
        "pyodbc",
        "twisted",
        "pandas",
        "yadisk[async_defaults]",
        "requests",
        "pysmb",
        "aiohttp",
        "asyncpg"
    ],
    extras_require={
        "dev": [
            "black",
            "flake8",
            "isort",
            "pre-commit",
        ],
    },
    entry_points={
        "console_scripts": [
            "format-code = format_code:main",
            "lint = lint:main",
        ]
    },
)
