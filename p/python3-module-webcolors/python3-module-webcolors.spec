%define  modulename webcolors

%def_with check

Name:    python3-module-%modulename
Version: 24.8.0
Release: alt1

Summary: Library for working with HTML/CSS color formats in Python

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/webcolors
VCS:     https://github.com/ubernostrum/webcolors

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
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Wed Aug 14 2024 Grigory Ustinov <grenka@altlinux.org> 24.8.0-alt1
- Automatically updated to 24.8.0.

* Tue Jun 25 2024 Grigory Ustinov <grenka@altlinux.org> 24.6.0-alt1
- Automatically updated to 24.6.0.
- Built with check.

* Mon Mar 27 2023 Grigory Ustinov <grenka@altlinux.org> 1.13-alt1
- Automatically updated to 1.13.

* Thu May 26 2022 Grigory Ustinov <grenka@altlinux.org> 1.12-alt1
- Automatically updated to 1.12.

* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 1.11.1-alt1
- Automatically updated to 1.11.1.

* Thu Jan 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.10-alt2
- Porting on Python3.

* Tue Sep 24 2019 Grigory Ustinov <grenka@altlinux.org> 1.10-alt1
- Initial build for Sisyphus.
