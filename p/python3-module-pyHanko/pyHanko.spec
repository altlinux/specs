%define  modulename pyHanko

# Tests are broken, some of them need internet connection
%def_without check

Name:    python3-module-%modulename
Version: 0.20.1
Release: alt1

Summary: pyHanko: sign and stamp PDF files

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/pyHanko
VCS:     https://github.com/MatthiasValvekens/pyHanko

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-asn1crypto
BuildRequires: python3-module-pytz
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-yaml
BuildRequires: python3-module-uharfbuzz
BuildRequires: python3-module-pyHanko-certvalidator
BuildRequires: python3-module-certomancer
BuildRequires: python3-module-qrcode
BuildRequires: python3-module-fonttools
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-python-barcode
BuildRequires: python3-module-certomancer-csc-dummy
BuildRequires: python3-module-pkcs11
Buildrequires: python3-module-pytest-aiohttp
Buildrequires: python3-module-aiohttp-tests
Buildrequires: python3-module-defusedxml
Buildrequires: python3-module-pytest-asyncio
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
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3

%files
%doc LICENSE *.md
%_bindir/pyhanko
%python3_sitelibdir/pyhanko
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Mon Sep 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.20.1-alt1
- Automatically updated to 0.20.1.

* Tue Aug 01 2023 Grigory Ustinov <grenka@altlinux.org> 0.20.0-alt1
- Automatically updated to 0.20.0.

* Tue Jul 04 2023 Grigory Ustinov <grenka@altlinux.org> 0.19.0-alt1
- Automatically updated to 0.19.0.

* Sat Apr 29 2023 Grigory Ustinov <grenka@altlinux.org> 0.18.1-alt1
- Automatically updated to 0.18.1.

* Fri Apr 28 2023 Grigory Ustinov <grenka@altlinux.org> 0.18.0-alt1
- Automatically updated to 0.18.0.

* Fri Mar 10 2023 Grigory Ustinov <grenka@altlinux.org> 0.17.2-alt1
- Automatically updated to 0.17.2.

* Thu Mar 09 2023 Grigory Ustinov <grenka@altlinux.org> 0.17.1-alt1
- Automatically updated to 0.17.1.

* Tue Feb 07 2023 Grigory Ustinov <grenka@altlinux.org> 0.17.0-alt1
- Automatically updated to 0.17.0.

* Thu Dec 22 2022 Grigory Ustinov <grenka@altlinux.org> 0.16.0-alt1
- Automatically updated to 0.16.0.

* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 0.15.1-alt1
- Automatically updated to 0.15.1.

* Sun Oct 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.15.0-alt1
- Automatically updated to 0.15.0.

* Fri Sep 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.13.1-alt1
- Initial build for Sisyphus.
