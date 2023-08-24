%define pypi_name chess

%def_with check

Name:    python3-module-%pypi_name
Version: 1.10.0
Release: alt1

Summary: A chess library for Python
License: GPL-3.0
Group:   Development/Python3
URL:     https://github.com/niklasf/python-chess

Packager: Leonid Znamenok <respublica@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: stockfish

Requires: stockfish

BuildArch: noarch

Source: %name-%version.tar

%description
A chess library for Python, with move generation and validation,
PGN parsing and writing, Polyglot opening book reading, Gaviota
tablebase probing, Syzygy tablebase probing, and UCI/XBoard engine communication

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc CHANGELOG.rst README.rst LICENSE.txt
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Aug 07 2023 Leonid Znamenok <respublica@altlinux.org> 1.10.0-alt1
- New version 1.10.0.

* Thu Apr 06 2023 Leonid Znamenok <respublica@altlinux.org> 1.9.4-alt1
- Initial build for Sisyphus
