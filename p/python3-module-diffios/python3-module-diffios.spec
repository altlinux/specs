%define pypi_name diffios

%def_with check

Name:    python3-module-%pypi_name
Version: 0.0.9
Release: alt1

Summary: Cisco IOS diff tool
License: MIT
Group:   Development/Python3
URL:     https://github.com/robphoenix/diffios

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
diffios is a Python library that provides a way to compare Cisco IOS
configurations against a baseline template, and generate an output detailing
the differences between them.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Nov 10 2023 Alexander Burmatov <thatman@altlinux.org> 0.0.9-alt1
- Initial build for Sisyphus.
