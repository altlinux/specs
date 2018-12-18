
%define oname pyroute2

Name: python-module-%oname
Version: 0.5.1
Release: alt1
Summary: Python Netlink library
Group: Development/Python
License: GPLv2+, ASL 2.0
Url: https://github.com/svinota/pyroute2
Source: %oname-%version.tar.gz
BuildArch: noarch


BuildRequires: python-devel
#BuildRequires: python-module-setuptools
BuildRequires: python-modules-distutils

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools

%description
Pyroute2 is a pure Python netlink library.
It requires only Python stdlib, no 3rd party libraries.
The library was started as an RTNL protocol implementation,
so the name is pyroute2, but now it supports many netlink protocols.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python Netlink library
Group: Development/Python3

%description -n python3-module-%oname
Pyroute2 is a pure Python netlink library.
It requires only Python stdlib, no 3rd party libraries.
The library was started as an RTNL protocol implementation,
so the name is pyroute2, but now it supports many netlink protocols.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for Python Netlink library
Group: Development/Documentation

%description doc
Documentation for Python Netlink library.


%prep
%setup -n %oname-%version

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
# install tests
cp -pr tests %buildroot%python_sitelibdir/%oname/

pushd ../python3
%python3_install
cp -pr tests %buildroot%python3_sitelibdir/%oname/
popd


# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

%files
%doc README.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%doc README.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc docs/html examples

%changelog
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
