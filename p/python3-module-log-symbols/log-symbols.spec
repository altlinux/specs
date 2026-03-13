%define   modulename log-symbols
%define   pypi_name log_symbols
%def_with check

Name:     python3-module-%modulename
Version:  0.0.14
Release:  alt1

Summary:  Colored symbols for various log levels for Python

License:  MIT
Group:    Development/Python3
URL:      https://pypi.org/project/log-symbols
VCS:      https://github.com/manrajgrover/py-log-symbols

BuildArch: noarch

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-colorama
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Fri Mar 13 2026 Grigory Ustinov <grenka@altlinux.org> 0.0.14-alt1
- Initial build for Sisyphus.
