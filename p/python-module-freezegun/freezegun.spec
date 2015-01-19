%define oname freezegun

%def_with python3

Name: python-module-%oname
Version: 0.2.8
Release: alt1.git20141231
Summary: Let your Python tests travel through time
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/freezegun/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/spulec/freezegun.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-dateutil
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-coveralls python-module-sure
BuildPreReq: python-module-mock
BuildPreReq: python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-dateutil
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-coveralls python3-module-sure
BuildPreReq: python3-module-mock
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides %oname
%py_requires six dateutil sqlite3

%description
FreezeGun is a library that allows your python tests to travel through
time by mocking the datetime module.

%package -n python3-module-%oname
Summary: Let your Python tests travel through time
Group: Development/Python3
%py3_provides %oname
%py3_requires six dateutil sqlite3

%description -n python3-module-%oname
FreezeGun is a library that allows your python tests to travel through
time by mocking the datetime module.

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
sed -i 's|nosetests|nosetests -v|' Makefile
%make test
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3 -v|' Makefile
%make test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt1.git20141231
- Initial build for Sisyphus

