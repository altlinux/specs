%define _unpackaged_files_terminate_build 1
%define pypi_name deal
%define module_name %pypi_name
%def_with check

Name: python3-module-%pypi_name
Version: 4.24.6
Release: alt2

Summary: Design by contract for Python. Write bug-free code. Add a few decorators, get static analysis and tests for free
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/deal/
Vcs: https://github.com/life4/deal
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-%release.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-module-docstring-parser-tests
# Filter outdated and possibly unmaintained packages
%add_pyproject_deps_check_filter deal-solver$
%add_pyproject_deps_check_filter vaa$
# We have too new typeguard that isn't suitable for the tests
%add_pyproject_deps_check_filter typeguard$
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_metadata_extra integration
%endif

%description
A Python library for design by contract (DbC) and checking values,
exceptions, and side-effects. In a nutshell, deal empowers you to write
bug-free code. By adding a few decorators to your code, you get for free
tests, static analysis, formal verification, and much more. Read intro
to get started.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# Overriding coverage addopts that is in the pyproject.toml.
echo > pytest.ini
## test_common.py:test_infer:
# Switch off the test that was broken after Python had updated to 3.13.
## Others:
# The following tests are deselected since they require DNS resolution
# which isn't provided in the hasher.
%pyproject_run_pytest -Wignore \
	--deselect="tests/test_linter/test_extractors/test_common.py::test_infer[from pathlib import Path\nPath.write_text-expected1]" \
	--deselect="tests/test_imports.py::test_smoke_has" \
	--deselect="tests/test_runtime/test_offline.py::test_raises_exception" \
	--deselect="tests/test_runtime/test_offline.py::test_raises_specified_exception" \
	--deselect="tests/test_runtime/test_offline.py::test_allow_network" \
	--deselect="tests/test_runtime/test_offline.py::test_decorating_async_function" \
	--deselect="tests/test_runtime/test_offline.py::test_decorating_generator" \
	--deselect="tests/test_runtime/test_pure.py::test_pure_offline" \
	--deselect="tests/test_runtime/test_raises.py::test_raises_doesnt_override_another_contract" \
	--deselect="tests/test_runtime/test_raises.py::test_raises_doesnt_override_another_contract_async" \
	--deselect="tests/test_runtime/test_raises.py::test_raises_generator"

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jun 10 2026 Alexandr Shashkin <dutyrok@altlinux.org> 4.24.6-alt2
- Fixed FTBFS:
  + Handled pytest.param Call nodes alongside Tuple in test extractor.
  + Skipped None docstring values from docstring_parser test cases.
  + Added BuildRequires on python3-module-docstring-parser-tests.

* Mon Dec 01 2025 Alexandr Shashkin <dutyrok@altlinux.org> 4.24.6-alt1
- Updated to 4.24.6.

* Tue Jul 01 2025 Alexandr Shashkin <dutyrok@altlinux.org> 4.24.5-alt1
- Initial build for ALT Sisyphus.

