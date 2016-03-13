%define oname zc.monitorcache

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt3.1
Summary: zc.monitor plugin to modify cache sizes
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.monitorcache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zc zc.monitor zc.z3monitor

%description
zc.monitorcache is a zc.z3monitor plugin that allows one to modify or
check the cache size (in objects or bytes) of a running instance.

%package -n python3-module-%oname
Summary: zc.monitor plugin to modify cache sizes
Group: Development/Python3
%py3_requires zc zc.monitor zc.z3monitor

%description -n python3-module-%oname
zc.monitorcache is a zc.z3monitor plugin that allows one to modify or
check the cache size (in objects or bytes) of a running instance.

%package -n python3-module-%oname-tests
Summary: Tests for zc.monitorcache
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
zc.monitorcache is a zc.z3monitor plugin that allows one to modify or
check the cache size (in objects or bytes) of a running instance.

This package contains tests for zc.monitorcache.

%package tests
Summary: Tests for zc.monitorcache
Group: Development/Python
Requires: %name = %version-%release

%description tests
zc.monitorcache is a zc.z3monitor plugin that allows one to modify or
check the cache size (in objects or bytes) of a running instance.

This package contains tests for zc.monitorcache.

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
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

