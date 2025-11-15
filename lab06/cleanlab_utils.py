"""
https://docs.cleanlab.ai/master/tutorials/faq.html#How-to-handle-near-duplicate-data-identified-by-cleanlab
"""

import pandas as pd
from typing import Callable


def merge_duplicate_sets(df, merge_key: str):
    """Generate group keys for each row, then merge intersecting sets.

    :param df: DataFrame with columns 'is_near_duplicate_issue' and 'near_duplicate_sets'
    :param merge_key: Name of the column to store the merged sets
    """

    df[merge_key] = df.apply(construct_group_key, axis=1)
    merged_sets = consolidate_sets(df[merge_key].tolist())
    df[merge_key] = df[merge_key].map(lambda x: next(s for s in merged_sets if x.issubset(s)))
    return df


def construct_group_key(row):
    """Convert near_duplicate_sets into a frozenset and include the row's own index."""
    return frozenset(row["near_duplicate_sets"]).union({row.name})


def consolidate_sets(sets_list):
    """Merge sets if they intersect."""

    # Convert the input list of frozensets to a list of mutable sets
    sets_list = [set(item) for item in sets_list]

    # A flag to keep track of whether any sets were merged in the current iteration
    merged = True

    # Continue the merging process as long as we have merged some sets in the previous iteration
    while merged:
        merged = False
        new_sets = []

        # Iterate through each set in our list
        for current_set in sets_list:
            # Skip empty sets
            if not current_set:
                continue

            # Find all sets that have an intersection with the current set
            intersecting_sets = [s for s in sets_list if s & current_set]

            # If more than one set intersects, set the merged flag to True
            if len(intersecting_sets) > 1:
                merged = True

            # Merge all intersecting sets into one set
            merged_set = set().union(*intersecting_sets)
            new_sets.append(merged_set)

            # Empty the sets we've merged to prevent them from being processed again
            for s in intersecting_sets:
                sets_list[sets_list.index(s)] = set()

        # Replace the original sets list with the new list of merged sets
        sets_list = new_sets

    # Convert the merged sets back to frozensets for the output
    return [frozenset(item) for item in sets_list]


def lowest_score_strategy(sub_df):
    """Keep the row with the lowest near_duplicate_score."""
    return sub_df["near_duplicate_score"].idxmin()


def filter_near_duplicates(data: pd.DataFrame, strategy_fn: Callable = lowest_score_strategy, **strategy_kwargs):
    """
    Given a dataframe with columns 'is_near_duplicate_issue' and 'near_duplicate_sets',
    return a series of boolean values where True indicates the rows to be removed.
    The strategy_fn determines which rows to keep within each near_duplicate_set.

    :param data: DataFrame with is_near_duplicate_issue and near_duplicate_sets columns
    :param strategy_fn: Function to determine which rows to keep within each near_duplicate_set
    :return: Series of boolean values where True indicates rows to be removed.
    """

    # Filter out rows where 'is_near_duplicate_issue' is True to get potential duplicates
    duplicate_rows = data.query("is_near_duplicate_issue").copy()

    # Generate group keys for each row and merge intersecting sets
    group_key = "sets"
    duplicate_rows = merge_duplicate_sets(duplicate_rows, merge_key=group_key)

    # Use the strategy function to determine the indices of the rows to keep for each group
    to_keep_indices = duplicate_rows.groupby(group_key).apply(strategy_fn, **strategy_kwargs).explode().values

    # Produce a boolean series indicating which rows should be removed
    to_remove = ~data.index.isin(to_keep_indices)

    return to_remove
