%define oname tempest
%def_without check
%def_with docs

Name: python3-module-%oname
Version: 32.0.0
Release: alt1.1

Summary: OpenStack Integration Testing

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/tempest

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-jsonschema >= 3.2.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-paramiko >= 2.7.0
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-stestr >= 1.0.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 4.7.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-subunit
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-urllib3 >= 1.21.1
BuildRequires: python3-module-debtcollector >= 1.2.0

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-mock >= 2.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-cryptography >= 2.1
BuildRequires: python3-module-pycodestyle >= 2.0.0
BuildRequires: python3-module-flake8-import-order
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-sphinxcontrib-rsvgconverter
%endif

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

%if_with docs
%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rfv *.egg-info

find -name "*.py" | xargs subst "s|pep8|pycodestyle|"

%build
%pyproject_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%if_with docs
# install man page
install -pDm 644 man/%oname.1 %buildroot%_man1dir/%oname.1
%endif

# Move config files to proper location
install -d -m 755 %buildroot%_sysconfdir/%oname
mv %buildroot/usr/etc/%oname/*.sample %buildroot%_sysconfdir/%oname
mv %buildroot/usr/etc/%oname/allow-list.yaml %buildroot%_sysconfdir/%oname

%check
%__python3 -m stestr --test-path ./tempest/tests run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/check-uuid
%_bindir/skip-tracker
%_bindir/subunit-describe-calls
%_bindir/tempest
%dir %_sysconfdir/%oname
%config(noreplace) %_sysconfdir/%oname/*.sample
%config(noreplace) %_sysconfdir/%oname/allow-list.yaml
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 32.0.0-alt1.1
- Moved on modern pyproject macros.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 32.0.0-alt1
- Automatically updated to 32.0.0.
- Renamed spec file.
- Unified.
- Build without check.

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 19.0.0-alt5
- Drop unneeded BR: python3-module-unittest2.
- Build without docs.

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
