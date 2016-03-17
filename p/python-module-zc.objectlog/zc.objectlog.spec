%define oname zc.objectlog

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt2.1
Summary: A customizable log for a single object in Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.objectlog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc zc.copy zope.app.keyreference

%description
The objectlog package provides a customizable log for a single object.
The system was designed to provide information for a visual log of
important object changes and to provide analyzable information for
metrics.

%package -n python3-module-%oname
Summary: A customizable log for a single object in Zope 3
Group: Development/Python3
%py3_requires zc zc.copy zope.app.keyreference

%description -n python3-module-%oname
The objectlog package provides a customizable log for a single object.
The system was designed to provide information for a visual log of
important object changes and to provide analyzable information for
metrics.

%package -n python3-module-%oname-tests
Summary: Tests for zc.objectlog
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The objectlog package provides a customizable log for a single object.
The system was designed to provide information for a visual log of
important object changes and to provide analyzable information for
metrics.

This package contains tests for zc.objectlog.

%package tests
Summary: Tests for zc.objectlog
Group: Development/Python
Requires: %name = %version-%release

%description tests
The objectlog package provides a customizable log for a single object.
The system was designed to provide information for a visual log of
important object changes and to provide analyzable information for
metrics.

This package contains tests for zc.objectlog.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Version 0.2.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

