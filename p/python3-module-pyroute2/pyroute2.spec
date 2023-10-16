%define oname pyroute2

%def_with check

Name: python3-module-%oname
Version: 0.7.9
Release: alt1

Summary: Python Netlink library

Group: Development/Python3
License: GPLv2+ and Apache-2.0
Url: https://github.com/svinota/pyroute2

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-modules-sqlite3
%endif

%add_python3_req_skip pyroute2.bsd.rtmsocket
%add_python3_req_skip dhclient
%add_python3_req_skip netl
%add_python3_req_skip mitogen.core mitogen.master

%description
Pyroute2 is a pure Python3 netlink library.
It requires only Python stdlib, no 3rd party libraries.
The library was started as an RTNL protocol implementation,
so the name is pyroute2, but now it supports many netlink protocols.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -- tests/test_minimal/*.py tests/test_unit/*.py

%files
%doc *.rst
%_bindir/%oname-cli
%_bindir/%oname-dhcp-client
%_bindir/%oname-test-platform
%_bindir/ss2
%python3_sitelibdir/%oname
%python3_sitelibdir/pr2modules
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Oct 16 2023 Grigory Ustinov <grenka@altlinux.org> 0.7.9-alt1
- Automatically updated to 0.7.9.

* Fri Apr 28 2023 Anton Vyatkin <toni@altlinux.org> 0.7.7-alt1
- NMU: New version 0.7.7.

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.5.19-alt2.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 0.5.19-alt2
- NMU: make mitogen requirement optional, as in README

* Sat May 15 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.19-alt1
- Automatically updated to 0.5.19.

* Wed Apr 21 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.18-alt1
- Automatically updated to 0.5.18.

* Tue Sep 15 2020 Grigory Ustinov <grenka@altlinux.org> 0.5.14-alt1
- Automatically updated to 0.5.14.

* Fri Sep 04 2020 Grigory Ustinov <grenka@altlinux.org> 0.5.13-alt1
- Automatically updated to 0.5.13.

* Thu May 28 2020 Grigory Ustinov <grenka@altlinux.org> 0.5.12-alt1
- Build new version 0.5.12.

* Wed Dec 11 2019 Grigory Ustinov <grenka@altlinux.org> 0.5.7-alt1
- Build new version 0.5.7.

* Thu Aug 29 2019 Grigory Ustinov <grenka@altlinux.org> 0.5.6-alt1
- Build new version only for python3.

* Mon Apr 22 2019 Alexey Shabalin <shaba@altlinux.org> 0.5.2-alt1
- 0.5.2

* Tue Dec 18 2018 Alexey Shabalin <shaba@altlinux.org> 0.5.1-alt1
- 0.5.1

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.15-alt1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * backup-file-in-package for python-module-pyroute2-doc

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.15-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 06 2017 Alexey Shabalin <shaba@altlinux.ru> 0.4.15-alt1
- Initial package.
