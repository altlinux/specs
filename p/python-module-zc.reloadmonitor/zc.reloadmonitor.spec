%define oname zc.reloadmonitor

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt3.1
Summary: Allows you to cause already imported modules to be reloaded
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.reloadmonitor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc zope.component zc.monitor zope.configuration

%description
zc.reloadmonitor provides a plug-in for zc.monitor. It allows you to
cause already imported modules to be reloaded.

%package -n python3-module-%oname
Summary: Allows you to cause already imported modules to be reloaded
Group: Development/Python3
%py3_requires zc zope.component zc.monitor zope.configuration

%description -n python3-module-%oname
zc.reloadmonitor provides a plug-in for zc.monitor. It allows you to
cause already imported modules to be reloaded.

%package -n python3-module-%oname-tests
Summary: Tests for zc.reloadmonitor
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zc.ngi

%description -n python3-module-%oname-tests
zc.reloadmonitor provides a plug-in for zc.monitor. It allows you to
cause already imported modules to be reloaded.

This package contains tests for zc.reloadmonitor.

%package tests
Summary: Tests for zc.reloadmonitor
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zc.ngi

%description tests
zc.reloadmonitor provides a plug-in for zc.monitor. It allows you to
cause already imported modules to be reloaded.

This package contains tests for zc.reloadmonitor.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

