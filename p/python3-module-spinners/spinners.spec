%define   modulename spinners
%def_with check

Name:     python3-module-%modulename
Version:  0.0.24
Release:  alt1

Summary:  More than 60 spinners for terminal, python wrapper for amazing node library cli-spinners

License:  MIT
Group:    Development/Python3
URL:      https://pypi.org/project/spinners
VCS:      https://github.com/manrajgrover/py-spinners

BuildArch: noarch

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
%summary

%prep
%setup

sed -i 's/assertEquals/assertEqual/' tests/test_spinners.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Fri Mar 13 2026 Grigory Ustinov <grenka@altlinux.org> 0.0.24-alt1
- Initial build for Sisyphus.
