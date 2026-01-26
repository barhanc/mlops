import io
import base64
import matplotlib.pyplot as plt

from typing import Annotated
from fastmcp import FastMCP


mcp = FastMCP("Line plot generator")


@mcp.tool(description="Create a line plot from numerical data and return a base64 encoded PNG.")
def get_line_plot(
    data: Annotated[list[list[float]], "A list of lists of numbers to plot."],
    title: Annotated[str, "The title of the plot."] = "",
    xlabel: Annotated[str, "Label for the X-axis."] = "",
    ylabel: Annotated[str, "Label for the Y-axis."] = "",
    legend: Annotated[bool, "Whether to show the legend."] = False,
) -> str:
    plt.figure(figsize=(10, 6))

    for i, points in enumerate(data):
        plt.plot(points, label=f"Series {i}")

    if legend:
        plt.legend()

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)

    return base64.b64encode(buf.read()).decode()


if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8004)
