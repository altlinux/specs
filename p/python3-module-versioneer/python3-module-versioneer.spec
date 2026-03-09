%define pypi_name versioneer

Name: python3-module-versioneer
Version: 0.29
Release: alt1

Summary: VCS-based management of project version strings

License: Unlicense
Group: Development/Python3
URL: https://github.com/python-versioneer/python-versioneer
# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
Versioneer is a tool for managing a recorded version number in setuptools
and pyproject.toml based Python projects. It does this by adding a special
_version.py file into your source tree, where your __init__.py can import
it. Version numbers are derived from VCS tags.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/versioneer
%python3_sitelibdir/versioneer.py
%python3_sitelibdir/__pycache__/versioneer.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Mar 09 2026 Vitaly Lipatov <lav@altlinux.ru> 0.29-alt1
- initial build for ALT Sisyphus

