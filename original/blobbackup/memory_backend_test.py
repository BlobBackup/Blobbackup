from unittest import TestCase, main
from blobbackup.memory_backend import MemoryBackend


class MemoryBackendTest(TestCase):
    def setUp(self):
        self.backend = MemoryBackend()

    def test_check_connection(self):
        self.assertTrue(self.backend.check_connection())

    def test_makedirs(self):
        self.backend.makedirs("test")
        self.assertFalse(self.backend.exists("test"))

    def test_round_trip(self):
        self.assertFalse(self.backend.exists("dir/test1"))
        self.assertFalse(self.backend.exists("dir/test2"))

        self.backend.write("dir/test1", b"test1")
        self.backend.write("dir/test2", b"test2")

        self.assertTrue(self.backend.exists("dir/test1"))
        self.assertTrue(self.backend.exists("dir/test2"))
        self.assertTrue(self.backend.ls("dir"), ["dir/test1", "dir/test2"])

        self.assertEqual(self.backend.read("dir/test1"), b"test1")
        self.assertEqual(self.backend.read("dir/test2"), b"test2")

        self.backend.rm("dir/test1")
        self.backend.rm("dir/test2")

        self.assertFalse(self.backend.exists('dir/test1'))
        self.assertFalse(self.backend.exists("dir/test2"))
        self.assertEqual(self.backend.ls("dir"), [])


if __name__ == "__main__":
    main()