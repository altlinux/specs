%define _unpackaged_files_terminate_build 1
%define pypi_name pyuca
%define mod_name pyuca

%def_with check

Name: python3-module-%pypi_name
Version: 1.2
Release: alt1

Summary: A Python implementation of the Unicode Collation Algorithm
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/pyuca/
VCS: https://github.com/jtauber/pyuca
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
This is a Python implementation of the Unicode Collation Algorithm (UCA).
It passes all of the UCA conformance tests for Unicode 5.2.0 (Python 2.7),
Unicode 6.3.0 (Python 3.3+), Unicode 8.0.0 (Python 3.5+),
Unicode 9.0.0 (Python 3.6+), and Unicode 10.0.0 (Python 3.7+) with a
variable-weighting setting of Non-ignorable.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# --doctest-modules to collect more than 0 tests
%pyproject_run_pytest -vra --doctest-modules

%files
%doc README.md LICENSE AUTHORS
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Mar 03 2026 Aleksandr Dovydenkov <asd@altlinux.org> 1.2-alt1
- Initial build for Sisyphus.