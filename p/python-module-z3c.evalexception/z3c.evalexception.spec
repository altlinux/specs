%define oname z3c.evalexception

%def_with python3

Name: python-module-%oname
Version: 2.0
Release: alt3.1
Summary: Debugging middlewares for zope.publisher-based web applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.evalexception/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires paste zope.security

%description
z3c.evalexception provides two WSGI middlewares for debugging web
applications running on the zope.publisher object publishing framework
(e.g. Zope 3). Both middlewares will intercept an exception thrown by
the application and provide means for debugging.

%package -n python3-module-%oname
Summary: Debugging middlewares for zope.publisher-based web applications
Group: Development/Python3
%py3_requires paste zope.security

%description -n python3-module-%oname
z3c.evalexception provides two WSGI middlewares for debugging web
applications running on the zope.publisher object publishing framework
(e.g. Zope 3). Both middlewares will intercept an exception thrown by
the application and provide means for debugging.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Initial build for Sisyphus

