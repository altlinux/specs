%define oname auxlib

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 0.0.19
Release: alt1.git20150731
Summary: Auxiliary library to the python standard library
License: ISC
Group: Development/Python
Url: https://pypi.python.org/pypi/auxlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kalefranz/auxlib.git
# branch: develop
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-enum34 python-module-pycrypto
BuildPreReq: python-module-dateutil python-module-yaml
BuildPreReq: python-module-wheel python-module-pytest-cov
BuildPreReq: python-module-ddt python-module-testtools
BuildPreReq: python-module-radon python-module-mimeparse
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-enum34 python3-module-pycrypto
BuildPreReq: python3-module-dateutil python3-module-yaml
BuildPreReq: python3-module-wheel python3-module-pytest-cov
BuildPreReq: python3-module-ddt python3-module-testtools
BuildPreReq: python3-module-radon python3-module-mimeparse
%endif

%py_provides %oname
%py_requires enum34 Crypto dateutil yaml

%description
Auxiliary library to the python standard library.

%if_with python3
%package -n python3-module-%oname
Summary: Auxiliary library to the python standard library
Group: Development/Python3
%py3_provides %oname
%py3_requires enum34 Crypto dateutil yaml

%description -n python3-module-%oname
Auxiliary library to the python standard library.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
py.test -vv --cov %oname
%if_with python3
pushd ../python3
python3 setup.py test -v
py.test-%_python3_version -vv --cov %oname
popd
%endif

%files
%doc LICENSE *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.19-alt1.git20150731
- Initial build for Sisyphus

