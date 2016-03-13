%define oname repoze.component

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt2.git20121206.1
Summary: A Python component system
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.component
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.component.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze repoze.lru

%description
``repoze.component`` is a package that software developers can use to
provide configurability and pluggability to their applications.
``repoze.component`` provides a generalized indirection mechanism
which can be used to provide plugin points to integrators or other
developers who may wish to provide alternate implementations of
application logic or configuration values.

%package -n python3-module-%oname
Summary: A Python component system
Group: Development/Python3
%py3_requires repoze repoze.lru

%description -n python3-module-%oname
``repoze.component`` is a package that software developers can use to
provide configurability and pluggability to their applications.
``repoze.component`` provides a generalized indirection mechanism
which can be used to provide plugin points to integrators or other
developers who may wish to provide alternate implementations of
application logic or configuration values.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.component
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
``repoze.component`` is a package that software developers can use to
provide configurability and pluggability to their applications.
``repoze.component`` provides a generalized indirection mechanism
which can be used to provide plugin points to integrators or other
developers who may wish to provide alternate implementations of
application logic or configuration values.

This package contains tests for repoze.component.

%package tests
Summary: Tests for repoze.component
Group: Development/Python
Requires: %name = %version-%release

%description tests
``repoze.component`` is a package that software developers can use to
provide configurability and pluggability to their applications.
``repoze.component`` provides a generalized indirection mechanism
which can be used to provide plugin points to integrators or other
developers who may wish to provide alternate implementations of
application logic or configuration values.

This package contains tests for repoze.component.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt2.git20121206.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2.git20121206
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20121206
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1.git20110222.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20110222.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20110222
- Initial build for Sisyphus

