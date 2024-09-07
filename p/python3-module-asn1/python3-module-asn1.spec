%define pypi_name asn1

%def_without check

Name:    python3-module-%pypi_name
Version: 2.7.1
Release: alt1

Summary: Python-ASN1 is a simple ASN.1 encoder and decoder for Python 2.7 and 3.5+.
License: MIT
Group:   Development/Python3
URL:     https://github.com/andrivet/python-asn1

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

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
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc AUTHORS.rst CHANGELOG.rst README.rst
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%python3_sitelibdir/__pycache__/asn1.cpython*

%changelog
* Sat Sep 07 2024 Andrey Cherepanov <cas@altlinux.org> 2.7.1-alt1
- New version.

* Tue Aug 22 2023 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- Initial build for Sisyphus (ALT #47312).
