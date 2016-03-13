%define oname repoze.formapi

%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt2.1
Summary: Minimalistic form library
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.formapi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

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

%package -n python3-module-%oname
Summary: Minimalistic form library
Group: Development/Python3
%py3_requires repoze

%description -n python3-module-%oname
The repoze.formapi provides a form library which integrates with HTML
forms instead of abstracting them away.

It provides a small framework to take you through the entire process of
rendering a form, provide default values, validate and execute form
actions.

Form fields are defined using Python base types which map out nested
data structures with end points that are either integers, strings,
floats or tuples of these. It's up to the application to bridge these
with more complex objects.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.formapi
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
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
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Version 0.6.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

