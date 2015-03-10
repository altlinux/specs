%define mname unicore
%define oname %mname.google

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20150120
Summary: Tools for dealing with Google from Universal Core
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/unicore.google/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/universalcore/unicore.google.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid_celery python-module-mock
BuildPreReq: python-module-universal-analytics-python
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid_celery python3-module-mock
BuildPreReq: python3-module-universal-analytics-python
%endif

%py_provides %oname
%py_requires %mname pyramid_celery UniversalAnalytics

%description
Tools for interfacing with Google APIs from Universal Core.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Tools for interfacing with Google APIs from Universal Core.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Tools for dealing with Google from Universal Core
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname pyramid_celery UniversalAnalytics

%description -n python3-module-%oname
Tools for interfacing with Google APIs from Universal Core.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Tools for interfacing with Google APIs from Universal Core.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|urllib2|urllib.request|' \
	../python3/%mname/google/tests/test_tasks.py
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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
rm -fR build
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/google
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/google/tests

%files tests
%python_sitelibdir/%mname/google/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/google
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/google/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/google/tests
%endif

%changelog
* Tue Mar 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20150120
- Initial build for Sisyphus

