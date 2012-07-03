%define oname z3c.vcsync
Name: python-module-%oname
Version: 0.17
Release: alt2.1
Summary: Synchronize object data with a version control system
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.vcsync/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires grokcore.component zope.app.container py

%description
This package contains code that helps with handling synchronization of
persistent content with a version control system.

This can be useful in software that needs to be able to work offline.
The web application runs on a user's laptop that may be away from an
internet connection. When connected again, the user syncs with a version
control server, receiving updates that may have been made by others, and
committing their own changes.

Another advantage is that the version control system always contains a
history of how content developed over time. The version-control based
content can also be used for other purposes independent of the
application.

%package tests
Summary: Tests for z3c.vcsync
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package contains code that helps with handling synchronization of
persistent content with a version control system.

This can be useful in software that needs to be able to work offline.
The web application runs on a user's laptop that may be away from an
internet connection. When connected again, the user syncs with a version
control server, receiving updates that may have been made by others, and
committing their own changes.

Another advantage is that the version control system always contains a
history of how content developed over time. The version-control based
content can also be used for other purposes independent of the
application.

This package contains tests for z3c.vcsync.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.17-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1
- Initial build for Sisyphus

