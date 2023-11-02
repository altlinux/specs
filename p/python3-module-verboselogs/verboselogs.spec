%define _unpackaged_files_terminate_build 1
%define pypi_name verboselogs
%def_with check

Name: python3-module-%pypi_name
Version: 1.7
Release: alt1

Summary: Verbose logging level for Python's logging module
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/verboselogs/
Vcs: https://github.com/xolox/python-verboselogs

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
The verboselogs package extends Python's logging module to add the log levels
NOTICE, SPAM, SUCCESS and VERBOSE:

- The NOTICE level sits between the predefined WARNING and INFO levels.
- The SPAM level sits between the predefined DEBUG and NOTSET levels.
- The SUCCESS level sits between the predefined WARNING and ERROR levels.
- The VERBOSE level sits between the predefined INFO and DEBUG levels.

%package -n %name-tests
Summary: Tests for %name
Group: Development/Python3
%if_with check
%pyproject_builddeps_check
%endif
%description -n %name-tests
Tests for %name

%prep
%setup

%pyproject_deps_resync_metadata
%pyproject_deps_resync_build

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-tests.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# Disabled test_pylint_plugin because it requires an ancient version of pylint
%pyproject_run_pytest %pypi_name -k "VerboseLogsTestCase and not test_pylint_plugin"

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/%pypi_name/
%exclude %python3_sitelibdir/%pypi_name/tests.py

%files -n %name-tests
%python3_sitelibdir/%pypi_name/tests.py

%changelog
* Fri Oct 27 2023 Vladislav Glinkin <smasher@altlinux.org> 1.7-alt1
- Initial build for ALT

