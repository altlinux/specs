%define oname traceback2

%def_disable check
%def_without bootstrap

Name: python3-module-%oname
Version: 1.4.0
Release: alt3

Summary: Backports of the traceback module
License: Python
Group: Development/Python3
Url: https://pypi.python.org/pypi/traceback2
# https://github.com/testing-cabal/traceback2.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: git-core

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-contextlib2 python3-module-html5lib
BuildPreReq: python3-module-mimeparse python3-module-pbr
BuildPreReq: python3-module-pytest

%if_with bootstrap
BuildPreReq: python3-module-unittest2
%endif

%py3_provides %oname
%py3_requires linecache2 six

%description
A backport of traceback to older supported Pythons.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A backport of traceback to older supported Pythons.

This package contains tests for %oname.

%prep
%setup

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
%__python3 setup.py test -v
rm -fR build
py.test-%_python3_version -vv

%files
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt3
- Drop python2 support.
- Disable bootstrap.

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.4.0-alt2.1
- rebuild with all requires

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.4.0-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.0-alt1.git20150309.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1.git20150309.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.git20150309
- Initial build for Sisyphus

