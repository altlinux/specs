%define oname repoze.slicer
Name: python-module-%oname
Version: 1.0a2
Release: alt1.1
Summary: WSGI middleware to filter HTML responses
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.slicer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze wsgifilter lxml

%description
repoze.slicer is a simple piece of WSGI middleware that can extract part
of a HTML response. This can be used to reduce the amount of parsing and
manipulation of DOM trees in browsers, which is especially expensive
with older versions of IE.

%package tests
Summary: Tests for repoze.slicer
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.slicer is a simple piece of WSGI middleware that can extract part
of a HTML response. This can be used to reduce the amount of parsing and
manipulation of DOM trees in browsers, which is especially expensive
with older versions of IE.

This package contains tests for repoze.slicer.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0a2-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a2-alt1
- Initial build for Sisyphus

