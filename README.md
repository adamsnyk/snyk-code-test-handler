## Snyk Code to ...

Pipe `snyk code test --json` into other artifacts and formats.

We're not sure where we're going with this but we need Snyk Code reporting support.

To put new Snyk Code tests into a python dict, do:

`snyk code test --json | python code_test_report`

To run this on example test outputs, do:

`cat examples/code_tests.json | python code_test_report`

This is a start, enjoy!
