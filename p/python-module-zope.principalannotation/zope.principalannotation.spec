%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zope.principalannotation

%def_with python3

Name: python-module-%oname
Version: 4.1.1
#Release: alt1.1
Summary: Annotations for Zope Principals
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.principalannotation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/93/ec/738a49c913ae66a5f0ce6cd005e78646ac981bfd3fda7f1e4ae598a902b5/%{oname}-%{version}.tar.gz

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
%setup -q -n %{oname}-%{version}

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
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1.1
- (AUTO) subst_x86_64.

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

