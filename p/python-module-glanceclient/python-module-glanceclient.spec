%def_with python3

Name: python-module-glanceclient
Version: 1.1.0
Release: alt2.1
Summary: Python API and CLI for OpenStack Glance

Group: Development/Python
License: ASL 2.0
Url: http://github.com/openstack/python-glanceclient
Source: %name-%version.tar
Patch1: fix-alt-urllib3.patch

BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-debtcollector python-module-docutils python-module-enum34 python-module-flake8 python-module-functools32 python-module-genshi python-module-hacking python-module-iso8601 python-module-jinja2 python-module-jinja2-tests python-module-jsonpatch python-module-jsonpointer python-module-jsonschema python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-monotonic python-module-ndg-httpsclient python-module-netaddr python-module-netifaces python-module-ntlm python-module-oslo.config python-module-oslo.i18n python-module-oslo.serialization python-module-oslo.utils python-module-pbr python-module-prettytable python-module-pyasn1 python-module-pytest python-module-pytz python-module-requests python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-stevedore python-module-twisted-core python-module-unittest2 python-module-urllib3 python-module-wrapt python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-mccabe python3-module-mimeparse python3-module-ndg-httpsclient python3-module-netaddr python3-module-ntlm python3-module-oslo.config python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-unittest2 python3-module-urllib3 python3-module-wrapt python3-module-yieldfrom.http.client python3-pyflakes python3-tools-pep8 xz
BuildRequires: python-module-alabaster python-module-html5lib python-module-keystoneclient python-module-oslosphinx python-module-warlock python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-jsonpointer python3-module-jsonschema python3-module-keystoneclient python3-module-yieldfrom.urllib3 rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 1.6
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-babel >= 1.3
#BuildRequires: python-module-argparse
#BuildRequires: python-module-prettytable
#BuildRequires: python-module-keystoneclient >= 1.6.0
#BuildRequires: python-module-OpenSSL >= 0.11
#BuildRequires: python-module-requests >= 2.5.0
#BuildRequires: python-module-warlock >= 1.0.1
#BuildRequires: python-module-six >= 1.9.0
#BuildRequires: python-module-oslo.i18n >= 1.5.0
#BuildRequires: python-module-oslo.utils >= 2.0.0

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 1.6
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
#BuildRequires: python3-module-babel >= 1.3
#BuildRequires: python3-module-argparse
#BuildRequires: python3-module-prettytable
#BuildRequires: python3-module-keystoneclient >= 1.6.0
#BuildRequires: python3-module-OpenSSL >= 0.11
#BuildRequires: python3-module-requests >= 2.5.0
#BuildRequires: python3-module-warlock >= 1.0.1
#BuildRequires: python3-module-six >= 1.9.0
#BuildRequires: python3-module-oslo.i18n >= 1.5.0
#BuildRequires: python3-module-oslo.utils >= 2.0.0
%endif

%description
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100 percent of the OpenStack Glance API.

%if_with python3
%package -n python3-module-glanceclient
Summary: Python API and CLI for OpenStack Glance
Group: Development/Python3

%description -n python3-module-glanceclient
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100 percent of the OpenStack Glance API.
%endif

%package doc
Summary: Documentation for OpenStack Glance API Client
Group: Development/Documentation

%description doc
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100 percent of the OpenStack Glance API.

This package contains auto-generated documentation.

%prep
%setup
%patch1 -p1

# Remove bundled egg-info
rm -rf python_glanceclient.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py
rm -rf {,test-}requirements.txt

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
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/glance %buildroot%_bindir/python3-glance
%endif

%python_install

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# generate man page
sphinx-build -b man doc/source man
install -p -D -m 644 man/glance.1 %buildroot%_mandir/man1/glance.1

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%doc LICENSE
%_bindir/glance
%python_sitelibdir/*
%_man1dir/glance*

%if_with python3
%files -n python3-module-glanceclient
%_bindir/python3-glance
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt2.1
- NMU: Use buildreq for BR.

* Tue Nov 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt2
- fix work with system urllib3

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 0.17.2-alt1
- 0.17.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.16.1-alt1
- 0.16.1
- add python3 package

* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 0.12.0-alt1
- First build for ALT (based on Fedora 0.12.0-1.fc20.src)

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.4.1-alt1
- Initial release for Sisyphus (based on Fedora)

