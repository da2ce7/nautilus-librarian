import typer
from enum import Enum

app = typer.Typer()


@app.command()
def test(echo_string: str):
    typer.echo(f"Testing LibVips module: {echo_string}")


class Step(Enum):
    validate_size = "validate_size"
    resize = "resize"
    modify_icc_profile = "modify_icc_profile"


def validate_size():
    print("- Validating size of the images")


def resize():
    print("- Resizing images")


def icc_modify():
    print("- Modifying ICC color profiles")


def execute_pipeline():
    validate_size()
    resize()
    icc_modify()


stepExecuters = {
    'validate_size': validate_size,
    'resize': resize,
    'modify_icc_profile': icc_modify
}


@app.command()
def process(step: Step = None):
    """
    Execute the image processing pipeline.

    If --step is used, only specified step is executed.
    """
    if not step:
        execute_pipeline()
    else:
        typer.echo(f"Processing images, using step {step}")
        stepExecuters[step.value]()


if __name__ == "__main__":
    app()