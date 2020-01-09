%define oname oslo.rootwrap

Name: python3-module-%oname
Version: 5.17.1
Release: alt1
Summary: Oslo Rootwrap

Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Source1: oslo.rootwrap.watch

BuildArch:      noarch

Provides: python3-module-oslo-rootwrap = %EVR
Obsoletes: python3-module-oslo-rootwrap < %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0

BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-mock >= 2.0.0
BuildRequires: python3-module-fixtures >= 3.0.0

%description
The Oslo Rootwrap allows fine filtering of shell commands to run as `root`
from OpenStack services.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for the Oslo rootwrap handling library
Group: Development/Documentation
Provides: python-module-oslo-rootwrap-doc = %EVR

%description doc
Documentation for the Oslo rootwrap handling library.


%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info

%build
%python3_build

# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/*
%_bindir/oslo-rootwrap
%_bindir/oslo-rootwrap-daemon
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc html

%changelog
* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 5.17.1-alt1
- Automatically updated to 5.17.1.
- Added watch file.
- Renamed spec file.
- Build without python2.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 5.16.1-alt1
- Automatically updated to 5.16.1.

* Sun Aug 18 2019 Grigory Ustinov <grenka@altlinux.org> 5.16.0-alt1
- Automatically updated to 5.16.0

* Sat Dec 08 2018 Alexey Shabalin <shaba@altlinux.org> 5.14.1-alt1
- 5.14.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 5.4.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.1-alt1
- 5.4.1
- add test packages

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 5.1.1-alt1
- 5.1.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 5.1.0-alt1
- 5.1.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 4.1.0-alt1
- 4.1.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0
- rename package from python-module-oslo-rootwrap to python-module-oslo.rootwrap
- add python3 package

* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.0-alt1
- First build for ALT
