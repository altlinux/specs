%define oname rabbitpy

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.21.1
Release: alt1.git20141030
Summary: A pure python, thread-safe, minimalistic and pythonic RabbitMQ client library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/rabbitpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gmr/rabbitpy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pamqp python-module-nose
BuildPreReq: python-module-mock python-module-coverage
BuildPreReq: python-module-coveralls
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pamqp python3-module-nose
BuildPreReq: python3-module-mock python3-module-coverage
BuildPreReq: python3-module-coveralls
%endif

%py_provides %oname

%description
A pure python, thread-safe, minimalistic and pythonic BSD Licensed
AMQP/RabbitMQ library that supports Python 2.6+ and Python 3.2+.
rabbitpy aims to provide a simple and easy to use API for interfacing
with RabbitMQ, minimizing the programming overhead often found in other
libraries.

%package -n python3-module-%oname
Summary: A pure python, thread-safe, minimalistic and pythonic RabbitMQ client library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A pure python, thread-safe, minimalistic and pythonic BSD Licensed
AMQP/RabbitMQ library that supports Python 2.6+ and Python 3.2+.
rabbitpy aims to provide a simple and easy to use API for interfacing
with RabbitMQ, minimizing the programming overhead often found in other
libraries.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A pure python, thread-safe, minimalistic and pythonic BSD Licensed
AMQP/RabbitMQ library that supports Python 2.6+ and Python 3.2+.
rabbitpy aims to provide a simple and easy to use API for interfacing
with RabbitMQ, minimizing the programming overhead often found in other
libraries.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A pure python, thread-safe, minimalistic and pythonic BSD Licensed
AMQP/RabbitMQ library that supports Python 2.6+ and Python 3.2+.
rabbitpy aims to provide a simple and easy to use API for interfacing
with RabbitMQ, minimizing the programming overhead often found in other
libraries.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.21.1-alt1.git20141030
- Initial build for Sisyphus

