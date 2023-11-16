%define pypi_name textfsm

%def_with check

Name:    python3-module-%pypi_name
Version: 1.1.3
Release: alt1

Summary: Python module for parsing semi-structured text into python tables
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/google/textfsm

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-six

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Python module which implements a template based state machine for parsing
semi-formatted text. Originally developed to allow programmatic access to
information returned from the command line interface (CLI)
of networking devices.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install
rm -fr %buildroot%python3_sitelibdir/testdata

%check
%pyproject_run_pytest

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-1.1.2.dist-info/

%changelog
* Mon Nov 13 2023 Alexander Burmatov <thatman@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus.
