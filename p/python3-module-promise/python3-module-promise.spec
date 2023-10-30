%define pypi_name promise

%def_with check

Name:    python3-module-%pypi_name
Version: 2.3.0
Release: alt1

Summary: Ultra-performant Promise implementation in Python
License: MIT
Group:   Development/Python3
URL:     https://github.com/syrusakbary/promise

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-benchmark
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar
Patch0: python311-compatibility.patch
Patch1: fix-compatibility-in-tests.patch

%description
This is a implementation of Promises in Python. It is a super set
of Promises/A+ designed to have readable, performant code and
to provide just the extensions that are absolutely necessary
for using promises in Python.

%prep
%setup -n %pypi_name-%version
%patch0 -p1
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-2.3.dist-info/

%changelog
* Thu Oct 05 2023 Alexander Burmatov <thatman@altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus.
