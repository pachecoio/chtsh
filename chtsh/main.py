import click

from chtsh.retrieval import coding_query

def main():
    command()


@click.command()
@click.option(
    "--prompt",
    "-p",
    help="The prompt to use for the query",
)
def command(prompt):
    coding_query(prompt)

