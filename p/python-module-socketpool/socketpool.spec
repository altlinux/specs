%define oname socketpool

%def_with python3

Name: python-module-%oname
Version: 0.5.3
Release: alt1.git20140425
Summary: Simple Python socket pool
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/socketpool/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/benoitc/socketpool.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-eventlet python-module-gevent
BuildPreReq: python-module-py
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-eventlet python3-module-gevent
BuildPreReq: python3-module-py
%endif

%py_provides %oname

%description
Socket pool is a simple socket pool that suports multiple factories and
backends. It can easily be used by gevent, eventlet or any other
library.

%package -n python3-module-%oname
Summary: Simple Python socket pool
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Socket pool is a simple socket pool that suports multiple factories and
backends. It can easily be used by gevent, eventlet or any other
library.

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
export PYTHONPATH=$PWD
py.test
#if_with python3
%if 0
pushd ../python3
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc NOTICE *.rst THANKS UNLICENSE examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc NOTICE *.rst THANKS UNLICENSE examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1.git20140425
- Initial build for Sisyphus

