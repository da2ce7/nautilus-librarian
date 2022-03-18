from test_nautilus_librarian.utils import compact_json

from nautilus_librarian.mods.dvc.domain.diff.path_list import PathList
from nautilus_librarian.mods.dvc.domain.utils import extract_added_files_from_dvc_diff


def test_extract_added_files_from_dvc_diff():

    dvc_diff = {
        "added": [
            {"path": "data/000001/32/000001-32.600.2.tif"},
            {"path": "data/000001/52/000001-52.600.2.tif"},
        ],
        "deleted": [],
        "modified": [],
        "renamed": [],
    }

    path_list = extract_added_files_from_dvc_diff(compact_json(dvc_diff))

    expected_path_list = PathList.from_string_list(
        [
            "data/000001/32/000001-32.600.2.tif",
            "data/000001/52/000001-52.600.2.tif",
        ]
    ).as_plain_list()

    assert path_list == expected_path_list
