import datetime as dt
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('update', Path(__file__).resolve().parents[1] / 'scripts/update.py')
update = importlib.util.module_from_spec(spec)
spec.loader.exec_module(update)


class UpdateTests(unittest.TestCase):
    def test_seven_day_delta_rejects_older_baseline(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / '2026-09-01.json').write_text('{}')
            with patch.object(update, 'HISTORY', root):
                self.assertIsNone(update.load_old_snapshot(dt.date(2026, 9, 10)))
                (root / '2026-09-03.json').write_text('{"repositories": []}')
                self.assertEqual(update.load_old_snapshot(dt.date(2026, 9, 10)), {'repositories': []})

    def test_failed_refresh_preserves_previous_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            previous = '{"repositories": [{"full_name": "a/b", "stars": 20}]}'
            (root / 'latest.json').write_text(previous)
            (root / 'repos.json').write_text('{"repositories": [{"full_name": "a/b", "category": "test"}]}')
            with patch.object(update, 'DATA', root), patch.object(update, 'normalize_self_links'), patch.object(update, 'fetch_repo', side_effect=OSError('offline')), patch.object(update.time, 'sleep'):
                self.assertEqual(update.main(), 1)
            self.assertEqual((root / 'latest.json').read_text(), previous)

    def test_stale_baseline_is_not_a_measured_delta(self):
        repos = [{'full_name': 'a/b', 'stars': 40, 'delta_7d': None}]
        update.add_deltas(repos, {'repositories': [{'full_name': 'a/b', 'stars': 20, 'stale': True}]})
        self.assertIsNone(repos[0]['delta_7d'])

    def test_readme_replacement_preserves_backslashes(self):
        self.assertIn(r'paper \1', update.replace_block('<!-- PAPERS_START --><!-- PAPERS_END -->', 'PAPERS', r'paper \1'))


if __name__ == '__main__':
    unittest.main()
