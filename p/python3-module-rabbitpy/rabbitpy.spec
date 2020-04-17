%define oname rabbitpy

%def_disable check

Name: python3-module-%oname
Version: 0.23.0
Release: alt2.git20141105.1.2

Summary: A pure python, thread-safe, minimalistic and pythonic RabbitMQ client library
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/rabbitpy/

BuildArch: noarch

# https://github.com/gmr/rabbitpy.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-pamqp
BuildRequires: python3-module-mock
BuildRequires: python3-module-nose

%description
A pure python, thread-safe, minimalistic and pythonic BSD Licensed
AMQP/RabbitMQ library that supports Python 2.6+ and Python 3.2+.
rabbitpy aims to provide a simple and easy to use API for interfacing
with RabbitMQ, minimizing the programming overhead often found in other
libraries.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

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

sed -i 's|sphinx-build|&-3|' docs/Makefile

%build
%python3_build_debug

%install
%python3_install

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Fri Apr 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.23.0-alt2.git20141105.1.2
- Build for python2 disabled.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.23.0-alt1.git20141105.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.23.0-alt1.git20141105.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.23.0-alt1.git20141105.1
- NMU: Use buildreq for BR.

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt1.git20141105
- Version 0.23.0

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.21.1-alt1.git20141030
- Initial build for Sisyphus

