%define oname manhole

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.0.0
Release: alt2.git20150419
Summary: Debugging manhole for python applications 
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/manhole/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ionelmc/python-manhole.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-dns python-module-docutils python-module-greenlet python-module-html5lib python-module-objects.inv python-module-psycopg2 python-module-pytest python-module-signalfd python-module-sphinx_py3doc_enhanced_theme python-module-sphinxcontrib-napoleon
BuildPreReq: python-module-sphinx-devel

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-process-tests python-module-signalfd
#BuildPreReq: python-module-gevent python-module-eventlet
#BuildPreReq: python-module-sphinx-devel /dev/pts /proc
#BuildPreReq: python-module-sphinxcontrib-napoleon
#BuildPreReq: python-module-sphinx_py3doc_enhanced_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-process-tests python3-module-signalfd
#BuildPreReq: python3-module-gevent python3-module-eventlet
BuildRequires: python3-module-cryptography python3-module-dns python3-module-greenlet python3-module-psycopg2 python3-module-pytest python3-module-signalfd
%endif

%py_provides %oname
#%py_requires signalfd eventlet gevent ctypes

%description
Manhole is in-process service that will accept unix domain socket
connections and present the stacktraces for all threads and an
interactive prompt. It can either work as a python daemon thread waiting
for connections at all times or a signal handler (stopping your
application and waiting for a connection).

Access to the socket is restricted to the application's effective user
id or root.

%package -n python3-module-%oname
Summary: Debugging manhole for python applications 
Group: Development/Python3
%py3_provides %oname
#%py3_requires signalfd eventlet gevent ctypes

%description -n python3-module-%oname
Manhole is in-process service that will accept unix domain socket
connections and present the stacktraces for all threads and an
interactive prompt. It can either work as a python daemon thread waiting
for connections at all times or a signal handler (stopping your
application and waiting for a connection).

Access to the socket is restricted to the application's effective user
id or root.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Manhole is in-process service that will accept unix domain socket
connections and present the stacktraces for all threads and an
interactive prompt. It can either work as a python daemon thread waiting
for connections at all times or a signal handler (stopping your
application and waiting for a connection).

Access to the socket is restricted to the application's effective user
id or root.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Manhole is in-process service that will accept unix domain socket
connections and present the stacktraces for all threads and an
interactive prompt. It can either work as a python daemon thread waiting
for connections at all times or a signal handler (stopping your
application and waiting for a connection).

Access to the socket is restricted to the application's effective user
id or root.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=$PWD/src
pushd docs
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
export PYTHONPATH=$PWD/src
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD/src
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.0-alt2.git20150419
- Rebuild with "def_disable check"
- Cleanup buildreq

* Wed Apr 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150419
- New snapshot

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20141223
- Initial build for Sisyphus

