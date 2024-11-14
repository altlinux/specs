%define pypi_name segno

%def_with check

Name:    python3-module-%pypi_name
Version: 1.6.1
Release: alt1

Summary: Python QR Code and Micro QR Code encoder
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/heuer/segno

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-flit-core

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pypng
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k "not test_plugin"

%files
%doc *.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Nov 08 2024 Alexander Burmatov <thatman@altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus.
