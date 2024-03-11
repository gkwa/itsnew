import json
import pathlib


def do_work(data_path):
    if not pathlib.Path(data_path).exists():
        with open(data_path, "w") as file:
            json.dump([], file)

    with open(data_path, "r") as file:
        data = json.load(file)

    checked_targets = set()

    for item in data:
        path_directory = pathlib.Path(item["path"]).parent

        for link in item["links"]:
            target = link["target"]

            absolute_path = path_directory / target

            link["file_exists"] = False
            checked_targets.add(target)

            if absolute_path.exists():
                link["file_exists"] = True

            if absolute_path.with_suffix(".md").exists():
                link["file_exists"] = True

    with open(data_path, "w") as file:
        json.dump(data, file, indent=2)

    return json.dumps(data, indent=2)
