# Copyright 2021 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
# or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.
"""kedro-171-package
"""

import os
from pathlib import Path

from kedro.runner import SequentialRunner

from kedro.framework.session import KedroSession
from kedro.framework.session.session import _activate_session
from kedro.framework.project import configure_project

__version__ = "0.1"


def get_session():
    "Get kedro session"
    cur_path = os.getcwd()
    os.chdir(Path(__file__).parents[2])
    configure_project("kedro_171_package")
    session = KedroSession.create(Path(__file__).resolve().parent.name)
    _activate_session(session, force=True)
    os.chdir(cur_path)

    return session


class Kedro171:
    def __init__(self):
        self.session = get_session()
        self.context = self.session.load_context()
        self.catalog = self.context.catalog
        self.pipeline = self.context.pipeline
        self.pipelines = self.context.pipelines
        self.runner = SequentialRunner()

    def run(self, pipeline=None, catalog=None):
        if pipeline is None:
            pipeline = self.pipeline
        if catalog is None:
            catalog = self.catalog
        self.runner.run(pipeline, catalog)
