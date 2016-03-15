%define sname oslo.versionedobjects

%def_with python3

Name: python-module-%sname
Version: 0.10.0
Release: alt1.1.1
Summary: OpenStack oslo.versionedobjects library
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo
Source: %name-%version.tar

BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-anyjson python-module-babel python-module-cffi python-module-chardet python-module-contextlib2 python-module-cryptography python-module-cssselect python-module-debtcollector python-module-django python-module-dns python-module-docutils python-module-ecdsa python-module-enum34 python-module-eventlet python-module-fasteners python-module-flake8 python-module-genshi python-module-greenlet python-module-hacking python-module-iso8601 python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-monotonic python-module-ndg-httpsclient python-module-netaddr python-module-ntlm python-module-oslo.concurrency python-module-oslo.config python-module-oslo.context python-module-oslo.i18n python-module-oslo.log python-module-oslo.middleware python-module-oslo.serialization python-module-oslo.service python-module-oslo.utils python-module-paste python-module-pbr python-module-psycopg2 python-module-pyasn1 python-module-pycrypto python-module-pytest python-module-pytz python-module-repoze.lru python-module-serial python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-stevedore python-module-twisted-core python-module-unittest2 python-module-webob python-module-wrapt python-module-yaml python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-contextlib2 python3-module-cryptography python3-module-cssselect python3-module-django python3-module-dns python3-module-docutils python3-module-ecdsa python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-greenlet python3-module-jinja2 python3-module-markupsafe python3-module-mccabe python3-module-mimeparse python3-module-netaddr python3-module-ntlm python3-module-oslo.concurrency python3-module-oslo.config python3-module-oslo.log python3-module-oslo.middleware python3-module-oslo.service python3-module-paste python3-module-pbr python3-module-pip python3-module-psycopg2 python3-module-pycparser python3-module-pycrypto python3-module-pytest python3-module-pytz python3-module-repoze.lru python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-unittest2 python3-module-wrapt python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-html5lib python-module-oslo.messaging python-module-oslosphinx python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-oslo.messaging rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 1.6
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-six >= 1.9.0
#BuildRequires: python-module-babel >= 1.3
#BuildRequires: python-module-oslo.concurrency >= 2.3.0
#BuildRequires: python-module-oslo.config >= 2.3.0
#BuildRequires: python-module-oslo.context >= 0.2.0
#BuildRequires: python-module-oslo.messaging >= 1.16.0
#BuildRequires: python-module-oslo.serialization >= 1.4.0
#BuildRequires: python-module-oslo.utils >= 2.0.0
#BuildRequires: python-module-iso8601 >= 0.1.9
#BuildRequires: python-module-oslo.log >= 0.8.0
#BuildRequires: python-module-oslo.i18n >= 1.5.0
#BuildRequires: python-module-fixtures >= 1.3.1


%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 1.6
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
#BuildRequires: python3-module-six >= 1.9.0
#BuildRequires: python3-module-babel >= 1.3
#BuildRequires: python3-module-oslo.concurrency >= 2.3.0
#BuildRequires: python3-module-oslo.config >= 2.3.0
#BuildRequires: python3-module-oslo.context >= 0.2.0
#BuildRequires: python3-module-oslo.messaging >= 1.16.0
#BuildRequires: python3-module-oslo.serialization >= 1.4.0
#BuildRequires: python3-module-oslo.utils >= 2.0.0
#BuildRequires: python3-module-iso8601 >= 0.1.9
#BuildRequires: python3-module-oslo.log >= 0.8.0
#BuildRequires: python3-module-oslo.i18n >= 1.5.0
#BuildRequires: python3-module-fixtures >= 1.3.1
%endif

%description
oslo.versionedobjects library deals with DB schema being at different versions
than the code expects, allowing services to be operated safely during upgrades.
It enables DB independent schema by providing an abstraction layer, which
allows us to support SQL and NoSQL Databases. oslo.versionedobjects is also
used in RPC APIs, to ensure upgrades happen without spreading version dependent
code across different services and projects.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/oslo.versionedobjects
* Source: http://git.openstack.org/cgit/openstack/oslo.versionedobjects
* Bugs: http://bugs.launchpad.net/oslo.versionedobjects

%if_with python3
%package -n python3-module-%sname
Summary: OpenStack oslo.versionedobjects library
Group: Development/Python3

%description -n python3-module-%sname
oslo.versionedobjects library deals with DB schema being at different versions
than the code expects, allowing services to be operated safely during upgrades.
It enables DB independent schema by providing an abstraction layer, which
allows us to support SQL and NoSQL Databases. oslo.versionedobjects is also
used in RPC APIs, to ensure upgrades happen without spreading version dependent
code across different services and projects.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/oslo.versionedobjects
* Source: http://git.openstack.org/cgit/openstack/oslo.versionedobjects
* Bugs: http://bugs.launchpad.net/oslo.versionedobjects
%endif


%package doc
Summary: Documentation for the Oslo versionedobjects library
Group: Development/Documentation

%description doc
Documentation for the Oslo versionedobjects library.

%prep
%setup

# Remove bundled egg-info
rm -rf %sname.egg-info

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
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Mon Jun 01 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- Initial release
