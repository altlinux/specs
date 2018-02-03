%define oname azoth

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt3.git20141205.1
Summary: Sqlalchemy utilities
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/azoth/

# https://github.com/TakesxiSximada/azoth.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose
BuildRequires: python-module-coverage
BuildRequires: python-module-virtualenv
BuildRequires: python-module-tox
BuildRequires: python-module-flake8 python-modules-sqlite3
BuildRequires: python-module-zope.sqlalchemy
BuildRequires: python-module-pbr python-module-unittest2 python-module-zc.recipe.egg
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-tox
BuildRequires: python3-module-nose
BuildRequires: python3-module-coverage
BuildRequires: python3-modules-sqlite3 python3-module-flake8
BuildRequires: python3-module-zope.sqlalchemy
BuildRequires: python3-module-html5lib python3-module-pbr python3-module-unittest2 python3-module-zc.recipe.egg python3-module-zope.component
%endif

%py_provides %oname
%py_requires zope.interface zope.sqlalchemy

%description
azoth is sqlalchemy helper library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
azoth is sqlalchemy helper library.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Sqlalchemy utilities
Group: Development/Python3
%py3_provides %oname
%py3_requires zope.interface zope.sqlalchemy

%description -n python3-module-%oname
azoth is sqlalchemy helper library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
azoth is sqlalchemy helper library.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

sed -i 's|\(nonlocal \)||' azoth/decorators.py

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
rm -fR build
py.test
%if_with python3
pushd ../python3
rm -fR build
py.test3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/testutils.*

%files tests
%python_sitelibdir/*/testutils.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%exclude %python3_sitelibdir/*/testutils.*
%exclude %python3_sitelibdir/*/*/testutils.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/testutils.*
%python3_sitelibdir/*/*/testutils.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt3.git20141205.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt3.git20141205
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt2.git20141205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt2.git20141205.1
- NMU: Use buildreq for BR.

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2.git20141205
- Excluded tests

* Wed Dec 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20141205
- Initial build for Sisyphus

