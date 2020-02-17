%define oname zope.weakset

Name: python3-module-%oname
Version: 3.6.0
Release: alt4

Summary: Zope Object Database: object database and persistence
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.weakset/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_requires zope


%description
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a plugable storage
interface, rich transaction support, and undo.

This distribution includes the weakset module from ZODB.

%package tests
Summary: Tests for zope.weakset
Group: Development/Python3
Requires: %name = %version-%release
%add_python3_req_skip __init__

%description tests
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a plugable storage
interface, rich transaction support, and undo.

This distribution includes the weakset module from ZODB.

This package contains tests for zope.weakset.

%prep
%setup

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
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Mon Feb 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.6.0-alt4
- Build for python2 disabled.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 3.6.0-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.0-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

