%define oname zope.thread

%def_with python3

Name: python-module-%oname
Version: 3.4
Release: alt3
Summary: Zope3 Thread-Local Storage
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.thread/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%py_requires zope

%description
This package is deprecated and exists soley for backward compatability.

%if_with python3
%package -n python3-module-%oname
Summary: Zope3 Thread-Local Storage (Python 3)
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
This package is deprecated and exists soley for backward compatability.

%package -n python3-module-%oname-tests
Summary: Tests for Zope3 Thread-Local Storage (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package is deprecated and exists soley for backward compatability.

This package contains tests for Zope3 Thread-Local Storage.
%endif

%package tests
Summary: Tests for Zope3 Thread-Local Storage
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package is deprecated and exists soley for backward compatability.

This package contains tests for Zope3 Thread-Local Storage.

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

#files -n python3-module-%oname-tests
#python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1
- Initial build for Sisyphus

