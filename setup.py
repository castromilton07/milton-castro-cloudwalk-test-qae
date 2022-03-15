from setuptools import setup

setup(
    name="cloudwalk_test_qae",
    description="Project Quality Assurance Engineer Test",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "cloudwalk_test_qae=quake_log_parser.main:main",
        ],
    },
)
