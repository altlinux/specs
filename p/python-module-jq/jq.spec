%define oname jq

%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20150118
Summary: Lightweight and flexible JSON processor
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jq/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mwilliamson/jq.py.git
Source: %name-%version.tar

BuildPreReq: flex libjq-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython python-module-nose
BuildPreReq: python-module-tox
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython python3-module-nose
BuildPreReq: python3-module-tox
%endif

%py_provides %oname

%description
jq is a lightweight and flexible JSON processor.

This project contains Python bindings for jq.

%package -n python3-module-%oname
Summary: Lightweight and flexible JSON processor
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
jq is a lightweight and flexible JSON processor.

This project contains Python bindings for jq.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
cython jq.pyx
%python_build_debug

%if_with python3
pushd ../python3
cython3 jq.pyx
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
python setup.py build_ext -i
nosetests tests -v
%if_with python3
pushd ../python3
python3 setup.py test
python3 setup.py build_ext -i
nosetests3 tests -v
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
* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150118
- Initial build for Sisyphus

