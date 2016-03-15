%define pypi_name oslo.cache

%def_with python3

Name: python-module-%pypi_name
Version: 0.5.0
Release: alt1.1.1
Summary: Cache storage for Openstack projects

Group: Development/Python
License: ASL 2.0
URL: https://launchpad.net/oslo
Source: %name-%version.tar
BuildArch:      noarch


# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-beaker python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-docutils python-module-ecdsa python-module-ed25519 python-module-enum34 python-module-flake8 python-module-genshi python-module-hacking python-module-jinja2 python-module-jinja2-tests python-module-lingua python-module-mako python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-ndg-httpsclient python-module-netaddr python-module-nss python-module-ntlm python-module-oslo.config python-module-pbr python-module-polib python-module-pyasn1 python-module-pycrypto python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-stevedore python-module-twisted-core python-module-unittest2 python-module-wrapt python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-beaker python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-lingua python3-module-mako python3-module-markupsafe python3-module-mccabe python3-module-mimeparse python3-module-netaddr python3-module-ntlm python3-module-oslo.config python3-module-pbr python3-module-pip python3-module-polib python3-module-pycparser python3-module-pycrypto python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-unittest2 python3-module-wrapt python3-module-yieldfrom.http.client python3-module-yieldfrom.urllib3 python3-module-zope python3-module-zope.interface python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-dogpile.cache python-module-html5lib python-module-oslo.log python-module-oslosphinx python3-module-dogpile.cache python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-oslo.log python3-module-yieldfrom.requests rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 1.6
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-dogpile.cache >= 0.5.4
#BuildRequires: python-module-six >= 1.9.0
#BuildRequires: python-module-oslo.config >= 2.3.0
#BuildRequires: python-module-oslo.i18n >= 1.5.0
#BuildRequires: python-module-oslo.log >= 1.8.0
#BuildRequires: python-module-oslo.utils >= 2.0.0


%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 1.6
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
#BuildRequires: python3-module-dogpile.cache >= 0.5.4
#BuildRequires: python3-module-six >= 1.9.0
#BuildRequires: python3-module-oslo.config >= 2.3.0
#BuildRequires: python3-module-oslo.i18n >= 1.5.0
#BuildRequires: python3-module-oslo.log >= 1.8.0
#BuildRequires: python3-module-oslo.utils >= 2.0.0
%endif

%description
Cache storage for Openstack projects.

%if_with python3
%package -n python3-module-%pypi_name
Summary: Cache storage for Openstack projects.
Group: Development/Python3

%description -n python3-module-%pypi_name
Cache storage for Openstack projects.
%endif

%package doc
Summary: Documentation for Cache storage for Openstack projects
Group: Development/Documentation

%description doc
Documentation for Cache storage for Openstack projects.


%prep
%setup

# Remove bundled egg-info
rm -rf %pypi_name.egg-info

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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%endif

%files doc
%doc html
%doc README.rst LICENSE

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- First build for ALT
