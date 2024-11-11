%define pypi_name spur

%def_with check

Name:    python3-module-%pypi_name
Version: 0.3.23
Release: alt1

Summary: Run commands and manipulate files locally or over SSH using the same interface

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/spur
VCS:     https://github.com/mwilliamson/spur.py

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-paramiko
BuildRequires: /dev/pts
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# No ssh server in hasher
%pyproject_run_pytest --ignore=tests/ssh_tests.py

%files
%doc LICENSE CHANGES *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 11 2024 Grigory Ustinov <grenka@altlinux.org> 0.3.23-alt1
- Initial build for Sisyphus.
