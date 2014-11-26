%define oname pyramid_ldap3

%def_with python3

Name: python-module-%oname
Version: 0.2.3
Release: alt1.git20141123
Summary: Provides LDAP authentication services for your Pyramid application based on python3-ldap
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_ldap3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Cito/pyramid_ldap3.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-ldap3
BuildPreReq: python-module-waitress python-module-pyramid_debugtoolbar
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-pyasn1
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-ldap3
BuildPreReq: python3-module-waitress python3-module-pyramid_debugtoolbar
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-pyasn1
%endif

%py_provides %oname

%description
pyramid_ldap3 provides LDAP authentication services for your Pyramid
application. It is a fork of the pyramid_ldap package with the goal of
eliminating the dependency on python-ldap and ldappool, replacing it
with a dependency on python3-ldap, which is a pure Python package that
also supports Python 3.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
pyramid_ldap3 provides LDAP authentication services for your Pyramid
application. It is a fork of the pyramid_ldap package with the goal of
eliminating the dependency on python-ldap and ldappool, replacing it
with a dependency on python3-ldap, which is a pure Python package that
also supports Python 3.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Provides LDAP authentication services for your Pyramid application based on python3-ldap
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pyramid_ldap3 provides LDAP authentication services for your Pyramid
application. It is a fork of the pyramid_ldap package with the goal of
eliminating the dependency on python-ldap and ldappool, replacing it
with a dependency on python3-ldap, which is a pure Python package that
also supports Python 3.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
pyramid_ldap3 provides LDAP authentication services for your Pyramid
application. It is a fork of the pyramid_ldap package with the goal of
eliminating the dependency on python-ldap and ldappool, replacing it
with a dependency on python3-ldap, which is a pure Python package that
also supports Python 3.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/sampleapp
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/sampleapp
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20141123
- Initial build for Sisyphus

