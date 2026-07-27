%define pypi_name astdoc

%def_with check

Name:    python3-module-%pypi_name
Version: 1.3.2
Release: alt1

Summary: A lightweight Python library for parsing and analyzing abstract syntax trees (AST) and extracting docstring information
License: MIT
Group:   Development/Python3
URL:     https://github.com/daizutabi/astdoc

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-uv-build

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-jinja2
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
A lightweight Python library for parsing and analyzing abstract syntax trees
(AST) and extracting docstring information. Designed to facilitate the
documentation process, astdoc provides tools for developers to easily access,
manipulate, and generate documentation from Python code.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jul 24 2026 Alexander Burmatov <thatman@altlinux.org> 1.3.2-alt1
- Initial build for Sisyphus.
