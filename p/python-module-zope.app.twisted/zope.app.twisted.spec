%define oname zope.app.twisted

%def_with python3

Name: python-module-%oname
Version: 3.5.0
Release: alt3
Summary: Twisted Integration for Zope 3 Applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.twisted/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

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

%package -n python3-module-%oname
Summary: Twisted Integration for Zope 3 Applications
Group: Development/Python3
%py3_requires zope.app ZConfig zdaemon zope.copypastemove zope.event
%py3_requires zope.exceptions zope.interface zope.publisher zope.security
%py3_requires zope.app.applicationcontrol zope.app.appsetup
%py3_requires zope.app.publication zope.app.wsgi zope.app.server
Requires: python3-module-twisted-conch
Requires: python3-module-twisted-core python3-module-twisted-lore
Requires: python3-module-twisted-mail python3-module-twisted-names
Requires: python3-module-twisted-news python3-module-twisted-runner
Requires: python3-module-twisted-web
Requires: python3-module-twisted-words

%description -n python3-module-%oname
This package integrates the Twisted HTTP and FTP server into a Zope 3
application setup. It also defines the script skeleton for a classic
Zope 3 application.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.twisted
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.testbrowser

%description -n python3-module-%oname-tests
This package integrates the Twisted HTTP and FTP server into a Zope 3
application setup. It also defines the script skeleton for a classic
Zope 3 application.

This package contains tests for zope.app.twisted.

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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|rfc822|rfc822py3|g' \
	src/zope/app/twisted/tests/test_inputbuffering.py
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
%python_sitelibdir/zope*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/zope/*/*/tests
%exclude %python_sitelibdir/zope/*/*/*/tests

%files tests
%python_sitelibdir/zope/*/*/tests
%python_sitelibdir/zope/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/zope*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/*/*/tests
%exclude %python3_sitelibdir/zope/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/zope/*/*/tests
%python3_sitelibdir/zope/*/*/*/tests
%endif

%changelog
* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

