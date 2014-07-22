%define oname grokcore.traverser

%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt2
Summary: Traverser for the Grok Framework
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.traverser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires grokcore grokcore.component grokcore.security
%py_requires grokcore.view grokcore.rest martian zope.component
%py_requires zope.interface zope.publisher

%description
Traverser for the Grok Framework.

%package -n python3-module-%oname
Summary: Traverser for the Grok Framework
Group: Development/Python3
%py3_requires grokcore grokcore.component grokcore.security
%py3_requires grokcore.view grokcore.rest martian zope.component
%py3_requires zope.interface zope.publisher

%description -n python3-module-%oname
Traverser for the Grok Framework.

%package -n python3-module-%oname-tests
Summary: Tests for grokcore.traverser
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires grokcore.view grokcore.content zope.app.wsgi
%py3_requires zope.app.appsetup zope.testing

%description -n python3-module-%oname-tests
Traverser for the Grok Framework.

This package contains tests for grokcore.traverser.

%package tests
Summary: Tests for grokcore.traverser
Group: Development/Python
Requires: %name = %version-%release
%py_requires grokcore.view grokcore.content zope.app.wsgi
%py_requires zope.app.appsetup zope.testing

%description tests
Traverser for the Grok Framework.

This package contains tests for grokcore.traverser.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*test*
%python3_sitelibdir/*/*/*/*test*
%endif

%changelog
* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added module for Python 3

* Fri Feb 22 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Version 1.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

