"""
Main program.
"""

import random
import re

from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt, Confirm
from rich.pretty import pretty_repr
from rich.progress import BarColumn, MofNCompleteColumn, Progress, TextColumn
from rich.table import Table
import questionary

from sortanalyzer import algorithms

def main() -> None:
    """
    Main function.
    """

    console = Console()

    console.print(Panel("A software tool to analyze performance of sorting algorithms.\n\n"
                        "We are going to generate a list to you! "
                        "After its creation, the list will be sorted through some "
                        "sorting algorithms, and the time taken by each of them will "
                        "be shown.",
                        title="[blue bold]SortAnalyzer[/blue bold]",
                        border_style="blue"))

    console.print()

    list_type = questionary.select("What kind of list to generate:",
                                   ["RANDOM LIST", "SORTED LIST (normal order)",
                                    "SORTED LIST (reverse order)"],
                                    pointer="❯").ask()

    if list_type is None:
        return

    list_size = IntPrompt.ask("Type the list size")

    _generated_list = []

    match list_type:
        case "RANDOM LIST":
            _generated_list = [random.randint(1,100*list_size) for i in range(list_size)]
        case "SORTED LIST (normal order)":
            _generated_list = list(range(1,list_size+1))
        case "SORTED LIST (reverse order)":
            _generated_list = list(range(list_size,0,-1))
        case _:
            console.print("Invalid option!")
            return

    console.print("\n[green bold]List generated successfully![/green bold]")

    show_generated_list = Confirm.ask("Show the generated list?")
    if show_generated_list:
        formatted_list = re.sub(
            r"\.\.\. \+\d+", "...", pretty_repr(_generated_list, max_length=10)
        )
        console.print(f"Generated list: {formatted_list}")

    show_sorted_list = Confirm.ask("Show the resulting list for each algorithm?")

    questionary.press_any_key_to_continue(
        message="<Press ENTER to continue...>"
    ).ask()

    console.print("")

    _list_to_work = _generated_list[:]  # A copy of the generated list.

    # Setting analysis:

    algorithms_names = ["Bubble sort", "Selection sort", "Insertion sort", "Quick sort",
                       "Merge sort", "Heap sort"]
    algorithms_funcs = [algorithms.bubble_sort, algorithms.selection_sort,
                        algorithms.insertion_sort, algorithms.quick_sort,
                        algorithms.merge_sort, algorithms.heap_sort]
    algorithms_times = []
    algorithms_resulting_lists = []  # Using string compact format,
                                     # so it does not occupy too much memory.

    console.print("Running algorithms...")

    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Starting analysis...", total=len(algorithms_funcs))

        for name, func in zip(algorithms_names, algorithms_funcs):
            progress.update(task, description=f"[cyan]Running {name}...")

            algorithms_times.append(func(_list_to_work))

            algorithms_resulting_lists.append(re.sub(r"\.\.\. \+\d+", "...",
                                            pretty_repr(_list_to_work, max_length=10)))

            _list_to_work = _generated_list[:]  # Resetting the list to work to its previous state.

            progress.update(task, advance=1)

        progress.update(task, description="[bold green]Analysis complete![/bold green]")

    console.print()

    table = Table(title="Analysis results")

    table.add_column("Algorithm", style="cyan", no_wrap=True)
    table.add_column("Time taken", style="magenta")

    if show_sorted_list:
        table.add_column("Resulting list", style="blue")

        for name, time, sorted_list in zip(algorithms_names,
                                           algorithms_times, algorithms_resulting_lists):
            table.add_row(name, time, sorted_list)
    else:
        for name, time in zip(algorithms_names, algorithms_times):
            table.add_row(name, time)

    console.print(table)
