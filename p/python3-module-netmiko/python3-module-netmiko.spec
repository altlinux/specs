%define pypi_name netmiko

%def_without check

Name:    python3-module-%pypi_name
Version: 4.5.0
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
%_bindir/%pypi_name-bulk-encrypt
%_bindir/%pypi_name-encrypt
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Dec 25 2024 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt1
- Automatically updated to 4.5.0.

* Tue Jan 09 2024 Alexander Burmatov <thatman@altlinux.org> 4.3.0-alt1
- New 4.3.0 version.

* Mon Nov 13 2023 Alexander Burmatov <thatman@altlinux.org> 4.2.0-alt1
- Initial build for Sisyphus.
