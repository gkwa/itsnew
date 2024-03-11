import argparse

from . import main2


def main() -> int:
    parser = argparse.ArgumentParser(description="Process data.json file")
    parser.add_argument("data_file", type=str, help="Path to data.json file")
    args = parser.parse_args()

    main2.do_work(args.data_file)
    print(f"updated {args.data_file}")
    return 0
