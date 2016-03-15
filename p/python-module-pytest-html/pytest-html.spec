%define oname pytest-html

%def_with python3

Name: python-module-%oname
Version: 1.3.2
Release: alt1.git20150727.1
Summary: Plugin for generating HTML reports for py.test results
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-html/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/davehunt/pytest-html.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides pytest_html
%py_requires pytest json

%description
pytest-html is a plugin for py.test that generates a HTML report for the
test results.

%if_with python3
%package -n python3-module-%oname
Summary: Plugin for generating HTML reports for py.test results
Group: Development/Python3
%py3_provides pytest_html
%py3_requires pytest

%description -n python3-module-%oname
pytest-html is a plugin for py.test that generates a HTML report for the
test results.
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
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.2-alt1.git20150727.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.git20150727
- Initial build for Sisyphus

