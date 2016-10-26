%define module_name kombu

%def_with python3

Name: python-module-%module_name
Version: 3.0.37
Release: alt1
Epoch: 1
Group: Development/Python
License: BSD License
Summary: Kombu is an AMQP messaging framework for Python
URL: https://github.com/celery/kombu/
Source: %name-%version.tar

#BuildPreReq: python-module-setuptools python-module-sphinx-devel
#BuildPreReq: python-module-django python-module-amqp
#BuildPreReq: python-module-anyjson python-module-boto
#BuildPreReq: python-module-pylibrabbitmq python-module-pymongo
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-amqp python-module-babel python-module-backports python-module-bson python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-ecdsa python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-psycopg2 python-module-pyasn1 python-module-pycrypto python-module-pytz python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base
BuildRequires: python-module-alabaster python-module-anyjson python-module-boto python-module-django python-module-docutils python-module-html5lib python-module-objects.inv python-module-pylibrabbitmq python-module-pymongo python3-module-setuptools rpm-build-python3 time
BuildRequires: python-module-amqp >= 1:1.4.9

%description
AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is `RabbitMQ`_.

The aim of `Kombu` is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and also
provide proven and tested solutions to common messaging problems.

%package tests
Summary: Tests for %module_name
Group: Development/Python
Requires: %name = %EVR

%description tests
AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is `RabbitMQ`_.

The aim of `Kombu` is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and also
provide proven and tested solutions to common messaging problems.

This package contain tests for %module_name.

%package -n python3-module-%module_name
Summary: Kombu is an AMQP messaging framework for Python
Group: Development/Python3

%description -n python3-module-%module_name
AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is `RabbitMQ`_.

The aim of `Kombu` is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and also
provide proven and tested solutions to common messaging problems.

%package -n python3-module-%module_name-tests
Summary: Tests for %module_name
Group: Development/Python3
Requires: python3-module-%module_name = %EVR

%description -n python3-module-%module_name-tests
AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is `RabbitMQ`_.

The aim of `Kombu` is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and also
provide proven and tested solutions to common messaging problems.

This package contain tests for %module_name.

%package docs
Summary: Documentation for %module_name
Group: Development/Documentation
BuildArch: noarch

%description docs
AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is `RabbitMQ`_.

The aim of `Kombu` is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and also
provide proven and tested solutions to common messaging problems.

This package contains documentation for %module_name.

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

%if "%_target_libdir_noarch" != "%_libdir"
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%files
%doc AUTHORS Changelog FAQ LICENSE README.rst THANKS TODO
%python_sitelibdir/kombu*
%exclude %python_sitelibdir/kombu/tests

%files tests
%python_sitelibdir/kombu/tests

%files docs
%doc docs/.build/html/*

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS Changelog FAQ LICENSE README.rst THANKS TODO
%python3_sitelibdir/kombu*
%exclude %python3_sitelibdir/kombu/tests

%files -n python3-module-%module_name-tests
%python3_sitelibdir/kombu/tests
%endif

%changelog
* Wed Oct 26 2016 Alexey Shabalin <shaba@altlinux.ru> 1:3.0.37-alt1
- 3.0.37

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:3.0.32-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:3.0.32-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:3.0.32-alt1.1
- NMU: Use buildreq for BR.

* Tue Dec 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1:3.0.32-alt1
- 3.0.32

* Mon Sep 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1:3.0.26-alt1
- downgrade to 3.0.26

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.a1.git20150714
- New snapshot

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.a1.git20141209
- New snapshot

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.a1.git20141117
- New snapshot

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.a1.git20141013
- Version 3.1.0a1

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.21-alt1.git20140707
- Version 3.0.21
- Added module for Python 3

* Sat Apr 13 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.10-alt1
- new version (ALT #28838)

* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1.7-alt1
- build for ALT
