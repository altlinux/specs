%define oname grokcore.content

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt3
Summary: Base content types for Grok
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.content/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires grokcore ZODB3 grokcore.component zope.annotation
%py_requires zope.container zope.interface

%description
This package provides base classes of basic content types.

%package -n python3-module-%oname
Summary: Base content types for Grok
Group: Development/Python3
%py3_requires grokcore ZODB3 grokcore.component zope.annotation
%py3_requires zope.container zope.interface

%description -n python3-module-%oname
This package provides base classes of basic content types.

%package -n python3-module-%oname-tests
Summary: Tests for grokcore.content
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.component

%description -n python3-module-%oname-tests
This package provides base classes of basic content types.

This package contains tests for grokcore.content.

%package tests
Summary: Tests for grokcore.content
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.component

%description tests
This package provides base classes of basic content types.

This package contains tests for grokcore.content.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

