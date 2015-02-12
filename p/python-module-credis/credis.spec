%define oname credis

%def_with python3

Name: python-module-%oname
Version: 1.0.5
Release: alt1.git20150211
Summary: High performance redis client implemented with cython
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/credis/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/yihuang/credis.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython python-module-hiredis
BuildPreReq: python-module-redis-py
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython python3-module-hiredis
BuildPreReq: python3-module-redis-py
%endif

%py_provides %oname
%py_requires hiredis

%description
Minimal redis client written in cython, 5X faster than redis-py.

%package -n python3-module-%oname
Summary: High performance redis client implemented with cython
Group: Development/Python3
%py3_provides %oname
%py3_requires hiredis

%description -n python3-module-%oname
Minimal redis client written in cython, 5X faster than redis-py.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
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

%files
%doc *.rst benchmark test
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst benchmark test
%python3_sitelibdir/*
%endif

%changelog
* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.git20150211
- Initial build for Sisyphus

