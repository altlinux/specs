%def_with python3
%define sname heatclient

Name: python-module-%sname
Version: 0.8.0
Release: alt1.1.1
Summary: Python API and CLI for OpenStack Heat

Group: Development/Python
License: ASL 2.0
Url: http://pypi.python.org/pypi/python-%sname
Source: %name-%version.tar

BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-debtcollector python-module-docutils python-module-enum34 python-module-flake8 python-module-genshi python-module-hacking python-module-iso8601 python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-monotonic python-module-ndg-httpsclient python-module-netaddr python-module-ntlm python-module-oslo.config python-module-oslo.i18n python-module-oslo.serialization python-module-oslo.utils python-module-pbr python-module-prettytable python-module-pyasn1 python-module-pytest python-module-pytz python-module-requests python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-stevedore python-module-twisted-core python-module-unittest2 python-module-urllib3 python-module-wrapt python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-mccabe python3-module-mimeparse python3-module-ndg-httpsclient python3-module-netaddr python3-module-ntlm python3-module-oslo.config python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-unittest2 python3-module-urllib3 python3-module-wrapt python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-d2to1 python-module-html5lib python-module-keystoneclient python-module-oslosphinx python-module-swiftclient python-module-yaml python3-module-d2to1 python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-keystoneclient python3-module-swiftclient python3-module-yaml rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 1.6
#BuildRequires: python-module-d2to1
#BuildRequires: python-module-argparse
#BuildRequires: python-module-iso8601 >= 0.1.9
#BuildRequires: python-module-prettytable >= 0.7
#BuildRequires: python-module-requests >= 2.5.2
#BuildRequires: python-module-oslo.i18n >= 1.5.0
#BuildRequires: python-module-oslo.serialization >= 1.4.0
#BuildRequires: python-module-oslo.utils >= 2.0.0
#BuildRequires: python-module-six >= 1.9.0
#BuildRequires: python-module-keystoneclient >= 1.6.0
#BuildRequires: python-module-swiftclient >= 2.2.0
#BuildRequires: python-module-yaml >= 3.1.0
#BuildRequires: python-module-babel >= 1.3
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 1.6
#BuildRequires: python3-module-d2to1
#BuildRequires: python3-module-argparse
#BuildRequires: python3-module-iso8601 >= 0.1.9
#BuildRequires: python3-module-prettytable >= 0.7
#BuildRequires: python3-module-requests >= 2.5.2
#BuildRequires: python3-module-oslo.i18n >= 1.5.0
#BuildRequires: python3-module-oslo.serialization >= 1.4.0
#BuildRequires: python3-module-oslo.utils >= 2.0.0
#BuildRequires: python3-module-six >= 1.9.0
#BuildRequires: python3-module-keystoneclient >= 1.6.0
#BuildRequires: python3-module-swiftclient >= 2.2.0
#BuildRequires: python3-module-yaml >= 3.1.0
#BuildRequires: python3-module-babel >= 1.3
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
%endif

%description
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100 percent of
the OpenStack Heat API.

%if_with python3
%package -n python3-module-%sname
Summary:    Python API and CLI for OpenStack Heat
Group: Development/Python3

%description -n python3-module-%sname
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100 percent of
the OpenStack Heat API.
%endif

%package doc
Summary: Documentation for OpenStack Heat API Client
Group: Development/Documentation

%description doc
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100 percent of
the OpenStack Heat API.

This package contains auto-generated documentation.

%prep
%setup

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config.
rm -rf {test-,}requirements.txt tools/{pip,test}-requires
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
mv %buildroot%_bindir/heat %buildroot%_bindir/python3-heat
%endif

%python_install
echo "%version" > %buildroot%python_sitelibdir/heatclient/versioninfo
echo "%version" > %buildroot%python3_sitelibdir/heatclient/versioninfo

# Delete tests
rm -fr %buildroot%python_sitelibdir/heatclient/tests
rm -fr %buildroot%python3_sitelibdir/heatclient/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/heat
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%_bindir/python3-heat
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- 0.3.0
- add python package

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.2.9-alt1
- First build for ALT (based on Fedora 0.2.9-1.fc21.src)

