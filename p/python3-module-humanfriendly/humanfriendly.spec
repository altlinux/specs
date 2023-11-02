%define _unpackaged_files_terminate_build 1
%define pypi_name humanfriendly

# check is disabled because python3-module-capturer and python3-module-coloredlogs
# require python3-module-humanfriendly (runtime dependency)
%def_without check

Name: python3-module-humanfriendly
Version: 10.0
Release: alt1

Summary: Human friendly input/output in Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/humanfriendly/
Vcs: https://github.com/xolox/python-humanfriendly

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
The functions and classes in the humanfriendly package can be used to make text
interfaces more user friendly. Some example features:

- Parsing and formatting numbers, file sizes, pathnames and timespans in
simple, human friendly formats.
- Easy to use timers for long running operations, with human friendly formatting
  of the resulting timespans.
- Prompting the user to select a choice from a list of options by typing the
  option's number or a unique substring of the option.
- Terminal interaction including text styling (ANSI escape sequences), user
  friendly rendering of usage messages and querying the terminal for its size.

%package -n %pypi_name
Summary: Humanfriendly demo binary file for %name
Group: Development/Python3
Requires: %name
%description -n %pypi_name
Humanfriendly demo binary file for %name

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

%files -n %pypi_name
%_bindir/%pypi_name

%files -n %name-tests
%python3_sitelibdir/%pypi_name/tests.py

%changelog
* Fri Oct 27 2023 Vladislav Glinkin <smasher@altlinux.org> 10.0-alt1
- Initial build for ALT

