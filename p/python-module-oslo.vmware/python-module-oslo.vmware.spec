%define sname oslo.vmware
%def_with python3

Name: python-module-%sname
Version: 1.21.0
Release: alt1.1.1
Summary: Oslo VMware library for OpenStack projects
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo
Source: %name-%version.tar

Provides: python-module-oslo-vmware = %EVR

BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-flake8 python-module-genshi python-module-hacking python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-ndg-httpsclient python-module-netaddr python-module-ntlm python-module-oslo.config python-module-pbr python-module-pyasn1 python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-stevedore python-module-twisted-core python-module-unittest2 python-module-wrapt python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-mccabe python3-module-mimeparse python3-module-ndg-httpsclient python3-module-netaddr python3-module-ntlm python3-module-oslo.config python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-unittest2 python3-module-wrapt python3-module-yieldfrom.http.client python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-d2to1 python-module-dns python-module-greenlet python-module-html5lib python-module-oslo.concurrency python-module-oslosphinx python-module-psycopg2 python3-module-chardet python3-module-d2to1 python3-module-dns python3-module-greenlet python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-oslo.concurrency python3-module-psycopg2 python3-module-urllib3 python3-module-yieldfrom.urllib3 rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 1.6
#BuildRequires: python-module-d2to1
#BuildRequires: python-module-six >= 1.9.0
#BuildRequires: python-module-babel >= 1.3
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-stevedore >= 1.5.0
#BuildRequires: python-module-netaddr >= 0.7.12
#BuildRequires: python-module-iso8601 >= 0.1.9
#BuildRequires: python-module-oslo.i18n >= 1.5.0
#BuildRequires: python-module-oslo.utils >= 2.0.0
#BuildRequires: python-module-oslo.serialization >= 1.2.0
#BuildRequires: python-module-oslo.concurrency >= 2.3.0
#BuildRequires: python-module-suds-jurko >= 0.6
#BuildRequires: python-module-eventlet >= 0.17.4
#BuildRequires: python-module-requests >= 2.5.0
#BuildRequires: python-module-urllib3 >= 1.8.3

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 1.6
#BuildRequires: python3-module-d2to1
#BuildRequires: python3-module-six >= 1.9.0
#BuildRequires: python3-module-babel >= 1.3
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
#BuildRequires: python3-module-stevedore >= 1.5.0
#BuildRequires: python3-module-netaddr >= 0.7.12
#BuildRequires: python3-module-iso8601 >= 0.1.9
#BuildRequires: python3-module-oslo.i18n >= 1.5.0
#BuildRequires: python3-module-oslo.utils >= 2.0.0
#BuildRequires: python3-module-oslo.serialization >= 1.2.0
#BuildRequires: python3-module-oslo.concurrency >= 2.3.0
#BuildRequires: python3-module-suds-jurko >= 0.6
#BuildRequires: python3-module-eventlet >= 0.17.4
#BuildRequires: python3-module-requests >= 2.5.0
#BuildRequires: python3-module-urllib3 >= 1.8.3
%endif

%description
The Oslo project intends to produce a python library containing infrastructure
code shared by OpenStack projects. The APIs provided by the project should be
high quality, stable, consistent and generally useful.

The Oslo VMware library offers session and API call management for VMware ESX/VC
server.

%if_with python3
%package -n python3-module-%sname
Summary: Oslo VMware library for OpenStack projects
Group: Development/Python3
Provides: python3-module-oslo-vmware = %EVR

%description -n python3-module-%sname
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application
or library.
%endif

%package doc
Summary: Documentation for OpenStack common VMware library
Group: Development/Documentation

%description doc
Documentation for OpenStack common VMware library.

%prep
%setup

# Remove bundled egg-info
#rm -rf %sname.egg-info
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
%doc README.rst LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.21.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.21.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.21.0-alt1
- 1.21.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- initial build
