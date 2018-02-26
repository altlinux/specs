%define oname zope.app.twisted
Name: python-module-%oname
Version: 3.5.0
Release: alt2.1
Summary: Twisted Integration for Zope 3 Applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.twisted/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app ZConfig zdaemon zope.copypastemove zope.event
%py_requires zope.exceptions zope.interface zope.publisher zope.security
%py_requires zope.app.applicationcontrol zope.app.appsetup
%py_requires zope.app.publication zope.app.wsgi zope.app.server
Requires: python-module-twisted python-module-twisted-conch
Requires: python-module-twisted-core python-module-twisted-lore
Requires: python-module-twisted-mail python-module-twisted-names
Requires: python-module-twisted-news python-module-twisted-runner
Requires: python-module-twisted-web python-module-twisted-web2
Requires: python-module-twisted-words

%description
This package integrates the Twisted HTTP and FTP server into a Zope 3
application setup. It also defines the script skeleton for a classic
Zope 3 application.

%package tests
Summary: Tests for zope.app.twisted
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testbrowser

%description tests
This package integrates the Twisted HTTP and FTP server into a Zope 3
application setup. It also defines the script skeleton for a classic
Zope 3 application.

This package contains tests for zope.app.twisted.

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
%python_sitelibdir/zope*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/zope/*/*/tests
%exclude %python_sitelibdir/zope/*/*/*/tests

%files tests
%python_sitelibdir/zope/*/*/tests
%python_sitelibdir/zope/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

