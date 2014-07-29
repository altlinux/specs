%define oname repoze.bfg.xmlrpc

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt3
Summary: XML-RPC support for repoze.bfg
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.xmlrpc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.bfg

%description
XML-RPC support for repoze.bfg.

%package -n python3-module-%oname
Summary: XML-RPC support for repoze.bfg
Group: Development/Python3
%py3_requires repoze.bfg

%description -n python3-module-%oname
XML-RPC support for repoze.bfg.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.bfg.xmlrpc
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires repoze.bfg.testing

%description -n python3-module-%oname-tests
XML-RPC support for repoze.bfg.

This package contains tests for repoze.bfg.xmlrpc.

%package tests
Summary: Tests for repoze.bfg.xmlrpc
Group: Development/Python
Requires: %name = %version-%release
%py_requires repoze.bfg.testing

%description tests
XML-RPC support for repoze.bfg.

This package contains tests for repoze.bfg.xmlrpc.

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
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

