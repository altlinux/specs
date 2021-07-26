%define oname linecache2

Name: python3-module-%oname
Version: 1.0.0
Release: alt1.git20150306.4
Summary: Backports of the linecache module
License: Python
Group: Development/Python3
Url: https://pypi.python.org/pypi/linecache2

# https://github.com/testing-cabal/linecache2.git
Source: %name-%version.tar
BuildArch: noarch
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

BuildRequires: git-core
BuildRequires: python3-module-fixtures python3-module-setuptools python3-module-pbr python3-module-unittest2 python3-module-html5lib

%description
A backport of linecache to older supported Pythons.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A backport of linecache to older supported Pythons.

This package contains tests for %oname.

%prep
%setup
%patch1 -p1

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

%build
%python3_build

%install
%python3_install

%check
%__python3 -m unittest2 -v

%files
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1.git20150306.4
- Drop python2 support.

* Tue Jul 06 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1.git20150306.3
- Fixed FTBFS.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.git20150306.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1.git20150306.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20150306.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1.git20150306.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150306
- Initial build for Sisyphus

