%define modulename pika

%def_with python3

Name: python-module-%modulename
Version: 0.9.14
Release: alt1.git20141201.1.1

%setup_python_module %modulename

Summary: Pika is a pure-Python implementation of the AMQP 0-9-1 protocol.
License: MPLv2.0
Group: Development/Python

Url: http://github.com/pika/pika
BuildArch: noarch

Source: %name-%version.tar

#BuildPreReq: %py_dependencies setuptools
#BuildPreReq: python-module-sphinx-devel python-module-twisted-core
#BuildPreReq: python-module-tornado
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires twisted.internet tornado

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-twisted-core python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-tornado python-module-twisted-logger python3-module-setuptools rpm-build-python3 time

%description
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that
tries to stay fairly independent of the underlying network support
library.

%package docs
Summary: Documentation for %modulename
Group: Development/Documentation

%description docs
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that
tries to stay fairly independent of the underlying network support
library.

This package contains documentation for %modulename.

%package -n python3-module-%modulename
Summary: Pika is a pure-Python implementation of the AMQP 0-9-1 protoco
Group: Development/Python3
%py3_requires twisted.internet tornado

%description -n python3-module-%modulename
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that
tries to stay fairly independent of the underlying network support
library.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%files
%doc *.rst
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%modulename
%doc *.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.14-alt1.git20141201.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.14-alt1.git20141201.1
- NMU: Use buildreq for BR.

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.14-alt1.git20141201
- New snapshot

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.14-alt1.git20140711
- Version 0.9.14
- Added module for Python 3

* Tue Jan 17 2012 Alexey Morsov <swi@altlinux.ru> 0.9.5-alt1.git20120106
- initial build

