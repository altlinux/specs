%define oname zope.publisher

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 4.2.1
Release: alt1.1
Summary: The Zope publisher publishes Python objects on the web
License: Boost Software License, Version 1.0
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.publisher/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.browser zope.component zope.configuration
%py_requires zope.contenttype zope.event zope.exceptions zope.i18n
%py_requires zope.interface zope.location zope.proxy zope.security

%description
zope.publisher allows you to publish Python objects on the web. It has
support for plain HTTP/WebDAV clients, web browsers as well as XML-RPC
and FTP clients. Input and output streams are represented by request and
response objects which allow for easy client interaction from Python.
The behaviour of the publisher is geared towards WSGI compatibility.

%package -n python3-module-%oname
Summary: The Zope publisher publishes Python objects on the web
Group: Development/Python3
%py3_requires zope.browser zope.component zope.configuration
%py3_requires zope.contenttype zope.event zope.exceptions zope.i18n
%py3_requires zope.interface zope.location zope.proxy zope.security

%description -n python3-module-%oname
zope.publisher allows you to publish Python objects on the web. It has
support for plain HTTP/WebDAV clients, web browsers as well as XML-RPC
and FTP clients. Input and output streams are represented by request and
response objects which allow for easy client interaction from Python.
The behaviour of the publisher is geared towards WSGI compatibility.

%package -n python3-module-%oname-tests
Summary: Tests for zope.publisher
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.testing

%description -n python3-module-%oname-tests
zope.publisher allows you to publish Python objects on the web. It has
support for plain HTTP/WebDAV clients, web browsers as well as XML-RPC
and FTP clients. Input and output streams are represented by request and
response objects which allow for easy client interaction from Python.
The behaviour of the publisher is geared towards WSGI compatibility.

This package contains tests for zope.publisher.

%package tests
Summary: Tests for zope.publisher
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
zope.publisher allows you to publish Python objects on the web. It has
support for plain HTTP/WebDAV clients, web browsers as well as XML-RPC
and FTP clients. Input and output streams are represented by request and
response objects which allow for easy client interaction from Python.
The behaviour of the publisher is geared towards WSGI compatibility.

This package contains tests for zope.publisher.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build
sed -i 's|qhttp|http|g' src/zope/publisher/http.py
sed -i 's|qxmlrpc|xmlrpc|g' src/zope/publisher/xmlrpc.py

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|qhttp|http|g' src/zope/publisher/http.py
sed -i 's|qxmlrpc|xmlrpc|g' src/zope/publisher/xmlrpc.py
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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.2.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.2.1-alt1
- Version 4.2.1

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.0-alt1
- Version 4.1.0

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.0-alt2
- Version 4.0.0

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.0-alt1.a4
- Version 4.0.0a4 again

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.13.4-alt2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.13.4-alt1
- Version 3.13.4

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a4
- Version 4.0.0a4

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.0-alt1
- Version 3.13.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.12.6-alt4.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt1
- Initial build for Sisyphus

