"""
Enables quick loading of the kedro session, context, catalog from within
ipython.


## Example

%run -m kedro_171_package


catalog.list()


"""
import os
from pathlib import Path

from kedro.runner import SequentialRunner

from kedro.framework.session import KedroSession
from kedro.framework.session.session import _activate_session
from kedro.framework.project import configure_project


def get_session():
    "Get kedro session"
    cur_path = os.getcwd()
    os.chdir(Path(__file__).parents[2])
    configure_project("kedro_171_package")
    session = KedroSession.create(Path(__file__).resolve().parent.name)
    _activate_session(session, force=True)
    os.chdir(cur_path)

    return session


if __name__ == "__main__":
    session = get_session()
    context = session.load_context()
    catalog = context.catalog
    pipeline = context.pipeline
    pipelines = context.pipelines
    runner = SequentialRunner()
