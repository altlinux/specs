%define oname osprofiler

Name: python3-module-%oname
Version: 2.9.0
Release: alt1
Summary: OpenStack cross-project profiling library
Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-prettytable >= 0.7.2
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-webob >= 1.6.0
BuildRequires: python3-module-oslo.messaging >= 5.2.0
BuildRequires: python3-module-oslo.log >= 3.11.0
BuildRequires: python3-module-oslo.config >= 5.2.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1

%description
OSProfiler is an OpenStack cross-project profiling library.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack cross-project profiling library
Group: Development/Documentation

%description doc
Documentation for OSProfiler is an OpenStack cross-project profiling library.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info

sed -i '/warning-is-error/d' setup.cfg

%build
%python3_build

python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python3_install

%files
%doc AUTHORS ChangeLog LICENSE PKG-INFO README.rst
%python3_sitelibdir/*
%_bindir/%oname
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc doc/build/html

%changelog
* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 2.9.0-alt1
- Automatically updated to 2.9.0.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 2.8.2-alt1
- Automatically updated to 2.8.2.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 2.6.0-alt1
- Automatically updated to 2.6.0

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 2.3.0-alt1
- Updated to 2.3.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Mar 12 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- Initial release
