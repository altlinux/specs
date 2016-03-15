%global sname oslo.messaging

%def_with python3

Name:       python-module-%sname
Epoch:      1
Version:    2.5.0
Release:    alt1.1.1
Summary:    OpenStack common messaging library

Group:      Development/Python
License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    %name-%version.tar

Provides:  python-module-oslo-messaging = %EVR
Obsoletes: python-module-oslo-messaging < %EVR
BuildArch:  noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-amqp python-module-anyjson python-module-babel python-module-cffi python-module-chardet python-module-contextlib2 python-module-cryptography python-module-cssselect python-module-debtcollector python-module-django python-module-dns python-module-docutils python-module-ecdsa python-module-enum34 python-module-eventlet python-module-extras python-module-fasteners python-module-fixtures python-module-flake8 python-module-futures python-module-genshi python-module-greenlet python-module-hacking python-module-iso8601 python-module-jinja2 python-module-jinja2-tests python-module-linecache2 python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-monotonic python-module-msgpack python-module-ndg-httpsclient python-module-netaddr python-module-netifaces python-module-ntlm python-module-oslo.concurrency python-module-oslo.config python-module-oslo.context python-module-oslo.i18n python-module-oslo.log python-module-oslo.serialization python-module-oslo.utils python-module-paste python-module-pbr python-module-psycopg2 python-module-pyasn1 python-module-pycrypto python-module-pytest python-module-pytz python-module-repoze.lru python-module-serial python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-stevedore python-module-testtools python-module-traceback2 python-module-twisted-core python-module-unittest2 python-module-wrapt python-module-yaml python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-dns python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-greenlet python3-module-jinja2 python3-module-markupsafe python3-module-mccabe python3-module-mimeparse python3-module-netaddr python3-module-ntlm python3-module-oslo.concurrency python3-module-oslo.config python3-module-oslo.log python3-module-paste python3-module-pbr python3-module-pip python3-module-psycopg2 python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-repoze.lru python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-unittest2 python3-module-wrapt python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.urllib3 python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-cachetools python-module-d2to1 python-module-futurist python-module-html5lib python-module-kombu python-module-oslo.middleware python-module-oslo.service python-module-oslosphinx python-module-zmq python3-module-contextlib2 python3-module-d2to1 python3-module-django python3-module-ecdsa python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-oslo.middleware python3-module-oslo.service python3-module-pycrypto python3-module-yieldfrom.requests rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 1.6
#BuildRequires: python-module-d2to1
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-iso8601
#BuildRequires: python-module-futurist >= 0.1.2
#BuildRequires: python-module-oslo.config >= 2.3.0
#BuildRequires: python-module-oslo.context >= 0.2.0
#BuildRequires: python-module-oslo.log >= 1.8.0
#BuildRequires: python-module-oslo.utils >= 2.0.0
#BuildRequires: python-module-oslo.serialization >= 1.4.0
#BuildRequires: python-module-oslo.service >= 0.7.0
#BuildRequires: python-module-oslo.i18n >= 1.5.0
#BuildRequires: python-module-oslo.middleware >= 2.8.0
#BuildRequires: python-module-six >= 1.9.0
#BuildRequires: python-module-cachetools >= 1.0.0
#BuildRequires: python-module-stevedore >= 1.5.0
#BuildRequires: python-module-yaml >= 3.1.0
#BuildRequires: python3-module-amqp >= 1.4.0
#BuildRequires: python-module-kombu >= 3.0.7
#BuildRequires: python-module-qpid-proton
#BuildRequires: python-module-eventlet >= 0.17.4
#BuildRequires: python-module-greenlet >= 0.3.2
#BuildRequires: python-module-fixtures
#BuildRequires: python-module-babel
#BuildRequires: python-module-futures >= 2.1.6
#BuildRequires: python-module-aioeventlet >= 0.4
#BuildRequires: python-module-trollius >= 1.0
#BuildRequires: python-module-futurist
#BuildRequires: python-module-contextlib2
#BuildRequires: python-module-zmq

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 0.6
#BuildRequires: python3-module-d2to1
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
#BuildRequires: python3-module-iso8601
#BuildRequires: python3-module-futurist >= 0.1.2
#BuildRequires: python3-module-oslo.config >= 2.3.0
#BuildRequires: python3-module-oslo.context >= 0.2.0
#BuildRequires: python3-module-oslo.log >= 1.8.0
#BuildRequires: python3-module-oslo.utils >= 2.0.0
#BuildRequires: python3-module-oslo.serialization >= 1.4.0
#BuildRequires: python3-module-oslo.service >= 0.7.0
#BuildRequires: python3-module-oslo.i18n >= 1.5.0
#BuildRequires: python3-module-oslo.middleware >= 2.8.0
#BuildRequires: python3-module-six >= 1.9.0
#BuildRequires: python3-module-cachetools >= 1.0.0
#BuildRequires: python3-module-stevedore >= 1.5.0
#BuildRequires: python3-module-yaml >= 3.1.0
#BuildRequires: python3-module-amqp >= 1.4.0
#BuildRequires: python3-module-kombu >= 3.0.7
# BuildRequires: python3-module-qpid-proton
#BuildRequires: python3-module-eventlet >= 0.17.4
#BuildRequires: python3-module-greenlet >= 0.3.2
#BuildRequires: python3-module-fixtures
#BuildRequires: python3-module-babel
#BuildRequires: python3-module-aioeventlet >= 0.4
#BuildRequires: python3-module-trollius >= 1.0
%endif

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

%if_with python3
%package -n python3-module-oslo.messaging
Summary: OpenStack oslo.messaging library
Group: Development/Python3
Provides: python3-module-oslo-messaging = %EVR
%add_python3_req_skip proton
%add_python3_req_skip pyngus

%description -n python3-module-oslo.messaging
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.
%endif

%package doc
Summary:    Documentation for OpenStack common messaging library
Group:     Development/Documentation
Provides:  python-module-oslo-messaging-doc = %EVR
Obsoletes: python-module-oslo-messaging-doc < %EVR

%description doc
Documentation for the oslo.messaging library.

%prep
%setup


# Remove bundled egg-info
#rm -rf %sname.egg-info
# let RPM handle deps
#sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
#rm -rf {test-,}requirements.txt

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif
%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst LICENSE
%python_sitelibdir/*
%_bindir/*

%if_with python3
%files -n python3-module-oslo.messaging
%python3_sitelibdir/*
%endif

%files doc
%doc html LICENSE

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:2.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:2.5.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1:2.5.0-alt1
- 2.5.0

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.8.3-alt1
- 1.8.3

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0
- add python3 package

* Tue Feb 17 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Tue Jul 15 2014 Lenar Shakirov <snejok@altlinux.ru> 1.3.0.2-alt1
- First build for ALT (based on Fedora 1.3.0.2-4.fc21.src)
