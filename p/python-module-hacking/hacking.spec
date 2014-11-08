%define oname hacking

%def_with python3

Name: python-module-%oname
Version: 0.9.3
Release: alt1.git20141105
Summary: OpenStack Hacking Guideline Enforcement
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/hacking/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/openstack-dev/hacking.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: git
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pbr python-tools-pep8 pyflakes
BuildPreReq: python-module-flake8 python-module-mccabe
BuildPreReq: python-module-six python-module-coverage
BuildPreReq: python-module-discover python-module-fixtures
BuildPreReq: python-module-mock python-module-subunit
BuildPreReq: python-module-sphinx python-module-oslosphinx
BuildPreReq: python-module-testrepository python-module-testscenarios
BuildPreReq: python-module-testtools python-module-mimeparse
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pbr python3-tools-pep8 python3-pyflakes
BuildPreReq: python3-module-flake8 python3-module-mccabe
BuildPreReq: python3-module-six python3-module-coverage
BuildPreReq: python3-module-discover python3-module-fixtures
BuildPreReq: python3-module-mock python3-module-subunit
BuildPreReq: python3-module-sphinx python3-module-oslosphinx
BuildPreReq: python3-module-testrepository python3-module-testscenarios
BuildPreReq: python3-module-testtools python3-module-mimeparse
%endif

%py_provides %oname

%description
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: OpenStack Hacking Guideline Enforcement
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

This package contains tests for %oname.

%prep
%setup

git init-db
git config user.email "real at altlinux.org"
git config user.name "REAL"
git add . -A
git commit -a -m "commit"
git tag %version

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
mv %buildroot%python_sitelibdir/hacking-*-py%_python_version.egg-info \
	%buildroot%python_sitelibdir/hacking-py%_python_version.egg-info

%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%python3_sitelibdir/hacking-*-py%_python3_version.egg-info \
	%buildroot%python3_sitelibdir/hacking-py%_python3_version.egg-info
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst doc/source/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst doc/source/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.git20141105
- Initial build for Sisyphus

