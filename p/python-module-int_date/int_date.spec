%define oname int_date

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20150816
Summary: Utility for int date like 20150312
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/int_date
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jealous/int_date.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-hamcrest python-module-pytest-cov
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-hamcrest python3-module-pytest-cov
%endif

%py_provides %oname

%description
Utilities to process the integer format date like: 20150301 First four
digits are year. Next two are month. Last two are date.

%if_with python3
%package -n python3-module-%oname
Summary: Utility for int date like 20150312
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Utilities to process the integer format date like: 20150301 First four
digits are year. Next two are month. Last two are date.
%endif

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
python setup.py test -v
py.test -vv --cov=%oname --junit-xml=junit-result.xml \
	--cov-report term-missing test
%if_with python3
pushd ../python3
python3 setup.py test -v
py.test-%_python3_version -vv --cov=%oname --junit-xml=junit-result.xml \
	--cov-report term-missing test
popd
%endif

%files
%doc *.md docs/_build/html
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150816
- Initial build for Sisyphus

