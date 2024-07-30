%define pypi_name picologging

%def_with check

Name:    python3-module-%pypi_name
Version: 0.9.3
Release: alt1

Summary: An optimized logging library for Python
License: MIT
Group:   Development/Python3
URL:     https://github.com/microsoft/picologging

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-scikit-build
BuildRequires: python3-module-flaky

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-hypothesis
%endif

Source: %pypi_name-%version.tar

%description
Picologging is a high-performance logging library for Python. picologging is
4-17x faster than the logging module in the standard library.
Picologging is designed to be used as a drop-in replacement for applications
which already use logging, and supports the same API as the logging module.

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
%python3_sitelibdir/%pypi_name-0.9.2.dist-info

%changelog
* Thu Jul 18 2024 Alexander Burmatov <thatman@altlinux.org> 0.9.3-alt1
- Initial build for Sisyphus.
