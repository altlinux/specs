%define oname tempest
%def_with python3

Name: python-module-%oname
Version: 15.0.0
Release: alt1.1
Summary: OpenStack Integration Testing Suite

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-six >= 1.9.0

BuildRequires: python-module-cliff >= 2.3.0
BuildRequires: python-module-jsonschema >= 2.5.0
BuildRequires: python-module-testtools >= 1.4.0
BuildRequires: python-module-paramiko >= 2.0
BuildRequires: python-module-netaddr >= 0.7.13
BuildRequires: python-module-testrepository >= 0.0.18
BuildRequires: python-module-oslo.concurrency >= 3.8.0
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.log >= 3.11.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-fixtures >= 3.0.0
BuildRequires: python-module-testscenarios >= 0.4
BuildRequires: python-module-yaml >= 3.10.0
BuildRequires: python-module-subunit python-module-subunit-tests
BuildRequires: python-module-stevedore >= 1.17.1
BuildRequires: python-module-prettytable >= 0.7.1
BuildRequires: python-module-os-testr >= 0.8.0
BuildRequires: python-module-urllib3 >= 1.15.1
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-unittest2

# for build doc and tests
BuildRequires: python-module-hacking >= 0.11.0
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-mock >= 2.0
BuildRequires: python-module-coverage >= 3.6
BuildRequires: python-module-oslotest >= 1.10.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-cliff >= 2.3.0
BuildRequires: python3-module-jsonschema >= 2.5.0
BuildRequires: python3-module-testtools >= 1.4.0
BuildRequires: python3-module-paramiko >= 2.0
BuildRequires: python3-module-netaddr >= 0.7.13
BuildRequires: python3-module-testrepository >= 0.0.18
BuildRequires: python3-module-oslo.concurrency >= 3.8.0
BuildRequires: python3-module-oslo.config >= 3.14.0
BuildRequires: python3-module-oslo.log >= 3.11.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.18.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-yaml >= 3.10.0
BuildRequires: python3-module-subunit python3-module-subunit-tests
BuildRequires: python3-module-stevedore >= 1.17.1
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-os-testr >= 0.8.0
BuildRequires: python3-module-urllib3 >= 1.15.1
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-unittest2
%endif

%description
This is a set of integration tests to be run against a live OpenStack
cluster. Tempest has batteries of tests for OpenStack API validation,
Scenarios, and other specific tests useful in validating an OpenStack
deployment.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Integration Testing Suite
Group: Development/Documentation

%description doc
Documentation for OpenStack Integration Testing Suite.

%package -n python3-module-%oname
Summary: OpenStack Integration Testing Suite
Group: Development/Python3

%description -n python3-module-%oname
This is a set of integration tests to be run against a live OpenStack
cluster. Tempest has batteries of tests for OpenStack API validation,
Scenarios, and other specific tests useful in validating an OpenStack
deployment.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %{oname}.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

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

# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/check-uuid %buildroot%_bindir/check-uuid.py3
mv %buildroot%_bindir/skip-tracker %buildroot%_bindir/skip-tracker.py3
mv %buildroot%_bindir/subunit-describe-calls %buildroot%_bindir/subunit-describe-calls.py3
mv %buildroot%_bindir/tempest %buildroot%_bindir/tempest.py3
mv %buildroot%_bindir/tempest-account-generator %buildroot%_bindir/tempest-account-generator.py3
mv %buildroot%_bindir/verify-tempest-config %buildroot%_bindir/verify-tempest-config.py3
popd
%endif
%python_install
mkdir -p %buildroot%_sysconfdir/tempest
mv %buildroot/usr/etc/tempest/* %buildroot%_sysconfdir/tempest/

%files
%doc README.rst LICENSE ChangeLog
%_sysconfdir/tempest
%_bindir/*
%exclude %_bindir/*.py3
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%files doc
%doc doc/build/html

%if_with python3
%files -n python3-module-%oname
%_sysconfdir/tempest
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 15.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 15.0.0-alt1
- initial build