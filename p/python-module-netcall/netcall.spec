%define oname netcall

%def_without python3

Name: python-module-%oname
Version: 0.4.2
Release: alt3.git20141120
Summary: A simple Python RPC system (ZeroMQ + Threading/Tornado/Gevent/Eventlet/Greenhouse)
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/netcall/

# https://github.com/aglyzov/netcall.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-zmq python-module-pebble
BuildRequires: python-module-tornado python-modules-multiprocessing
BuildRequires: python-module-ioloop python-module-gevent
BuildRequires: python-module-eventlet python-module-greenhouse
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-zmq python3-module-pebble
BuildRequires: python3-module-tornado
BuildRequires: python3-module-ioloop python3-module-gevent
BuildRequires: python3-module-eventlet
BuildRequires: python-tools-2to3
%endif

%py_provides %oname
%py_requires zmq pebble multiprocessing tornado ioloop gevent
%py_requires eventlet greenhouse

%description
This is a simple Python RPC system using ZeroMQ as a transport and
supporting various concurrency techniques: Python Threading,
Tornado/IOLoop, Gevent, Eventlet, Greenhouse.

Initially the code was forked from ZPyRPC in Feb 2014. The fork has
added support for Python Threading and various Greenlet environments,
refactored code, made incompatible API changes, added new features and
examples.

%if_with python3
%package -n python3-module-%oname
Summary: A simple Python RPC system (ZeroMQ + Threading/Tornado/Gevent/Eventlet/Greenhouse)
Group: Development/Python3
%py3_provides %oname
%py3_requires zmq pebble multiprocessing tornado ioloop gevent
%py3_requires eventlet

%description -n python3-module-%oname
This is a simple Python RPC system using ZeroMQ as a transport and
supporting various concurrency techniques: Python Threading,
Tornado/IOLoop, Gevent, Eventlet, Greenhouse.

Initially the code was forked from ZPyRPC in Feb 2014. The fork has
added support for Python Threading and various Greenlet environments,
refactored code, made incompatible API changes, added new features and
examples.
%endif

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
python setup.py build_ext -i
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
rm -fR build
py.test3 -vv
popd
%endif

%files
%doc *.md examples
%python_sitelibdir/*
%exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.2-alt3.git20141120
- Fixed build.

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2.git20141120
- Fixed build

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20141120
- Initial build for Sisyphus

