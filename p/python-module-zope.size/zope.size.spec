%define oname zope.size

%def_with python3

Name: python-module-%oname
Version: 4.1.0
Release: alt1.1
Summary: Interfaces and simple adapter that give the size of an object
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.size/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope zope.interface zope.i18nmessageid

%description
This package provides a definition of simple interface that allows to
retrieve the size of the object for displaying and for sorting.

The default adapter is also provided. It expects objects to have the
getSize method that returns size in bytes, however, it won't crash if an
object doesn't have one and will show size as not available instead.

%package -n python3-module-%oname
Summary: Interfaces and simple adapter that give the size of an object
Group: Development/Python3
%py3_requires zope zope.interface zope.i18nmessageid

%description -n python3-module-%oname
This package provides a definition of simple interface that allows to
retrieve the size of the object for displaying and for sorting.

The default adapter is also provided. It expects objects to have the
getSize method that returns size in bytes, however, it won't crash if an
object doesn't have one and will show size as not available instead.

%package -n python3-module-%oname-tests
Summary: Tests for zope.size
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides a definition of simple interface that allows to
retrieve the size of the object for displaying and for sorting.

The default adapter is also provided. It expects objects to have the
getSize method that returns size in bytes, however, it won't crash if an
object doesn't have one and will show size as not available instead.

This package contains tests for zope.size.

%package tests
Summary: Tests for zope.size
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a definition of simple interface that allows to
retrieve the size of the object for displaying and for sorting.

The default adapter is also provided. It expects objects to have the
getSize method that returns size in bytes, however, it won't crash if an
object doesn't have one and will show size as not available instead.

This package contains tests for zope.size.

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

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Version 3.5.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1
- Initial build for Sisyphus

