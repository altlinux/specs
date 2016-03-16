%define oname zope.principalannotation

%def_with python3

Name: python-module-%oname
Version: 4.1.0
Release: alt1.1
Summary: Annotations for Zope Principals
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.principalannotation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope ZODB3 zope.annotation zope.component zope.interface
%py_requires zope.location zope.security zope.site

%description
This package implements annotations for zope.security principals. To
make it clear, the principal here is the object that provides
zope.security.interfaces.IPrincipal interface and annotations is the
object providing zope.annotation.interfaces.IAnnotations.

The problem is that principals is dynamic, non-persistent objects
created on the fly for every security participation (request or
something), so common annotation techniques, like AttributeAnnotations
cannot be applied to them.

This package provides a persistent storage of principal annotations,
storing annotations by principal ID as well as an adapter from
IPrincipal to IAnnotations.

%package -n python3-module-%oname
Summary: Annotations for Zope Principals
Group: Development/Python3
%py3_requires zope ZODB3 zope.annotation zope.component zope.interface
%py3_requires zope.location zope.security zope.site

%description -n python3-module-%oname
This package implements annotations for zope.security principals. To
make it clear, the principal here is the object that provides
zope.security.interfaces.IPrincipal interface and annotations is the
object providing zope.annotation.interfaces.IAnnotations.

The problem is that principals is dynamic, non-persistent objects
created on the fly for every security participation (request or
something), so common annotation techniques, like AttributeAnnotations
cannot be applied to them.

This package provides a persistent storage of principal annotations,
storing annotations by principal ID as well as an adapter from
IPrincipal to IAnnotations.

%package -n python3-module-%oname-tests
Summary: Tests for zope.principalannotation
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.site

%description -n python3-module-%oname-tests
This package implements annotations for zope.security principals. To
make it clear, the principal here is the object that provides
zope.security.interfaces.IPrincipal interface and annotations is the
object providing zope.annotation.interfaces.IAnnotations.

The problem is that principals is dynamic, non-persistent objects
created on the fly for every security participation (request or
something), so common annotation techniques, like AttributeAnnotations
cannot be applied to them.

This package provides a persistent storage of principal annotations,
storing annotations by principal ID as well as an adapter from
IPrincipal to IAnnotations.

This package contains tests for zope.principalannotation.

%package tests
Summary: Tests for zope.principalannotation
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.site

%description tests
This package implements annotations for zope.security principals. To
make it clear, the principal here is the object that provides
zope.security.interfaces.IPrincipal interface and annotations is the
object providing zope.annotation.interfaces.IAnnotations.

The problem is that principals is dynamic, non-persistent objects
created on the fly for every security participation (request or
something), so common annotation techniques, like AttributeAnnotations
cannot be applied to them.

This package provides a persistent storage of principal annotations,
storing annotations by principal ID as well as an adapter from
IPrincipal to IAnnotations.

This package contains tests for zope.principalannotation.

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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a2
- Version 4.0.0a2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

