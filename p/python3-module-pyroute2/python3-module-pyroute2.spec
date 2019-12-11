%define oname pyroute2

Name: python3-module-%oname
Version: 0.5.7
Release: alt1

Summary: Python Netlink library

Group: Development/Python3
License: GPLv2+, ASL 2.0
Url: https://github.com/svinota/pyroute2

Source: %oname-%version.tar
Patch: pyroute2_install_parser_module.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

%add_python3_req_skip pyroute2.bsd.rtmsocket
%add_python3_req_skip dhclient
%add_python3_req_skip netl

%description
Pyroute2 is a pure Python3 netlink library.
It requires only Python stdlib, no 3rd party libraries.
The library was started as an RTNL protocol implementation,
so the name is pyroute2, but now it supports many netlink protocols.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version
%patch -p1

%build
%python3_build

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
%doc README.md
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
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
