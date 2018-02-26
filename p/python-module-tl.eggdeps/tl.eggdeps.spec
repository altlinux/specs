%define oname tl.eggdeps
Name: python-module-%oname
Version: 0.4
Release: alt1.1
Summary: Compute a dependency graph between active Python eggs
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/tl.eggdeps/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires tl

%description
The eggdeps tool reports dependencies between eggs in the working set.
Dependencies are considered recursively, creating a directed graph. This
graph is printed to standard output either as plain text, or as an input
file to the graphviz tools.

%package tests
Summary: Tests for tl.eggdeps
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The eggdeps tool reports dependencies between eggs in the working set.
Dependencies are considered recursively, creating a directed graph. This
graph is printed to standard output either as plain text, or as an input
file to the graphviz tools.

This package contains tests for tl.eggdeps.

%package -n python-module-tl
Summary: Core files for tl
Group: Development/Python
%py_provides tl

%description -n python-module-tl
Core files for tl.

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

touch %buildroot%python_sitelibdir/tl/__init__.py

%files
%doc *.txt doc/*.txt
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/tl/__init__.*
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%files -n python-module-tl
%python_sitelibdir/tl/__init__.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

