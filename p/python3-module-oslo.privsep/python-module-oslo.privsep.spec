%define oname oslo.privsep

Name: python3-module-%oname
Version: 1.33.3
Release: alt1
Summary: OpenStack library for privilege separation
Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-greenlet >= 0.4.10
BuildRequires: python3-module-msgpack >= 0.5.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-cffi >= 1.7.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-apidoc

%description
This library helps applications perform actions which require more or less privileges
than they were started with in a safe, easy to code and easy to use manner.
For more information on why this is generally a good idea please read over
the principle of least privilege and the specification which created this library.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Oslo service documentation
Group: Development/Documentation

%description doc
Documentation for %oname

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
%doc README.rst
%python3_sitelibdir/*
%_bindir/privsep-helper
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc html

%changelog
* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.33.3-alt1
- Automatically updated to 1.33.3
- Build without python2.

* Sun Aug 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.33.1-alt1
- Automatically updated to 1.33.1

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 1.29.2-alt1
- 1.29.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.16.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.16.0-alt1
- 1.16.0

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1.13.1-alt1
- 1.13.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.13.0-alt1
- Initial package.
