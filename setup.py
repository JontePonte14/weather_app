from setuptools import setup, find_packages
# Generate with chat.gpt

setup(
    name="weather_app",
    version="1.0.0",
    description="A GUI weather application using OpenWeatherMap API and tkinter",
    author="Jonathan",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "certifi>=2025.4.26",
        "charset-normalizer>=3.4.2",
        "idna>=3.10",
        "pillow>=11.2.1",
        "python-dotenv>=1.1.0",
        "requests>=2.32.3",
        "urllib3>=2.4.0"
    ],
    entry_points={
        "console_scripts": [
            "weather-app=weather_app.main:main"
        ]
    },
    include_package_data=True,
    python_requires=">=3.7",
)
