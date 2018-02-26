%define oname repoze.formapi
Name: python-module-%oname
Version: 0.5.0
Release: alt1.1
Summary: Minimalistic form library
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.formapi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze

%description
The repoze.formapi provides a form library which integrates with HTML
forms instead of abstracting them away.

It provides a small framework to take you through the entire process of
rendering a form, provide default values, validate and execute form
actions.

Form fields are defined using Python base types which map out nested
data structures with end points that are either integers, strings,
floats or tuples of these. It's up to the application to bridge these
with more complex objects.

%package tests
Summary: Tests for repoze.formapi
Group: Development/Python
Requires: %name = %version-%release

%description tests
The repoze.formapi provides a form library which integrates with HTML
forms instead of abstracting them away.

It provides a small framework to take you through the entire process of
rendering a form, provide default values, validate and execute form
actions.

Form fields are defined using Python base types which map out nested
data structures with end points that are either integers, strings,
floats or tuples of these. It's up to the application to bridge these
with more complex objects.

This package contains tests for repoze.formapi.

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
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

