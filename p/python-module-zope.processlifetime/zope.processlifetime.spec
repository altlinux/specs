%define oname zope.processlifetime
Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: Zope process lifetime events
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.processlifetime/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.interface

%description
This package provides interfaces / implementations for events relative
to the lifetime of a server process (startup, database opening, etc.)

%package tests
Summary: Tests for zope.processlifetime
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides interfaces / implementations for events relative
to the lifetime of a server process (startup, database opening, etc.)

This package contains tests for zope.processlifetime.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Add necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

