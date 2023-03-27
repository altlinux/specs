%define  modulename webcolors

Name:    python3-module-%modulename
Version: 1.13
Release: alt1

Summary: Library for working with HTML/CSS color formats in Python

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/ubernostrum/webcolors

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

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

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info
%doc *.rst

%changelog
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
