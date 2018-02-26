%define oname zope.principalannotation
Name: python-module-%oname
Version: 3.6.1
Release: alt2.1
Summary: Annotations for Zope Principals
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.principalannotation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

