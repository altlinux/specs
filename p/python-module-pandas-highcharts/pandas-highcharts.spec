%define oname pandas-highcharts

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3.0
Release: alt1.git20150228
Summary: Easily build Highcharts plots with pandas.DataFrame objects
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pandas-highcharts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gtnx/pandas-highcharts.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pandas python-module-pytz
BuildPreReq: python-module-numpy ipython
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pandas python3-module-pytz
BuildPreReq: python3-module-numpy ipython3
BuildPreReq: python-tools-2to3
%endif

%py_provides pandas_highcharts
%py_requires pandas pytz json numpy IPython

%description
pandas-highcharts is a Python package which allows you to easily build
Highcharts plots with pandas.DataFrame objects.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip core

%description tests
pandas-highcharts is a Python package which allows you to easily build
Highcharts plots with pandas.DataFrame objects.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Easily build Highcharts plots with pandas.DataFrame objects
Group: Development/Python3
%py3_provides pandas_highcharts
%py3_requires pandas pytz json numpy IPython

%description -n python3-module-%oname
pandas-highcharts is a Python package which allows you to easily build
Highcharts plots with pandas.DataFrame objects.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
pandas-highcharts is a Python package which allows you to easily build
Highcharts plots with pandas.DataFrame objects.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
python -m unittest -v pandas_highcharts.tests
%if_with python3
pushd ../python3
python3 setup.py test
python3 -m unittest -v pandas_highcharts.tests
popd
%endif

%files
%doc *.rst *.ipynb
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.ipynb
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150228
- Initial build for Sisyphus

