%define oname blazarclient

Name:       python3-module-%oname
Version:    2.2.1
Release:    alt1

Summary:    Client for OpenStack Reservation Service

Group:      Development/Python3
License:    ASL 2.0
Url:        http://docs.openstack.org/developer/%oname

Source:     https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0

%description
This is a client for the OpenStack Blazar API. It provides a Python API (the
blazarclient module) and a command-line script (blazar).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup -n python-%oname-%version

# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE
%_bindir/blazar
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 2.2.1-alt1
- Automatically updated to 2.2.1.
- Build without python2.
- Cleanup spec.

* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 2.0.1-alt1
- Initial build.
