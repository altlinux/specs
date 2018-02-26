%define oname zc.zservertracelog
Name: python-module-%oname
Version: 1.3.0
Release: alt2.1
Summary: Zope 3 tracelog implementation for zserver
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.zservertracelog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.appsetup zope.app.server zope.app.wsgi zope.server

%description
This package implements a Zope2-style (extended) tracelog. A tracelog is
a kind of access log that records several low-level events for each
request. Each log entry starts with a record type, a request identifier
and the time. Some log records have additional data.

%package tests
Summary: Tests for Zope 3 tracelog implementation for zserver
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package implements a Zope2-style (extended) tracelog. A tracelog is
a kind of access log that records several low-level events for each
request. Each log entry starts with a record type, a request identifier
and the time. Some log records have additional data.

This package contains tests for Zope 3 tracelog implementation for
zserver.

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
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

