#!/usr/bin/env python3

import argparse
import json
from datetime import datetime
import sys


def get_data_from_stdin() -> dict:
    return json.load(sys.stdin)


def get_data_from_file(file_path: str) -> dict:
    with open(file_path) as f:
        data = json.load(f)
    return data


def fetch_simple_results(data: dict) -> list:
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

    return simple_results

def compose_html_results(simple_results: list) -> str:
    html_results = [
        """
        <div style="padding-bottom: 24px;">
            <div>Vuln Type: {}</div>
            <div>Severity: {}</div>
            <div>Message: {}</div>
            <div>File: {}</div>
            <div>Lines: {}</div>
        </div>\n
        """.format(
            simple_result['type'],
            simple_result['level'],
            simple_result['message'],
            simple_result['file'],
            simple_result['lines'],
        ) for simple_result in simple_results
    ]
    return " ".join(html_results)

def compose_html_file(simple_results: list, html_path: str) -> None:
    html = '''
        <html>
            <body>
                <h2>Snyk Code Test</h2>
                <h3>Date + Time: {}</h3>
                <div style="height: 24px;" />
                <h3>Results:</h3>
                {}
            </body>
        </html>
    '''.format(
        datetime.now(),
        compose_html_results(simple_results=simple_results)
    )

    with open(html_path, 'w') as f:
        f.write(html)

def cli():
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

    simple_results = fetch_simple_results(data)

    compose_html_file(simple_results=simple_results, html_path='output.html')

if __name__ == "__main__":
    cli()
