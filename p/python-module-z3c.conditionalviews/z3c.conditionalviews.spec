%define oname z3c.conditionalviews

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt3.1
Summary: Intergrates with the zope publisher to validate conditional requests
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.conditionalviews/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.component zope.schema

%description
z3c.conditionalviews is a mechanism to validate a HTTP request based on
some conditional protocol like entity tags, or last modification date.
It is also extensible so that protocols like WebDAV can define there own
conditional protocol like the IF header.

%package -n python3-module-%oname
Summary: Intergrates with the zope publisher to validate conditional requests
Group: Development/Python3
%py3_requires zope.component zope.schema

%description -n python3-module-%oname
z3c.conditionalviews is a mechanism to validate a HTTP request based on
some conditional protocol like entity tags, or last modification date.
It is also extensible so that protocols like WebDAV can define there own
conditional protocol like the IF header.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.conditionalviews
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.zcmlfiles zope.securitypolicy

%description -n python3-module-%oname-tests
z3c.conditionalviews is a mechanism to validate a HTTP request based on
some conditional protocol like entity tags, or last modification date.
It is also extensible so that protocols like WebDAV can define there own
conditional protocol like the IF header.

This package contains tests for z3c.conditionalviews.

%package tests
Summary: Tests for z3c.conditionalviews
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.securitypolicy

%description tests
z3c.conditionalviews is a mechanism to validate a HTTP request based on
some conditional protocol like entity tags, or last modification date.
It is also extensible so that protocols like WebDAV can define there own
conditional protocol like the IF header.

This package contains tests for z3c.conditionalviews.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

