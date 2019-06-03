%define _unpackaged_files_terminate_build 1

%define oname kombu

# TODO: fix list issue
%def_disable test
%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 4.4.0
Release: alt1

Group: Development/Python
License: BSD License
Summary: Kombu is an AMQP messaging framework for Python

URL: https://github.com/celery/kombu/

# https://github.com/celery/kombu.git
# Source-url: https://pypi.io/packages/source/k/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

# Patches from Debian
Patch11: 0001-Remove-image-from-remote-donation-site-privacy-issue.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-anyjson python-module-boto python-module-django
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python2.7(sphinx_celery)
BuildRequires: python-module-pylibrabbitmq python-module-pymongo
BuildRequires: python-module-amqp >= 1:1.4.9
BuildRequires: python2.7(case) python2.7(unittest2) python2.7(mock) python2.7(pytest) python2.7(Pyro4) python2.7(serpent)
BuildRequires: python2.7(pytest_cov) python2.7(redis) python2.7(msgpack) python2.7(boto3) python2.7(pycurl)
BuildRequires: python-module-tox

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-amqp >= 1:1.4.9
BuildRequires: python3(pytz) python3(case) python3(unittest2) python3(mock) python3(pytest) python3(Pyro4) python3(serpent)
BuildRequires: python3(pytest_cov) python3(redis) python3(msgpack) python3(boto3) python3(pycurl)
BuildRequires: python3-module-tox
%endif

%description
AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is `RabbitMQ`_.

The aim of `Kombu` is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and also
provide proven and tested solutions to common messaging problems.

%if_with python3
%package -n python3-module-%oname
Summary: Kombu is an AMQP messaging framework for Python
Group: Development/Python3

%description -n python3-module-%oname
AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is `RabbitMQ`_.

The aim of `Kombu` is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and also
provide proven and tested solutions to common messaging problems.
%endif

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is `RabbitMQ`_.

The aim of `Kombu` is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and also
provide proven and tested solutions to common messaging problems.

This package contains documentation for %oname.

%prep
%setup
%patch11 -p1

# drop cosmetic only module
subst "s|pytest-sugar||" requirements/test.txt 

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

%if_enabled test
%check
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif
%endif

%files
%doc AUTHORS Changelog FAQ LICENSE README.rst THANKS TODO
%python_sitelibdir/kombu*

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS Changelog FAQ LICENSE README.rst THANKS TODO
%python3_sitelibdir/kombu*
%endif

%changelog
* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.4.0-alt1
- new version 4.4.0 (with rpmrb script)
- switch to build from tarball

* Thu Sep 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.2.1-alt1
- Updated to upstream version 4.2.1.

* Fri Feb 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.1.0-alt2
- Updated build dependencies.

* Wed Nov 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.1.0-alt1
- Updated to upstream version 4.1.0.
- Enabled tests.

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
