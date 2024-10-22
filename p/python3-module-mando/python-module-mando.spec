%define  oname mando

%def_with check

Name:    python3-module-%oname
Version: 0.8.2
Release: alt1

Summary: Python wrapper around argparse, a tool to create CLI apps

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/mando

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
Mando is a wrapper around argparse, and allows writing CLI
applications.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Oct 22 2024 Grigory Ustinov <grenka@altlinux.org> 0.8.2-alt1
- Build new version.
- Build with check.

* Thu Jul 28 2022 Grigory Ustinov <grenka@altlinux.org> 0.7.1-alt1
- Build new version.

* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt1
- Build new version.
- Drop python2 support.

* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus
