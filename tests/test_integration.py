# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from subprocess import Popen, PIPE,STDOUT
import os
import sys
import unittest

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class IntegrationTests(unittest.TestCase):
    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_scheduler(self):
        demo_file = os.path.join(project_dir, 'scheduler.py')
        p = Popen([sys.executable, demo_file], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        p.stdin.write(b'10\n')
        p.stdin.write(b'10\n')
        output = p.communicate()[0]
        output = str(output).upper()
        if os.getenv('DEBUG_OUTPUT'):
            print("Example output \n"+ output)

        with self.subTest(msg="Verify if output contains 'Schedule score:"):
            self.assertIn("Schedule score:".upper(), output)
        with self.subTest(msg="Verify if output contains Average happiness:"):
            self.assertIn("Average happiness:".upper(), output)
        with self.subTest(msg="Verify if error string contains in output"):
            self.assertNotIn("ERROR", output)
        with self.subTest(msg="Verify if warning string contains in output"):
            self.assertNotIn("WARNING", output)

    def test_demo(self):
        demo_file = os.path.join(project_dir, 'demo.py')
        p = Popen([sys.executable, demo_file], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        p.stdin.write(b'10\n')
        p.stdin.write(b'10\n')
        output = p.communicate()[0]
        output = str(output).upper()
        if os.getenv('DEBUG_OUTPUT'):
            print("Example output \n"+ output)

        with self.subTest(msg="Verify if output contains 'Schedule score:"):
            self.assertIn("Schedule score:".upper(), output)
        with self.subTest(msg="Verify if output contains Average happiness:"):
            self.assertIn("Average happiness:".upper(), output)
        with self.subTest(msg="Verify if error string contains in output"):
            self.assertNotIn("ERROR", output)
        with self.subTest(msg="Verify if warning string contains in output"):
            self.assertNotIn("WARNING", output)

if __name__ == '__main__':
    unittest.main()
