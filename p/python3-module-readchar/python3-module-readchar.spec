%define pypi_name readchar

%def_with check

Name:    python3-module-%pypi_name
Version: 4.1.0
Release: alt1

Summary: Python library to read characters and key strokes
License: MIT
Group:   Development/Python3
URL:     https://github.com/magmax/python-readchar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version
rm -f readchar/_win_read.py
rm -fr tests/windows

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dev3.dist-info/

%changelog
* Fri Aug 09 2024 Alexander Burmatov <thatman@altlinux.org> 4.1.0-alt1
- Initial build for Sisyphus.
