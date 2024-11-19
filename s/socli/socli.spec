%define _unpackaged_files_terminate_build 1
%define pypi_name socli

%def_with check

Name:    %pypi_name
Version: 7.3
Release: alt1

Summary: Stack overflow command line interface
License: BSD-3-Clause
Group:   Other
URL:     https://pypi.org/project/%pypi_name
VCS:     https://github.com/gautamkrishnar/%pypi_name

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%add_pyproject_deps_build_filter pytest-runner
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

BuildArch: noarch

Source:  %name-%version.tar
Source1: %pyproject_deps_config_name

%description
Stack Overflow command line written in python. Using SoCLI you can
search and browse Stack Overflow without leaving the terminal.

%package -n python3-module-%pypi_name
Summary: Python3 module for Stack overflow command line interface
Group:   Development/Python3
BuildArch: noarch

%description -n python3-module-%pypi_name
Python3 module for Stack Overflow command line written in python. Using SoCLI you can
search and browse Stack Overflow without leaving the terminal.

%package -n python3-module-%pypi_name-tests
Summary: Tests for python3 module %pypi_name
Group:   Development/Python3
BuildArch: noarch

%description -n python3-module-%pypi_name-tests
Tests for python3 module %pypi_name.

%prep
%setup -n %name-%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%_man1dir
mv %buildroot/usr/man/man1/socli.1 %buildroot%_man1dir/%pypi_name.1

%check
%pyproject_run_pytest -ra -k "not test_searchStats"

%files
%_bindir/%pypi_name
%_man1dir/%pypi_name.*

%files -n python3-module-%pypi_name
%doc *.md *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%pypi_name/tests

%files -n python3-module-%pypi_name-tests
%python3_sitelibdir/%pypi_name/tests/

%changelog
* Tue Nov 19 2024 Andrey Limachko <liannnix@altlinux.org> 7.3-alt1
- initial build (thx Yuri Kozyrev)
