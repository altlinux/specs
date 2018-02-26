%define oname repoze.monty
Name: python-module-%oname
Version: 0.1
Release: alt2.1
Summary: A form field marshaller for WSGI (stolen from Zope)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.monty/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze

%description
repoze.monty is a library that, given a WSGI environment dictionary (and
a wsgi.input file pointer if the request is a POST request), will return
a dictionary back containing "converted" form/query string elements. The
form and query string elements contained in the request are converted
into simple Python types when the form element names are decorated with
special suffixes.

%package tests
Summary: Tests for repoze.monty
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.monty is a library that, given a WSGI environment dictionary (and
a wsgi.input file pointer if the request is a POST request), will return
a dictionary back containing "converted" form/query string elements. The
form and query string elements contained in the request are converted
into simple Python types when the form element names are decorated with
special suffixes.

This package contains tests for repoze.monty.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

