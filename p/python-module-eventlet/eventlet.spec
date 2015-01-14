%define oname eventlet

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.16.1
Release: alt1.git20150114
Summary: Highly concurrent networking library
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/eventlet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eventlet/eventlet.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-greenlet python-module-nose
BuildPreReq: python-module-OpenSSL
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-greenlet python3-module-nose
BuildPreReq: python3-module-OpenSSL
%endif
%add_python_req_skip stackless

%description
Eventlet is a concurrent networking library for Python that allows you
to change how you run your code, not how you write it.

It uses epoll or libevent for highly scalable non-blocking I/O.
Coroutines ensure that the developer uses a blocking style of
programming that is similar to threading, but provide the benefits of
non-blocking I/O. The event dispatch is implicit, which means you can
easily use Eventlet from the Python interpreter, or as a small part of a
larger application.

%package -n python3-module-%oname
Summary: Highly concurrent networking library
Group: Development/Python3
%add_python3_req_skip stackless

%description -n python3-module-%oname
Eventlet is a concurrent networking library for Python that allows you
to change how you run your code, not how you write it.

It uses epoll or libevent for highly scalable non-blocking I/O.
Coroutines ensure that the developer uses a blocking style of
programming that is similar to threading, but provide the benefits of
non-blocking I/O. The event dispatch is implicit, which means you can
easily use Eventlet from the Python interpreter, or as a small part of a
larger application.

%package pickles
Summary: Pickles for Eventlet
Group: Development/Python

%description pickles
Eventlet is a concurrent networking library for Python that allows you
to change how you run your code, not how you write it.

It uses epoll or libevent for highly scalable non-blocking I/O.
Coroutines ensure that the developer uses a blocking style of
programming that is similar to threading, but provide the benefits of
non-blocking I/O. The event dispatch is implicit, which means you can
easily use Eventlet from the Python interpreter, or as a small part of a
larger application.

This package contains pickles for Eventlet.

%package docs
Summary: Documentation for Eventlet
Group: Development/Documentation
BuildArch: noarch

%description docs
Eventlet is a concurrent networking library for Python that allows you
to change how you run your code, not how you write it.

It uses epoll or libevent for highly scalable non-blocking I/O.
Coroutines ensure that the developer uses a blocking style of
programming that is similar to threading, but provide the benefits of
non-blocking I/O. The event dispatch is implicit, which means you can
easily use Eventlet from the Python interpreter, or as a small part of a
larger application.

This package contains documentation for Eventlet.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%make -C doc pickle
%make -C doc html

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
rm -fR build
python setup.py test
%if_with python3
pushd ../python3
rm -fR build
python3 setup.py test
popd
%endif

%files
%doc AUTHORS NEWS README*
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/pickle

%files docs
%doc examples doc/_build/html

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS NEWS README*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16.1-alt1.git20150114
- Version 0.16.1

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16.0-alt1.git20141230
- Version 0.16.0
- Added module for Python 3

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16.0-alt1.dev.git20141106
- Version 0.16.0.dev

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt2
- Added module for Python 3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1
- Version 0.15.0

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1
- Version 0.14.0

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.1-alt1
- Version 0.12.1

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.16-alt1
- Initial build for Sisyphus

