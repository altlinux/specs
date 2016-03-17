%define oname zc.async

%def_with python3

Name: python-module-%oname
Version: 1.5.4
Release: alt3.1
Summary: Schedule durable tasks across multiple processes and machines
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.async/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

Requires: python-module-twisted-core
%py_requires ZODB3 pytz rwproperty uuid zc.queue zc.dict zc.twist
%py_requires zope.bforest zope.component zope.event rwproperty
%py_requires zope.i18nmessageid zope.interface zope.minmax zope.testing

%description
The zc.async package provides an easy-to-use Python tool that schedules
work persistently and reliably across multiple processes and machines.

%package -n python3-module-%oname
Summary: Schedule durable tasks across multiple processes and machines
Group: Development/Python3
Requires: python3-module-twisted-core
%py3_requires ZODB3 pytz rwproperty uuid zc.queue zc.dict zc.twist
%py3_requires zope.bforest zope.component zope.event rwproperty
%py3_requires zope.i18nmessageid zope.interface zope.minmax zope.testing

%description -n python3-module-%oname
The zc.async package provides an easy-to-use Python tool that schedules
work persistently and reliably across multiple processes and machines.

%package -n python3-module-%oname-tests
Summary: Tests for zc.async
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The zc.async package provides an easy-to-use Python tool that schedules
work persistently and reliably across multiple processes and machines.

This package contains tests for zc.async.

%package tests
Summary: Tests for zc.async
Group: Development/Python
Requires: %name = %version-%release

%description tests
The zc.async package provides an easy-to-use Python tool that schedules
work persistently and reliably across multiple processes and machines.

This package contains tests for zc.async.

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
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*test*
%python3_sitelibdir/*/*/*/*test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.4-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.4-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.4-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.4-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.4-alt1
- Initial build for Sisyphus

