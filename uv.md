Instalación:

curl -LsSf https://astral.sh/uv/install.sh | sh

% uv init a_star
Initialized project `a-star` at `/Users/usu/Desktop/codigo/A_star/a_star`


Al ejecutar

uv run hello.py

se crea un entorno virtaul y se ejecuta hello.py


Python versions

Installing and managing Python itself.

    uv python install: Install Python versions.
    uv python list: View available Python versions.
    uv python find: Find an installed Python version.
    uv python pin: Pin the current project to use a specific Python version.
    uv python uninstall: Uninstall a Python version.

Consulta esto:

https://docs.astral.sh/uv/getting-started/features/#the-pip-interface


Managing dependencies

https://docs.astral.sh/uv/concepts/projects/dependencies/#adding-dependencies

developments depedencies:

uv add --dev pytest 

https://docs.astral.sh/uv/concepts/projects/dependencies/#development-dependencies


dependency groups:

https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-groups

uv add --group lint ruff


Download dependencies declared in pyproject.toml using Pip

https://stackoverflow.com/questions/62408719/download-dependencies-declared-in-pyproject-toml-using-pip


Si el proyecto está creado y tenemos un pyproject.toml:

uv run a_star => creará el entorno virtual y ejecutará a_star.py

uv sync => instalará las dependencias declaradas en pyproject.toml

No ha instalado ruff que estaba en el grupo lint. Ejecutar:

uv sync --group lint



