%define oname zope.traversing

%def_with python3

Name: python-module-%oname
Version: 4.0.0
Release: alt2
Summary: Resolving paths in the object hierarchy
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.traversing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

Requires: python-module-zope.i18nmessageid
%py_requires zope.component zope.i18n zope.interface zope.proxy
%py_requires zope.publisher zope.security zope.location 

%description
The zope.traversing package provides adapteres for resolving object
paths by traversing an object hierarchy. This also includes support for
traversal namespaces (e.g. ++view++, ++skin++, etc.) as well as
computing URLs via the @@absolute_url view.

%package -n python3-module-%oname
Summary: Resolving paths in the object hierarchy
Group: Development/Python3
Requires: python3-module-zope.i18nmessageid
%py3_requires zope.component zope.i18n zope.interface zope.proxy
%py3_requires zope.publisher zope.security zope.location 

%description -n python3-module-%oname
The zope.traversing package provides adapteres for resolving object
paths by traversing an object hierarchy. This also includes support for
traversal namespaces (e.g. ++view++, ++skin++, etc.) as well as
computing URLs via the @@absolute_url view.

%package -n python3-module-%oname-tests
Summary: Tests for zope.traversing
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.browserpage zope.browserresource zope.configuration
%py3_requires zope.container zope.pagetemplate zope.site zope.tal
%py3_requires zope.testing ZODB3

%description -n python3-module-%oname-tests
The zope.traversing package provides adapteres for resolving object
paths by traversing an object hierarchy. This also includes support for
traversal namespaces (e.g. ++view++, ++skin++, etc.) as well as
computing URLs via the @@absolute_url view.

This package contains tests for zope.traversing.

%package tests
Summary: Tests for zope.traversing
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.browserpage zope.browserresource zope.configuration
%py_requires zope.container zope.pagetemplate zope.site zope.tal
%py_requires zope.testing ZODB3

%description tests
The zope.traversing package provides adapteres for resolving object
paths by traversing an object hierarchy. This also includes support for
traversal namespaces (e.g. ++view++, ++skin++, etc.) as well as
computing URLs via the @@absolute_url view.

This package contains tests for zope.traversing.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Version 4.0.0
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a3
- Version 4.0.0a3

* Thu Dec 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14.0-alt1
- Version 3.14.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.13.2-alt4.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.2-alt4
- Added necessary requirements for tests

* Mon Jun 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.2-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.2-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.2-alt1
- Initial build for Sisyphus

