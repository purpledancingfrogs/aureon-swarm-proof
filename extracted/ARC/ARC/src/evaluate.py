#!/usr/bin/env python
import argparse, sys
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--solver", required=True)
    p.add_argument("--dataset", required=True)
    args = p.parse_args()
    print("EVALUATOR CREATED")
    print("solver:", args.solver)
    print("dataset:", args.dataset)
    sys.exit(0)
if __name__ == "__main__":
    main()
