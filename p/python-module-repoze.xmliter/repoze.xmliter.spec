%define oname repoze.xmliter

%def_with python3

Name: python-module-%oname
Version: 0.6
Release: alt1.git20140921.1
Summary: Wrapper for lxml trees which serializes to string upon iteration
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.xmliter
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.xmliter.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze lxml

%description
This package provides a wrapper for ``lxml`` trees which serializes to
string on iteration, but otherwise makes the tree available in an
attribute.

The primary for this is WSGI middleware which may avoid
needless XML parsing and serialization.

%package -n python3-module-%oname
Summary: Wrapper for lxml trees which serializes to string upon iteration
Group: Development/Python3
%py3_requires repoze lxml

%description -n python3-module-%oname
This package provides a wrapper for ``lxml`` trees which serializes to
string on iteration, but otherwise makes the tree available in an
attribute.

The primary for this is WSGI middleware which may avoid
needless XML parsing and serialization.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.xmliter
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides a wrapper for ``lxml`` trees which serializes to
string on iteration, but otherwise makes the tree available in an
attribute.

The primary for this is WSGI middleware which may avoid
needless XML parsing and serialization.

This package contains tests for repoze.xmliter.

%package tests
Summary: Tests for repoze.xmliter
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a wrapper for ``lxml`` trees which serializes to
string on iteration, but otherwise makes the tree available in an
attribute.

The primary for this is WSGI middleware which may avoid
needless XML parsing and serialization.

This package contains tests for repoze.xmliter.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt1.git20140921.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.git20140921
- Version 0.6

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2.git20120125
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20120125
- Version 0.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.git20110603.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110603.1
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110603
- Initial build for Sisyphus

