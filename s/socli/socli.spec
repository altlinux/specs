%define _unpackaged_files_terminate_build 1
%define pypi_name socli

%def_with check

Name:    %pypi_name
Version: 7.3
Release: alt1.1

Summary: Stack overflow command line interface
License: BSD-3-Clause
Group:   Other
URL:     https://pypi.org/project/%pypi_name
VCS:     https://github.com/gautamkrishnar/%pypi_name

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-argcomplete
BuildRequires: python3-module-beautifulsoup4
BuildRequires: python3-module-colorama
BuildRequires: python3-module-py-stackexchange
BuildRequires: python3-module-requests
BuildRequires: python3-module-sentry-sdk
BuildRequires: python3-module-urwid
%endif

BuildArch: noarch

Source:  %name-%version.tar

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
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 7.3-alt1.1
- Demodernized packaging.

* Tue Nov 19 2024 Andrey Limachko <liannnix@altlinux.org> 7.3-alt1
- initial build (thx Yuri Kozyrev)
