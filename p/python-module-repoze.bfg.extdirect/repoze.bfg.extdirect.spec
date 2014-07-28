%define oname repoze.bfg.extdirect

%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt2
Summary: ExtDirect Implementation for repoze
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.extdirect/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.bfg venusian

%description
This repoze.bfg plugin provides a router for the ExtDirect Sencha API
included in ExtJS 3.x. ExtDirect allows to run server-side callbacks
directly through JavaScript without the extra AJAX boilerplate.

%package -n python3-module-%oname
Summary: ExtDirect Implementation for repoze
Group: Development/Python3
%py3_requires repoze.bfg venusian

%description -n python3-module-%oname
This repoze.bfg plugin provides a router for the ExtDirect Sencha API
included in ExtJS 3.x. ExtDirect allows to run server-side callbacks
directly through JavaScript without the extra AJAX boilerplate.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.bfg.extdirect
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This repoze.bfg plugin provides a router for the ExtDirect Sencha API
included in ExtJS 3.x. ExtDirect allows to run server-side callbacks
directly through JavaScript without the extra AJAX boilerplate.

This package contains tests for repoze.bfg.extdirect.

%package tests
Summary: Tests for repoze.bfg.extdirect
Group: Development/Python
Requires: %name = %version-%release

%description tests
This repoze.bfg plugin provides a router for the ExtDirect Sencha API
included in ExtJS 3.x. ExtDirect allows to run server-side callbacks
directly through JavaScript without the extra AJAX boilerplate.

This package contains tests for repoze.bfg.extdirect.

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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.3-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus

