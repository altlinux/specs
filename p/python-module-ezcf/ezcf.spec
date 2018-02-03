%define oname ezcf

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.dev1.git20150324.1.1
Summary: Import JSON/YAML like importing .py files
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ezcf/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/laike9m/ezcf.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-yaml
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-yaml
%endif

%py_provides %oname
%py_requires yaml json

%description
ezcf stands for easy configuration, it allows you to import JSON/YAML
like importing .py files, which is very useful for reading conf files
with these formats.

%if_with python3
%package -n python3-module-%oname
Summary: Import JSON/YAML like importing .py files
Group: Development/Python3
%py3_provides %oname
%py3_requires yaml json

%description -n python3-module-%oname
ezcf stands for easy configuration, it allows you to import JSON/YAML
like importing .py files, which is very useful for reading conf files
with these formats.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8

export PYTHONPATH=%buildroot%python_sitelibdir
python setup.py test
pushd tests
python -m unittest discover -v
popd
pushd tests2
python run_test.py -v
popd

%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 setup.py test
pushd tests
python3 -m unittest discover -v
popd
pushd tests2
python3 run_test.py -v
popd
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.1-alt1.dev1.git20150324.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.dev1.git20150324.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.dev1.git20150324
- Initial build for Sisyphus

