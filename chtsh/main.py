import click

from chtsh.retrieval import coding_query

def main():
    command()


@click.command()
@click.argument("prompt")
def command(prompt):
    coding_query(prompt)

