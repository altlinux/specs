%define _unpackaged_files_terminate_build 1

%define oname repoze.vhm

Name: python3-module-%oname
Version: 0.14
Release: alt2

Summary: Commit / abort transactions via WSGI middleware
License: BSD
Group: Development/Python3
Url: https://github.com/repoze/repoze.vhm

# https://github.com/repoze/repoze.vhm.git
Source0: https://pypi.python.org/packages/76/df/0175302b40198e77ad213562ce41f1d8a8ddcd537296c44ef2fa352bc9d8/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires repoze


%description
This package provides middleware and utilities for doing virtual
hosting within a WSGI/Repoze environment.  It is particularly useful
within a ``repoze.zope2`` environment, where it may be used as an
alternative to the classic `VirtualHostMonster` method of doing
virtual hosting.

%package tests
Summary: Tests for repoze.vhm
Group: Development/Python3
Requires: %name = %version-%release

%description tests
This package provides middleware and utilities for doing virtual
hosting within a WSGI/Repoze environment.  It is particularly useful
within a ``repoze.zope2`` environment, where it may be used as an
alternative to the classic `VirtualHostMonster` method of doing
virtual hosting.

This package contains tests for repoze.vhm.

%prep
%setup -q -n %{oname}-%{version}

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.14-alt2
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13-alt2.git20120324.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13-alt2.git20120324.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt2.git20120324
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20120324
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13-alt1.git20110322.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20110322.1
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20110322
- Initial build for Sisyphus

