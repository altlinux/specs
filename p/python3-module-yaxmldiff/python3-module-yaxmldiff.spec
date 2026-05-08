%define pypi_name yaxmldiff
%def_enable check

Name: python3-module-%pypi_name
Version: 0.2.0
Release: alt1

Summary: Yet Another XML Diff Library
Group: Development/Python3
License: Apache-2.0
Url: https://pypi.org/project/yaxmldiff

Vcs: https://github.com/latk/yaxmldiff.py.git
Source: https://pypi.io/packages/source/y/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 
BuildRequires: python3(wheel) python3(hatchling) python3(hatch-fancy-pypi-readme)
%{?_enable_check:BuildRequires: python3(pytest) python3(pylint)
BuildRequires: python3(mypy) python3(lxml)}

%description
This library checks if two XML documents seem semantically equivalent.
If not, it produces something similar to a unified diff.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir_noarch/*
%doc README* CHANGELOG*

%changelog
* Fri May 08 2026 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus

