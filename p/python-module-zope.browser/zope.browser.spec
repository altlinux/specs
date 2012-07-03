%define oname zope.browser

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt3
Summary: Shared Zope Toolkit browser components
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.browser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%py_requires zope zope.interface

%description
This package provides shared browser components for the Zope Toolkit.

%if_with python3
%package -n python3-module-%oname
Summary: Shared Zope Toolkit browser components (Python 3)
Group: Development/Python3
%py3_requires zope zope.interface

%description -n python3-module-%oname
This package provides shared browser components for the Zope Toolkit.

%package -n python3-module-%oname-tests
Summary: Tests for zope.browser (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides shared browser components for the Zope Toolkit.

This package contains tests for zope.browser.
%endif

%package tests
Summary: Tests for zope.browser
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides shared browser components for the Zope Toolkit.

This package contains tests for zope.browser.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt3
- Added module for Python 3

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

