%define pypi_name envparse

Name: python3-module-envparse
Version: 0.2.0
Release: alt1

Summary: Simple environment variable parsing

License: MIT
Group: Development/Python3
URL: https://github.com/rconradharris/envparse
# Source-url: https://files.pythonhosted.org/packages/2f/8d/bee8a59732c169a455627ff1557d0db180f7c352b0274480267ad3e46875/envparse-0.2.0.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
Simple environment variable parsing.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/envparse.py
%python3_sitelibdir/__pycache__/envparse.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 19 2026 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- initial build for Sisyphus.

