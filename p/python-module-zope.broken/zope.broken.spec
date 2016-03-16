%define oname zope.broken

%def_with python3

Name: python-module-%oname
Version: 3.6.0
Release: alt3.1
Summary: Zope Broken Object Interfaces
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.broken/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope zope.interface

%description
This package is obsolete and its functionality has been merged into the
ZODB3 distribution itself. If you use version 3.10 or later of ZODB3,
please change your imports of the IBroken interface to a direct:

  from ZODB.interfaces import IBroken

You can use this package with older versions of the ZODB3, which didn't
have the IBroken interface yet.

%package -n python3-module-%oname
Summary: Zope Broken Object Interfaces
Group: Development/Python3
%py3_requires zope zope.interface

%description -n python3-module-%oname
This package is obsolete and its functionality has been merged into the
ZODB3 distribution itself. If you use version 3.10 or later of ZODB3,
please change your imports of the IBroken interface to a direct:

  from ZODB.interfaces import IBroken

You can use this package with older versions of the ZODB3, which didn't
have the IBroken interface yet.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
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

