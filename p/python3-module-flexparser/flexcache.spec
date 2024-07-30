%define pypi_name flexparser

%def_with check

Name:    python3-module-%pypi_name
Version: 0.3.1
Release: alt1

Summary: Parsing made fun ... using typing

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/flexparser
VCS:     https://github.com/hgrecco/flexparser

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
The idea is quite simple. You write a class for every type of content (called
here ParsedStatement) you need to parse. Each class should have a from_string
constructor. We used extensively the typing module to make the output structure
easy to use and less error prone.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Tue Jul 30 2024 Grigory Ustinov <grenka@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus.
