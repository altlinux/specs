%define _unpackaged_files_terminate_build 1
%define pypi_name capturer

# %check is disabled because the python3-module-humanfriendly is not packaged (requirements.txt)
%def_without check

Name: python3-module-%pypi_name
Version: 3.0
Release: alt1

Summary: Easily capture stdout/stderr of the current process and subprocesses
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/capturer/
Vcs: https://github.com/xolox/python-capturer

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
The capturer package makes it easy to capture the stdout and stderr streams of
the current process and subprocesses. Output can be relayed to the terminal in
real time but is also available to the Python program for additional processing.

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
%pyproject_run_pytest %pypi_name

%files
%doc README.rst LICENSE.txt CHANGELOG.rst
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/%pypi_name/
%exclude %python3_sitelibdir/%pypi_name/tests.py

%files -n %name-tests
%python3_sitelibdir/%pypi_name/tests.py

%changelog
* Thu Oct 26 2023 Vladislav Glinkin <smasher@altlinux.org> 3.0-alt1
- Initial build for ALT

