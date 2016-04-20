%def_with python3

Name: python-module-neutronclient
Version: 4.1.2
Release: alt1
Summary: Python API and CLI for OpenStack Neutron
Group: Development/Python

License: ASL 2.0
Url: http://launchpad.net/python-neutronclient/
Source: %name-%version.tar

Provides: python-module-quantumclient
Obsoletes: python-module-quantumclient

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-cliff >= 1.15.0
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-iso8601 >= 0.1.9
BuildRequires: python-module-netaddr >= 0.7.12
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.5.0
BuildRequires: python-module-os-client-config >= 1.13.1
BuildRequires: python-module-keystoneauth1 >= 2.1.0
BuildRequires: python-module-requests >= 2.8.1
BuildRequires: python-module-simplejson >= 2.2.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-babel >= 1.3


%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-argparse
BuildRequires: python3-module-cliff >= 1.15.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-iso8601 >= 0.1.9
BuildRequires: python3-module-netaddr >= 0.7.12
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.5.0
BuildRequires: python3-module-os-client-config >= 1.13.1
BuildRequires: python3-module-keystoneauth1 >= 2.1.0
BuildRequires: python3-module-requests >= 2.8.1
BuildRequires: python3-module-simplejson >= 2.2.0
BuildRequires: python3-module-babel >= 1.3
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

# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

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
%doc doc/build/html

%changelog
* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 4.1.2-alt1
- 4.1.2

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 3.1.1-alt1
- 3.1.1

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
