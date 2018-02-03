%define oname eventlet

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.18.4
Release: alt1.1
Summary: Highly concurrent networking library
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/eventlet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eventlet/eventlet.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-greenlet >= 0.3
BuildRequires: python-module-nose
BuildRequires: python-module-OpenSSL python-module-six
BuildRequires: python-module-mysqlclient
BuildRequires: python-modules-json
BuildRequires: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-greenlet python3-module-nose
BuildRequires: python3-module-OpenSSL python3-module-six
BuildRequires: python3-module-mysqlclient
%endif
%py_requires greenlet six json OpenSSL MySQLdb
%add_python_req_skip stackless

BuildRequires(pre): rpm-macros-sphinx

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
%py3_requires greenlet six json OpenSSL MySQLdb
%add_python3_req_skip stackless
%add_python3_req_skip eventlet.support.six.moves

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
%exclude %python_sitelibdir/*/pickle

%files docs
%doc examples doc/_build/html

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS NEWS README*
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.18.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 0.18.4-alt1
- 0.18.4

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.17.4-alt1.git20150722.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.17.4-alt1.git20150722.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17.4-alt1.git20150722
- Version 0.17.4

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17.1-alt1.git20150225
- Version 0.17.1

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

