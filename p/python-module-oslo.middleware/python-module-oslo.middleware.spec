%define sname oslo.middleware

%def_with python3

Name: python-module-%sname
Version: 2.8.0
Release: alt1.1
Summary: OpenStack oslo.middleware library
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo
Source: %name-%version.tar

BuildArch: noarch

Provides: python-module-oslo-middleware = %EVR
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-flake8 python-module-genshi python-module-hacking python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-ndg-httpsclient python-module-netaddr python-module-ntlm python-module-pbr python-module-pyasn1 python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-stevedore python-module-twisted-core python-module-unittest2 python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-mccabe python3-module-mimeparse python3-module-netaddr python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-unittest2 python3-module-yieldfrom.http.client python3-module-yieldfrom.urllib3 python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-html5lib python-module-oslo.config python-module-oslo.context python-module-oslo.i18n python-module-oslosphinx python-module-pytest python-module-webob python-module-wrapt python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-oslo.config python3-module-wrapt python3-module-yieldfrom.requests rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 1.6
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-six >= 1.9.0
#BuildRequires: python-module-stevedore >= 1.5.0
#BuildRequires: python-module-babel >= 1.3
#BuildRequires: python-module-webob >= 1.2.3
#BuildRequires: python-module-oslo.utils >= 1.2.0
#BuildRequires: python-module-oslo.config >= 2.3.0
#BuildRequires: python-module-oslo.context >= 0.2.0
#BuildRequires: python-module-oslo.i18n >= 1.5.0

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 1.6
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
#BuildRequires: python3-module-six >= 1.9.0
#BuildRequires: python3-module-stevedore >= 1.5.0
#BuildRequires: python3-module-babel >= 1.3
#BuildRequires: python3-module-webob >= 1.2.3
#BuildRequires: python3-module-oslo.utils >= 1.2.0
#BuildRequires: python3-module-oslo.config >= 2.3.0
#BuildRequires: python3-module-oslo.context >= 0.2.0
#BuildRequires: python3-module-oslo.i18n >= 1.5.0

%endif

%description
Oslo middleware library includes components that can be injected into
wsgi pipelines to intercept request/response flows. The base class can be
enhanced with functionality like add/delete/modification of http headers
and support for limiting size/connection etc.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/oslo.middleware
* Source: http://git.openstack.org/cgit/openstack/oslo.middleware
* Bugs: http://bugs.launchpad.net/oslo.middleware


%if_with python3
%package -n python3-module-oslo.middleware
Summary: OpenStack oslo.middleware library
Group: Development/Python3
Provides: python3-module-oslo-middleware = %EVR

%description -n python3-module-oslo.middleware
Oslo middleware library includes components that can be injected into
wsgi pipelines to intercept request/response flows. The base class can be
enhanced with functionality like add/delete/modification of http headers
and support for limiting size/connection etc.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/oslo.middleware
* Source: http://git.openstack.org/cgit/openstack/oslo.middleware
* Bugs: http://bugs.launchpad.net/oslo.middleware
%endif


%package doc
Summary: Documentation for the Oslo middleware handling library
Group: Development/Documentation
Provides: python-module-oslo-middleware-doc = %EVR

%description doc
Documentation for the Oslo middleware handling library.

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
%files -n python3-module-oslo.middleware
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.8.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- Initial release
