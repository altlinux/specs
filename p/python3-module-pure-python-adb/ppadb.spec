Name: python3-module-pure-python-adb
Version: 1.0.0
Release: alt1

Summary: Anoter ADB shell implemented in Python
License: MIT
Group: Development/Python
URL: https://pypi.org/project/pure-python-adb
VCS: https://github.com/spm5065/pure-python-adb

Provides: python3-module-ppadb = %EVR
Obsoletes: python3-module-ppadb

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
# Upstream lists dev tools and the test-only Exscript library in
# requirements.txt; the package itself only needs aiofiles.
%add_pyproject_deps_runtime_filter exscript black pytest ruff
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_build_filter exscript
%add_pyproject_deps_check_filter exscript
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
# Upstream ships an invalid PEP440 fallback_version (">0.3.0"), which
# setuptools-scm parses eagerly even when the version is overridden via
# SETUPTOOLS_SCM_PRETEND_VERSION; strip the bogus leading '>'.
sed -i 's/^fallback_version=">0.3.0"/fallback_version="0.3.0"/' pyproject.toml

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile requirements.txt
%pyproject_build

%install
%pyproject_install

%check
# The tests in test/ are integration tests: they need a live Android
# emulator and the unpackaged Exscript library (see test/conftest.py).
# Only the offline unit tests in test_async (mocked streams) can run here.
# test_create_connection dials a real adb server at 127.0.0.1:5037, and
# test_push_dir relies on os.walk mocking that Python 3.14's
# pathlib.Path.walk now honors, yielding unrelated fake paths.
%pyproject_run_pytest -k 'not test_create_connection and not test_push_dir' \
    test_async

%files
%python3_sitelibdir/ppadb
# upstream project name is pure-python-adb-reborn
%python3_sitelibdir/pure_python_adb_reborn-%version.dist-info

%changelog
* Thu Oct 23 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.0-alt1
- 1.0.0 released

* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.6-alt1
- initial
