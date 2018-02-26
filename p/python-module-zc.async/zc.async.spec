%define oname zc.async
Name: python-module-%oname
Version: 1.5.4
Release: alt2.1
Summary: Schedule durable tasks across multiple processes and machines
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.async/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

Requires: python-module-twisted-core
%py_requires ZODB3 pytz rwproperty uuid zc.queue zc.dict zc.twist
%py_requires zope.bforest zope.component zope.event rwproperty
%py_requires zope.i18nmessageid zope.interface zope.minmax zope.testing

%description
The zc.async package provides an easy-to-use Python tool that schedules
work persistently and reliably across multiple processes and machines.

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.4-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.4-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.4-alt1
- Initial build for Sisyphus

