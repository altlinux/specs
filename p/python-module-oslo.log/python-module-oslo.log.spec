%define sname oslo.log

%def_with python3

Name: python-module-%sname
Version: 1.11.0
Release: alt1.1
Summary: OpenStack oslo.log library
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo
Source: %name-%version.tar

BuildArch: noarch

Provides: python-module-oslo-log = %EVR
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-extras python-module-fixtures python-module-flake8 python-module-genshi python-module-hacking python-module-iso8601 python-module-jinja2 python-module-jinja2-tests python-module-linecache2 python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-monotonic python-module-ndg-httpsclient python-module-netaddr python-module-ntlm python-module-oslo.i18n python-module-oslo.utils python-module-pbr python-module-pyasn1 python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-stevedore python-module-testtools python-module-traceback2 python-module-twisted-core python-module-unittest2 python-module-wrapt python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-mccabe python3-module-mimeparse python3-module-netaddr python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-unittest2 python3-module-yieldfrom.http.client python3-module-yieldfrom.urllib3 python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-debtcollector python-module-html5lib python-module-oslo.config python-module-oslo.context python-module-oslo.serialization python-module-oslosphinx python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-oslo.config python3-module-wrapt python3-module-yieldfrom.requests rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 1.6
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-babel >= 1.3
#BuildRequires: python-module-six >= 1.9.0
#BuildRequires: python-module-iso8601 >= 0.1.9
#BuildRequires: python-module-oslo.config >= 2.3.0
#BuildRequires: python-module-oslo.context >= 0.2.0
#BuildRequires: python-module-oslo.i18n >= 1.5.0
#BuildRequires: python-module-oslo.utils >= 2.0.0
#BuildRequires: python-module-oslo.serialization >= 1.4.0
#BuildRequires: python-module-debtcollector >= 0.3.0


%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 1.6
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
#BuildRequires: python3-module-babel >= 1.3
#BuildRequires: python3-module-six >= 1.9.0
#BuildRequires: python3-module-iso8601 >= 0.1.9
#BuildRequires: python3-module-oslo.config >= 2.3.0
#BuildRequires: python3-module-oslo.context >= 0.2.0
#BuildRequires: python3-module-oslo.i18n >= 1.5.0
#BuildRequires: python3-module-oslo.utils >= 2.0.0
#BuildRequires: python3-module-oslo.serialization >= 1.4.0
#BuildRequires: python3-module-debtcollector >= 0.3.0
%endif

%description
OpenStack logging configuration library provides standardized configuration for
all openstack projects. It also provides custom formatters, handlers and
support for context specific logging (like resource id's etc).

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/oslo.log
* Source: http://git.openstack.org/cgit/openstack/oslo.log
* Bugs: http://bugs.launchpad.net/oslo.log

%if_with python3
%package -n python3-module-%sname
Summary: OpenStack oslo.log library
Group: Development/Python3
Provides: python3-module-oslo-log = %EVR

%description -n python3-module-%sname
OpenStack logging configuration library provides standardized configuration for
all openstack projects. It also provides custom formatters, handlers and
support for context specific logging (like resource id's etc).

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/oslo.log
* Source: http://git.openstack.org/cgit/openstack/oslo.log
* Bugs: http://bugs.launchpad.net/oslo.log
%endif


%package doc
Summary: Documentation for the Oslo log handling library
Group: Development/Documentation
Provides: python-module-oslo-log-doc = %EVR

%description doc
Documentation for the Oslo log handling library.

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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.11.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- Initial release
