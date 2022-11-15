%define oname pyroute2

Name: python3-module-%oname
Version: 0.5.19
Release: alt2.1

Summary: Python Netlink library

Group: Development/Python3
License: GPLv2+, ASL 2.0
Url: https://github.com/svinota/pyroute2

Source: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%add_python3_req_skip pyroute2.bsd.rtmsocket
%add_python3_req_skip dhclient
%add_python3_req_skip netl
%add_python3_req_skip mitogen.core mitogen.master

%description
Pyroute2 is a pure Python3 netlink library.
It requires only Python stdlib, no 3rd party libraries.
The library was started as an RTNL protocol implementation,
so the name is pyroute2, but now it supports many netlink protocols.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/tests/pytest/pr2test
%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/tests/utils.py

%description tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

%build
%python3_build

# git describe is useless inside hasher, so make version file manually
echo '__version__ = "%version"' > pyroute2/config/version.py

%install
%python3_install
# install tests
cp -pr tests %buildroot%python3_sitelibdir/%oname/

# It is the file in the package whose name matches the format emacs or vim uses
# for backup and autosave files. It may have been installed by  accident.
find %buildroot \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

%files
%doc README.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
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
