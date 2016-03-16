%define oname tl.eggdeps

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt2.1
Summary: Compute a dependency graph between active Python eggs
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/tl.eggdeps/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires tl

%description
The eggdeps tool reports dependencies between eggs in the working set.
Dependencies are considered recursively, creating a directed graph. This
graph is printed to standard output either as plain text, or as an input
file to the graphviz tools.

%package -n python3-module-%oname
Summary: Compute a dependency graph between active Python eggs
Group: Development/Python3
%py3_requires tl

%description -n python3-module-%oname
The eggdeps tool reports dependencies between eggs in the working set.
Dependencies are considered recursively, creating a directed graph. This
graph is printed to standard output either as plain text, or as an input
file to the graphviz tools.

%package -n python3-module-%oname-tests
Summary: Tests for tl.eggdeps
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
The eggdeps tool reports dependencies between eggs in the working set.
Dependencies are considered recursively, creating a directed graph. This
graph is printed to standard output either as plain text, or as an input
file to the graphviz tools.

This package contains tests for tl.eggdeps.

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

%package -n python3-module-tl
Summary: Core files for tl
Group: Development/Python3
%py3_provides tl

%description -n python3-module-tl
Core files for tl.

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
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/tl/__init__.py
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

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
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/tl/__init__.*
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%files -n python-module-tl
%python_sitelibdir/tl/__init__.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt doc/*.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/tl/__init__.*
%exclude %python3_sitelibdir/tl/__pycache__/__init__.*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-tl
%python3_sitelibdir/tl/__init__.*
%python3_sitelibdir/tl/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

