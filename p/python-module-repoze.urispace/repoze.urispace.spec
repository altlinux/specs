%define oname repoze.urispace
Name: python-module-%oname
Version: 0.3.2
Release: alt2.1
Summary: Library / middleware for URI-based assertions
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.urispace/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze paste zope.interface elementtree

%description
repoze.urispace implements the URISpace 1.0 spec, as proposed to the W3C
by Akamai. Its aim is to provide an implementation of that language as a
vehicle for asserting declarative metadata about a resource based on
pattern matching against its URI.

Once asserted, such metadata can be used to guide the application in
serving the resource, with possible applciations including:

* Setting cache control headers.
* Selecting externally applied themes, e.g. in Deliverance.
* Restricting access, e.g. to emulate Zope's "placeful security."

%package tests
Summary: Tests for repoze.urispace
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.urispace implements the URISpace 1.0 spec, as proposed to the W3C
by Akamai. Its aim is to provide an implementation of that language as a
vehicle for asserting declarative metadata about a resource based on
pattern matching against its URI.

This package contains tests for repoze.urispace.

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
%doc *.txt docs/*.rst docs/examples
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus

