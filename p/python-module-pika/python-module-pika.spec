%define modulename pika

%def_with python3

Name: python-module-%modulename
Version: 0.9.14
Release: alt1.git20141201

%setup_python_module %modulename

Summary: Pika is a pure-Python implementation of the AMQP 0-9-1 protocol.
License: MPLv2.0
Group: Development/Python

Url: http://github.com/pika/pika
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: %py_dependencies setuptools
BuildPreReq: python-module-sphinx-devel python-module-twisted-core
BuildPreReq: python-module-tornado
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires twisted.internet tornado

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
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.14-alt1.git20141201
- New snapshot

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.14-alt1.git20140711
- Version 0.9.14
- Added module for Python 3

* Tue Jan 17 2012 Alexey Morsov <swi@altlinux.ru> 0.9.5-alt1.git20120106
- initial build

