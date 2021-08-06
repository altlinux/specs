%define oname tempest

Name: python3-module-%oname
Version: 19.0.0
Release: alt4
Summary: OpenStack Integration Testing Suite

Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-jsonschema >= 2.6.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-paramiko >= 2.0
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-stestr >= 1.0.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-subunit
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-urllib3 >= 1.21.1
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-unittest2

# for build doc and tests
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-hacking >= 0.11.0
BuildRequires: python3-module-mock >= 2.0
BuildRequires: python3-module-coverage >= 3.6
BuildRequires: python3-module-oslotest >= 1.10.0

%description
This is a set of integration tests to be run against a live OpenStack
cluster. Tempest has batteries of tests for OpenStack API validation,
Scenarios, and other specific tests useful in validating an OpenStack
deployment.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Integration Testing Suite
Group: Development/Documentation

%description doc
Documentation for OpenStack Integration Testing Suite.

%prep
%setup -n %oname-%version

find -name "*.py" | xargs subst "s|pep8|pycodestyle|"

# Remove bundled egg-info
rm -rf %{oname}.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%python3_build

python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr build/sphinx/html/.buildinfo

%install
%python3_install
mkdir -p %buildroot%_sysconfdir/tempest
mv %buildroot/usr/etc/tempest/* %buildroot%_sysconfdir/tempest/
rm -rf %buildroot/usr/etc/tempest

%files
%doc README.rst LICENSE ChangeLog
%_sysconfdir/tempest
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%files doc
%doc build/sphinx/html

%changelog
* Fri Aug 06 2021 Vitaly Lipatov <lav@altlinux.ru> 19.0.0-alt4
- replace pep8 with pycodestyle

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 19.0.0-alt3
- drop unneeded BR: python3-module-subunit-tests

* Fri Oct 25 2019 Grigory Ustinov <grenka@altlinux.org> 19.0.0-alt2
- Build without python2.

* Tue Dec 11 2018 Alexey Shabalin <shaba@altlinux.org> 19.0.0-alt1
- 19.0.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 15.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 15.0.0-alt1
- initial build
