%define oname grokcore.component

%def_with python3

Name: python-module-%oname
Version: 2.5
Release: alt2
Summary: Grok-like configuration for basic components (adapters, utilities, subscribers)
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.component/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires martian zope.component zope.configuration zope.interface
%py_requires zope.testing

%description
This package provides base classes of basic component types for the Zope
Component Architecture, as well as means for configuring and registering
them directly in Python (without ZCML).

%package -n python3-module-%oname
Summary: Grok-like configuration for basic components (adapters, utilities, subscribers)
Group: Development/Python3
%py3_requires martian zope.component zope.configuration zope.interface
%py3_requires zope.testing

%description -n python3-module-%oname
This package provides base classes of basic component types for the Zope
Component Architecture, as well as means for configuring and registering
them directly in Python (without ZCML).

%package -n python3-module-%oname-tests
Summary: Tests for grokcore.component
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides base classes of basic component types for the Zope
Component Architecture, as well as means for configuring and registering
them directly in Python (without ZCML).

This package contains tests for grokcore.component.

%package tests
Summary: Tests for grokcore.component
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides base classes of basic component types for the Zope
Component Architecture, as well as means for configuring and registering
them directly in Python (without ZCML).

This package contains tests for grokcore.component.

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
* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt2
- Added module for Python 3

* Fri Feb 22 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1
- Version 2.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt2
- Added necessary requirements
- Excludes *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1
- Initial build for Sisyphus

