%define pypi_name fpdf2

Name: python3-module-%pypi_name
Version: 2.8.7
Release: alt1

Summary: Simple and fast PDF generation for Python

License: LGPL-3.0-only
Group: Development/Python3
URL: https://github.com/py-pdf/fpdf2

BuildArch: noarch

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-fonttools

%description
fpdf2 is a minimalist PDF creation library for Python.
It is a fork of the FPDF library adding new features,
fixes and Python 3 support.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/fpdf/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Mar 05 2026 Vitaly Lipatov <lav@altlinux.ru> 2.8.7-alt1
- initial build

