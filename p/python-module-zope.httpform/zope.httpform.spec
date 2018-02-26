%define oname zope.httpform
Name: python-module-%oname
Version: 1.0.2
Release: alt2.1
Summary: HTTP Form Data Parser
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.httpform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.interface

%description
zope.httpform is a library that, given a WSGI or CGI environment
dictionary, will return a dictionary back containing converted
form/query string elements. The form and query string elements contained
in the environment are converted into simple Python types when the form
element names are decorated with special suffixes.

%package tests
Summary: Tests for HTTP Form Data Parser
Group: Development/Python
Requires: %name = %version-%release

%description tests
zope.httpform is a library that, given a WSGI or CGI environment
dictionary, will return a dictionary back containing converted
form/query string elements. The form and query string elements contained
in the environment are converted into simple Python types when the form
element names are decorated with special suffixes.

This package contains tests for HTTP Form Data Parser.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

