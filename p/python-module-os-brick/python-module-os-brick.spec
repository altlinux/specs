%define pypi_name os-brick

%def_with python3

Name: python-module-%pypi_name
Version: 0.5.0
Release: alt1.1
Summary: OpenStack Cinder brick library for managing local volume attaches
Group: Development/Python
License: ASL 2.0
Url: https://github.com/openstack/%pypi_name
Source: %name-%version.tar

BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-debtcollector python-module-dns python-module-docutils python-module-enum34 python-module-eventlet python-module-fasteners python-module-flake8 python-module-genshi python-module-greenlet python-module-hacking python-module-iso8601 python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-monotonic python-module-ndg-httpsclient python-module-netaddr python-module-ntlm python-module-oslo.concurrency python-module-oslo.config python-module-oslo.context python-module-oslo.i18n python-module-oslo.log python-module-oslo.serialization python-module-oslo.utils python-module-paste python-module-pbr python-module-psycopg2 python-module-pyasn1 python-module-pytest python-module-pytz python-module-repoze.lru python-module-requests python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-stevedore python-module-twisted-core python-module-unittest2 python-module-urllib3 python-module-wrapt python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-dns python3-module-docutils python3-module-enum34 python3-module-genshi python3-module-greenlet python3-module-jinja2 python3-module-markupsafe python3-module-mimeparse python3-module-netaddr python3-module-ntlm python3-module-oslo.concurrency python3-module-oslo.config python3-module-oslo.log python3-module-paste python3-module-pbr python3-module-pip python3-module-psycopg2 python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-repoze.lru python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-unittest2 python3-module-wrapt
BuildRequires: python-module-alabaster python-module-html5lib python-module-oslo.service python-module-oslosphinx python-module-retrying python3-module-html5lib python3-module-jinja2-tests python3-module-oslo.service rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 1.6
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-babel
#BuildRequires: python-module-eventlet >= 0.17.4
#BuildRequires: python-module-oslo.concurrency >= 2.3.0
#BuildRequires: python-module-oslo.log >= 1.8.0
#BuildRequires: python-module-oslo.serialization >= 1.4.0
#BuildRequires: python-module-oslo.i18n >= 1.5.0
#BuildRequires: python-module-oslo.service >= 0.7.0
#BuildRequires: python-module-oslo.utils >= 2.0.0
#BuildRequires: python-module-retrying >= 1.2.3
#BuildRequires: python-module-six >= 1.9.0


%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 1.6
#BuildRequires: python3-module-eventlet >= 0.17.4
#BuildRequires: python3-module-oslo.concurrency >= 2.3.0
#BuildRequires: python3-module-oslo.log >= 1.8.0
#BuildRequires: python3-module-oslo.serialization >= 1.4.0
#BuildRequires: python3-module-oslo.i18n >= 1.5.0
#BuildRequires: python3-module-oslo.service >= 0.7.0
#BuildRequires: python3-module-oslo.utils >= 2.0.0
#BuildRequires: python3-module-retrying >= 1.2.3
#BuildRequires: python3-module-six >= 1.9.0
%endif

%description
OpenStack Cinder brick library for managing local volume attaches

%package doc
Summary: Documentation for OpenStack os-brick library
Group: Development/Documentation

%description doc
Documentation for OpenStack os-brick library

%if_with python3
%package -n python3-module-%pypi_name
Summary: OpenStack Cinder brick library for managing local volume attaches
Group: Development/Python3

%description -n python3-module-%pypi_name
OpenStack Cinder brick library for managing local volume attaches

%endif

%prep
%setup
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

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

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

# Move config files to proper location
install -d -m 755 %buildroot%_sysconfdir/%pypi_name/rootwrap.d
mv %buildroot/usr/etc/os-brick/rootwrap.d/*.filters %buildroot%_sysconfdir/%pypi_name/rootwrap.d/

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


%files
%python_sitelibdir/*
%dir %_sysconfdir/%pypi_name
%dir %_sysconfdir/%pypi_name/rootwrap.d
%config(noreplace) %_sysconfdir/%pypi_name/rootwrap.d/*

%files doc
%doc html README.rst

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%dir %_sysconfdir/%pypi_name
%dir %_sysconfdir/%pypi_name/rootwrap.d
%config(noreplace) %_sysconfdir/%pypi_name/rootwrap.d/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- Initial packaging
