from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "dl"
COUNT = 9


def test_module_readmes_exist():
    for index in range(COUNT):
        module = ROOT / f"{PREFIX}{index:02d}"
        assert (module / "README.md").is_file()
        for exercise in range(3):
            assert (module / f"ex{exercise:02d}" / "SUBJECT.md").is_file()


def test_no_solution_files_committed():
    for module in ROOT.glob(f"{PREFIX}[0-9][0-9]"):
        assert not list(module.glob("ex*/solution.py"))
