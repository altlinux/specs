%define oname repoze.formapi

Name: python3-module-%oname
Version: 0.6.1
Release: alt3

Summary: Minimalistic form library
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/repoze.formapi/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires repoze


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
Group: Development/Python3
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

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%files
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt3
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.1-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt2.1.1
- (AUTO) subst_x86_64.

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

