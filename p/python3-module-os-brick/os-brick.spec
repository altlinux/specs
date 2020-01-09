%define oname os-brick

Name: python3-module-%oname
Version: 2.11.0
Release: alt1
Summary: OpenStack Cinder brick library for managing local volume attaches
Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Source1: os-brick.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.privsep >= 1.32.0
BuildRequires: python3-module-oslo.service >= 1.24.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-retrying >= 1.2.3
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-os-win >= 3.0.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 0.8.0
BuildRequires: python3-module-openstackdocstheme

%description
OpenStack Cinder brick library for managing local volume attaches

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack os-brick library
Group: Development/Documentation

%description doc
Documentation for OpenStack os-brick library

%prep
%setup -n %oname-%version
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

sed -i '/warning-is-error/d' setup.cfg

%build
%python3_build

python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python3_install

# Move config files to proper location
install -d -m 755 %buildroot%_sysconfdir/%oname/rootwrap.d
mv %buildroot/usr/etc/os-brick/rootwrap.d/*.filters %buildroot%_sysconfdir/%oname/rootwrap.d/

%files
%python3_sitelibdir/*
%dir %_sysconfdir/%oname
%dir %_sysconfdir/%oname/rootwrap.d
%config(noreplace) %_sysconfdir/%oname/rootwrap.d/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc README.rst doc/build/html

%changelog
* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 2.11.0-alt1
- Automatically updated to 2.11.0.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 2.10.0-alt1
- Automatically updated to 2.10.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 2.8.2-alt1
- Automatically updated to 2.8.2

* Tue Dec 18 2018 Alexey Shabalin <shaba@altlinux.org> 2.5.4-alt1
- 2.5.4

* Fri Oct 05 2018 Grigory Ustinov <grenka@altlinux.org> 2.5.3-alt1
- Autoupdated to 2.5.3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.11.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- Initial packaging
