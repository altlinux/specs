%define modulename frozendict

%def_with check

Name: python3-module-frozendict
Version: 2.3.6
Release: alt1

Summary: An immutable dictionary

Url: https://pypi.org/project/frozendict
License: MIT
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# https://github.com/Marco-Sulla/python-frozendict
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

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
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v

%files
%doc README.md
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version-py%_python3_version.egg-info

%changelog
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

