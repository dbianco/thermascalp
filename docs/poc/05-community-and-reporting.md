# PoC 5: Community and reporting

- **Test report template:** [`.github/ISSUE_TEMPLATE/bench-test-report.md`](../../.github/ISSUE_TEMPLATE/bench-test-report.md)
  so contributors log results in one format.
- **Dummy head first:** publish PoC 1 before anything else so others can reproduce data.
- **Clinician and patient feedback:** a short interview guide for oncology nurses and patient advocates covering
  setup time, noise, comfort, tubing, and cleaning. Gather opinions only; no testing on people.
- **Simulation:** [`tools/ice_runtime.py`](../../tools/ice_runtime.py) lets people explore tank sizing without hardware.
  Run `python3 tools/ice_runtime.py --ice-kg 3 --water-kg 3`.
