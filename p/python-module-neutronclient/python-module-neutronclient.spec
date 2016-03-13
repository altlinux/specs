%def_with python3

Name: python-module-neutronclient
Version: 3.1.0
Release: alt1.1.1
Summary: Python API and CLI for OpenStack Neutron
Group: Development/Python

License: ASL 2.0
Url: http://launchpad.net/python-neutronclient/
Source: %name-%version.tar

Provides: python-module-quantumclient
Obsoletes: python-module-quantumclient

BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cmd2 python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-flake8 python-module-genshi python-module-hacking python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-ndg-httpsclient python-module-netaddr python-module-ntlm python-module-oslo.config python-module-pbr python-module-pyasn1 python-module-pyparsing python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-stevedore python-module-twisted-core python-module-unittest2 python-module-wrapt python-module-yaml python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-mccabe python3-module-mimeparse python3-module-ndg-httpsclient python3-module-netaddr python3-module-ntlm python3-module-oslo.config python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-unittest2 python3-module-urllib3 python3-module-wrapt python3-module-yaml python3-module-yieldfrom.http.client python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-cliff python-module-html5lib python-module-keystoneclient python-module-oslosphinx python3-module-cliff python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-keystoneclient python3-module-yieldfrom.urllib3 rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 1.6
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-babel >= 1.3
#BuildRequires: python-module-six >= 1.9.0
#BuildRequires: python-module-argparse
#BuildRequires: python-module-cliff >= 1.14.0
#BuildRequires: python-module-iso8601 >= 0.1.9
#BuildRequires: python-module-netaddr >= 0.7.12
#BuildRequires: python-module-oslo.i18n >= 1.5.0
#BuildRequires: python-module-oslo.serialization >= 1.4.0
#BuildRequires: python-module-oslo.utils >= 2.0.0
#BuildRequires: python-module-requests >= 2.5.2
#BuildRequires: python-module-keystoneclient >= 1.6.0
#BuildRequires: python-module-simplejson >= 2.2.0
#BuildRequires: python-module-babel >= 1.3

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 1.6
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
#BuildRequires: python3-module-argparse
#BuildRequires: python3-module-cliff >= 1.14.0
#BuildRequires: python3-module-iso8601 >= 0.1.9
#BuildRequires: python3-module-netaddr >= 0.7.12
#BuildRequires: python3-module-oslo.i18n >= 1.5.0
#BuildRequires: python3-module-oslo.serialization >= 1.4.0
#BuildRequires: python3-module-oslo.utils >= 2.0.0
#BuildRequires: python3-module-requests >= 2.5.2
#BuildRequires: python3-module-keystoneclient >= 1.6.0
#BuildRequires: python3-module-simplejson >= 2.2.0
#BuildRequires: python3-module-babel >= 1.3
%endif

%description
Client library and command line utility for interacting with Openstack
Neutron's API.

%if_with python3
%package -n python3-module-neutronclient
Summary: Python API and CLI for OpenStack Neutron
Group: Development/Python3

%description -n python3-module-neutronclient
Client library and command line utility for interacting with Openstack
Neutron's API.
%endif

%package doc
Summary: Documentation for OpenStack Neutron API Client
Group: Development/Documentation

%description doc
Client library and command line utility for interacting with Openstack
Neutron's API.

This package contains auto-generated documentation.


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
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/neutron %buildroot%_bindir/python3-neutron
%endif

%python_install

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Install other needed files
install -p -D -m 644 tools/neutron.bash_completion \
    %buildroot%_sysconfdir/bash_completion.d/neutron.bash_completion

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc LICENSE
%doc README.rst
%_bindir/neutron
%python_sitelibdir/*
%_sysconfdir/bash_completion.d

%if_with python3
%files -n python3-module-neutronclient
%_bindir/python3-neutron
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.1.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 3.1.0-alt1
- 3.1.0

* Wed Oct 14 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.12-alt1
- 2.3.12 (no changes)

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.11-alt1
- 2.3.11
- add python3 package

* Fri Aug 15 2014 Lenar Shakirov <snejok@altlinux.ru> 2.3.4-alt2
- Provides/Obsoletes: python-module-quantumclient added

* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 2.3.4-alt1
- First build for ALT (based on Fedora 2.3.4-1.fc21.src)
