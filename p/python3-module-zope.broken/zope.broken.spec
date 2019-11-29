%define oname zope.broken

Name: python3-module-%oname
Version: 3.6.0
Release: alt4

Summary: Zope Broken Object Interfaces
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.broken/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_requires zope zope.interface


%description
This package is obsolete and its functionality has been merged into the
ZODB3 distribution itself. If you use version 3.10 or later of ZODB3,
please change your imports of the IBroken interface to a direct:

  from ZODB.interfaces import IBroken

You can use this package with older versions of the ZODB3, which didn't
have the IBroken interface yet.

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


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.6.0-alt4
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 3.6.0-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.0-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

