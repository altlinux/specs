%define _unpackaged_files_terminate_build 1
%define pypi_name coloredlogs

%def_with check

Name: python3-module-%pypi_name
Version: 15.0.1
Release: alt1

Summary: Colored terminal output for Python's logging module
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/coloredlogs/
Vcs: https://github.com/xolox/python-coloredlogs

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
The coloredlogs package enables colored terminal output for Python's logging
module. The ColoredFormatter class inherits from logging.Formatter and uses ANSI
escape sequences to render your logging messages in color. It uses only standard
colors so it should work on any UNIX terminal.

%package -n %pypi_name
Summary: Coloredlogs demo binary file for %name
Group: Development/Python3
Requires: %name
%description -n %pypi_name
Coloredlogs demo binary file for %name

%package -n %name-tests
Summary: Test for %name
Group: Development/Python3
%if_with check
BuildRequires: /proc
BuildRequires: /dev/kvm
BuildRequires: rpm-build-vm
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
# Problems with 'test_auto_install'
vm-run '%pyproject_run_pytest %pypi_name -k "not test_auto_install"'

%files
%doc README.rst LICENSE.txt CHANGELOG.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/coloredlogs.pth
%exclude %python3_sitelibdir/%pypi_name/tests.py

%files -n %pypi_name
%_bindir/%pypi_name

%files -n %name-tests
%python3_sitelibdir/%pypi_name/tests.py

%changelog
* Fri Oct 27 2023 Vladislav Glinkin <smasher@altlinux.org> 15.0.1-alt1
- Initial build for ALT

