%define pypi_name cowsay

%def_with check

Name:    python3-module-%pypi_name
Version: 6.1
Release: alt1

Summary: The famous cowsay for GNU/Linux is now available for python

License: GPL-3.0
Group:   Development/Python3
URL:     https://pypi.org/project/cowsay
VCS:     https://github.com/VaasuDevanS/cowsay-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
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
%pyproject_run_pytest %pypi_name/tests

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Feb 11 2025 Grigory Ustinov <grenka@altlinux.org> 6.1-alt1
- Initial build for Sisyphus.
