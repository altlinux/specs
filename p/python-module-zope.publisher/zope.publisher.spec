%define oname zope.publisher
Name: python-module-%oname
Version: 3.13.0
Release: alt1
Summary: The Zope publisher publishes Python objects on the web
License: Boost Software License, Version 1.0
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.publisher/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.browser zope.component zope.configuration
%py_requires zope.contenttype zope.event zope.exceptions zope.i18n
%py_requires zope.interface zope.location zope.proxy zope.security

%description
zope.publisher allows you to publish Python objects on the web. It has
support for plain HTTP/WebDAV clients, web browsers as well as XML-RPC
and FTP clients. Input and output streams are represented by request and
response objects which allow for easy client interaction from Python.
The behaviour of the publisher is geared towards WSGI compatibility.

%package tests
Summary: Tests for zope.publisher
Group: Development/Python
Requires: %name = %version-%release
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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
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

