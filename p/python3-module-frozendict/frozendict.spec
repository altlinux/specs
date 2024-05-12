%define modulename frozendict

%def_with check

Name: python3-module-frozendict
Version: 2.4.4
Release: alt1

Summary: An immutable dictionary

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/frozendict
VCS: https://github.com/Marco-Sulla/python-frozendict

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
frozendict is an immutable wrapper around dictionaries that implements
the complete mapping interface. It can be used as a drop-in replacement
for dictionaries where immutability is desired.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE.txt README.md
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Sun May 12 2024 Grigory Ustinov <grenka@altlinux.org> 2.4.4-alt1
- Automatically updated to 2.4.4.

* Tue Apr 16 2024 Grigory Ustinov <grenka@altlinux.org> 2.4.2-alt1
- Automatically updated to 2.4.2.

* Mon Apr 01 2024 Grigory Ustinov <grenka@altlinux.org> 2.4.1-alt1
- Automatically updated to 2.4.1.

* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 2.4.0-alt1
- Automatically updated to 2.4.0.
- Build with check.

* Wed Dec 27 2023 Grigory Ustinov <grenka@altlinux.org> 2.3.10-alt1
- Automatically updated to 2.3.10.

* Wed May 03 2023 Grigory Ustinov <grenka@altlinux.org> 2.3.8-alt2
- Fixed build with python3.11.

* Wed May 03 2023 Grigory Ustinov <grenka@altlinux.org> 2.3.8-alt1
- Automatically updated to 2.3.8.

* Tue Apr 25 2023 Grigory Ustinov <grenka@altlinux.org> 2.3.7-alt1
- Automatically updated to 2.3.7.
- Build without check for python3.11.

* Thu Mar 23 2023 Grigory Ustinov <grenka@altlinux.org> 2.3.6-alt1
- Automatically updated to 2.3.6.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 2.3.5-alt1
- Automatically updated to 2.3.5.

* Mon Jul 25 2022 Grigory Ustinov <grenka@altlinux.org> 2.3.4-alt1
- Automatically updated to 2.3.4.

* Mon Jun 27 2022 Grigory Ustinov <grenka@altlinux.org> 2.3.2-alt1
- Automatically updated to 2.3.2.
- Build with check.

* Thu Mar 10 2022 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- new version 2.3.0 (with rpmrb script)
- frozendict is arch dependent package now

* Thu Jul 22 2021 Grigory Ustinov <grenka@altlinux.org> 1.2-alt2
- Drop python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.qa1
- NMU: applied repocop patch

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- initial build for ALT Sisyphus

