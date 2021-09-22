#!/usr/bin/env python3

import argparse
import json
import pprint
import sys


def get_data_from_stdin() -> dict:
    return json.load(sys.stdin)


def get_data_from_file(file_path: str) -> dict:
    with open(file_path) as f:
        data = json.load(f)
    return data


def parse_data(data: dict) -> list:
    results = data["runs"][0]["results"]

    simple_results = []

    for result in results:
        simple_result = {}
        simple_result["type"] = result["ruleId"]
        simple_result["level"] = result["level"]
        simple_result["message"] = result["message"]["text"]
        simple_result["file"] = result["locations"][0]["physicalLocation"][
            "artifactLocation"
        ]["uri"]
        simple_result["lines"] = "{} - {}".format(
            result["locations"][0]["physicalLocation"]["region"]["startLine"],
            result["locations"][0]["physicalLocation"]["region"]["endLine"],
        )
        simple_results.append(simple_result)

    pprint.pprint(simple_results)
    print("\nTotal Issues: {}\n".format(len(simple_results)))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Simplify Snyk Code output.")
    parser.add_argument(
        "--file",
        type=str,
        metavar="/path/to/file",
        help="File path of the json report from Snyk Code.",
        required=False,
    )
    args = parser.parse_args()

    if args.file is not None:
        data = get_data_from_file(args.file)
    else:
        data = get_data_from_stdin()

    parse_data(data)
