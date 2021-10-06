# Snyk Code to HTML

## Getting Started

Pipe `snyk code test --json` into other artifacts and formats.

We're not sure where we're going with this but we need Snyk Code reporting support.

To put new Snyk Code tests into a python dict, do:

`snyk code test --json | python3 code_test_report`

To run this on example test outputs, do:

`cat examples/code_tests.json | python3 code_test_report`

This is a start, enjoy!

## Example in Automated Context

```
curl https://raw.githubusercontent.com/adamsnyk/snyk-code-test-handler/master/code_test_report/__main__.py > code_test_report.py
snyk code test --json | python3 code_test_report.py
rm code_test_report.py
open output.html
```

OR 

```
curl https://raw.githubusercontent.com/adamsnyk/snyk-code-test-handler/master/code_test_report/__main__.py > code_test_report.py
cat code_tests.json | python3 code_test_report.py
rm code_test_report.py
open output.html
```

## HTML Output

HTML ourput is currently under the `output.html` but we can customise the location soon!