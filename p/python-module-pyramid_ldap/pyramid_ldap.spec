%define oname pyramid_ldap

%def_without python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20130717
Summary: LDAP authentication policy for Pyramid
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_ldap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pylons/pyramid_ldap.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-ldappool-tests
BuildPreReq: python-module-ldap-tests python-module-waitress
BuildPreReq: python-module-pyramid_debugtoolbar python-module-nose
BuildPreReq: python-module-coverage python-module-PasteDeploy
BuildPreReq: python-module-zope.deprecation python-module-repoze.lru
BuildPreReq: python-module-zope.component
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid python3-module-PasteDeploy
BuildPreReq: python3-module-ldap python3-module-waitress
BuildPreReq: python3-module-pyramid_debugtoolbar python3-module-nose
BuildPreReq: python3-module-coverage python3-module-zope.deprecation
BuildPreReq: python3-module-repoze.lru python3-module-zope.component
%endif

%py_provides %oname

%description
pyramid_ldap provides LDAP authentication services for your Pyramid
application.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
pyramid_ldap provides LDAP authentication services for your Pyramid
application.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: LDAP authentication policy for Pyramid
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pyramid_ldap provides LDAP authentication services for your Pyramid
application.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
pyramid_ldap provides LDAP authentication services for your Pyramid
application.

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
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.txt *.rst docs/*.rst
%python_sitelibdir/%oname
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20130717
- Initial build for Sisyphus

