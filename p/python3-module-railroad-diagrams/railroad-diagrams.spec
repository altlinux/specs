%define _unpackaged_files_terminate_build 1
%define pypi_name railroad-diagrams
%define mod_name railroad

Name: python3-module-%pypi_name
Version: 3.0.1
Release: alt1.1
Summary: A small library for generating railroad diagrams using SVG
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/railroad-diagrams
Vcs: https://github.com/tabatkins/railroad-diagrams
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%description
This is a small library for generating railroad diagrams (like what
JSON.org uses) using SVG, with both JS and Python ports.

Railroad diagrams are a way of visually representing a grammar in a form
that is more readable than using regular expressions or BNF. They can
easily represent any context-free grammar, and some more powerful
grammars. There are several railroad-diagram generators out there, but
none of them had the visual appeal I wanted, so I wrote my own.

See also https://github.com/tabatkins/railroad-diagrams for JS version

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md README-py.md
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1.1
- Demodernized packaging.

* Tue Sep 24 2024 Stanislav Levin <slev@altlinux.org> 3.0.1-alt1
- 1.1.1 -> 3.0.1.

* Wed Feb 02 2022 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Initial build for ALT
