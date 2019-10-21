%define oname neutronclient

Name: python3-module-%oname
Version: 6.14.0
Release: alt1

Summary: Python API and CLI for OpenStack Neutron

Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/python-%oname

Source: https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-os-client-config >= 1.28.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-keystoneclient >= 3.8.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-simplejson >= 3.5.1
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-babel >= 2.3.4

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0

%description
Client library and command line utility for interacting with Openstack
Neutron's API.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Neutron API Client
Group: Development/Documentation

%description doc
Client library and command line utility for interacting with Openstack
Neutron's API.

This package contains auto-generated documentation.

%prep
%setup -n python-%oname-%version

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%build
%python3_build

%install
%python3_install

python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

# Install other needed files
install -p -D -m 644 tools/neutron.bash_completion \
    %buildroot%_sysconfdir/bash_completion.d/neutron.bash_completion

rm -rf %buildroot%python_sitelibdir/*/tests/functional/hooks
rm -rf %buildroot%python3_sitelibdir/*/tests/functional/hooks

%files
%doc LICENSE
%doc README.rst
%_bindir/neutron
%python3_sitelibdir/*
%_sysconfdir/bash_completion.d
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc build/sphinx/html

%changelog
* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 6.14.0-alt1
- Automatically updated to 6.14.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 6.12.0-alt1
- Automatically updated to 6.12.0

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 6.9.1-alt1
- 6.9.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 6.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 6.1.0-alt1
- 6.1.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 6.0.0-alt1
- 6.0.0

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
