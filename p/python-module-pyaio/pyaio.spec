%define oname pyaio

%def_disable check
%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt2.git20130914
Summary: Python aio bindings
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyaio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/felipecruz/pyaio.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-gevent
BuildPreReq: python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-gevent
%endif

%py_provides %oname

%description
Python Asynchronous I/O bindings (aio.h).

You should wait for the callback to finish before queuing more requests
in a tight loop. pyaio could hang if you hit the max aio queue size.

%package -n python3-module-%oname
Summary: Python aio bindings
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python Asynchronous I/O bindings (aio.h).

You should wait for the callback to finish before queuing more requests
in a tight loop. pyaio could hang if you hit the max aio queue size.

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
python setup.py build_ext -i
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%files
%doc AUTHORS *.markdown
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.markdown
%python3_sitelibdir/*
%endif

%changelog

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 0.4-alt2.git20130914
- Disable tests

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20130914
- Initial build for Sisyphus

