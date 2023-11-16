%define pypi_name netmiko

%def_without check

Name:    python3-module-%pypi_name
Version: 4.2.0
Release: alt1

Summary: Multi-vendor library to simplify Paramiko SSH connections to network devices
License: MIT
Group:   Development/Python3
URL:     https://github.com/ktbyers/netmiko

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-poetry

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version
sed -i 's|from typing.re import Pattern|from typing import Pattern|' \
    $(find . -name 'snmp_autodetect.py')

%build
%pyproject_build

%install
%pyproject_install

%check
# See https://github.com/ktbyers/netmiko/blob/develop/TESTING.md

%files
%doc *.md
%_bindir/%pypi_name-cfg
%_bindir/%pypi_name-grep
%_bindir/%pypi_name-show
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 13 2023 Alexander Burmatov <thatman@altlinux.org> 4.2.0-alt1
- Initial build for Sisyphus.
