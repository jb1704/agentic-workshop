"""Secret lookup that works the same in Colab and on a local machine.

In Colab, add keys under the key icon in the left sidebar (Secrets).
Locally, put them in a .env file next to this repo (see .env.example).
"""

import os


def get_secret(name: str, required: bool = True) -> str | None:
    """Return the secret `name` from Colab secrets, the environment, or .env."""
    try:
        from google.colab import userdata  # type: ignore

        value = userdata.get(name)
        if value:
            return value
    except Exception:
        pass

    value = os.environ.get(name)
    if value:
        return value

    try:
        from dotenv import load_dotenv

        load_dotenv()
        value = os.environ.get(name)
        if value:
            return value
    except ImportError:
        pass

    if required:
        raise RuntimeError(
            f"{name} not found. In Colab add it under Secrets (key icon, left "
            f"sidebar); locally add it to a .env file."
        )
    return None
