%define oname openstacksdk
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 1.0.1
Release: alt1

Summary: An SDK for building applications to work with OpenStack

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/openstacksdk

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-yaml >= 3.13
BuildRequires: python3-module-appdirs >= 1.3.0
BuildRequires: python3-module-requestsexceptions >= 1.2.0
BuildRequires: python3-module-jsonpatch >= 1.16
BuildRequires: python3-module-os-service-types >= 1.7.0
BuildRequires: python3-module-keystoneauth1 >= 3.18.0
BuildRequires: python3-module-munch >= 2.1.0
BuildRequires: python3-module-decorator >= 4.4.1
BuildRequires: python3-module-jmespath >= 0.9.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-netifaces >= 0.10.4
BuildRequires: python3-module-dogpile.cache >= 0.6.5
BuildRequires: python3-module-cryptography >= 2.7

%if_with check
BuildRequires: python3-module-hacking >= 3.1.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-ddt >= 1.0.1
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-jsonschema >= 3.2.0
BuildRequires: python3-module-oslo.config >= 6.1.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-statsd >= 3.3.0
BuildRequires: python3-module-stestr >= 1.0.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-prometheus_client
BuildRequires: python3-module-requests-mock >= 1.2.0
%endif

%if_with docs
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-rsvgconverter
%endif

%description
The openstacksdk is a client library for building applications to work with
OpenStack clouds. The project aims to provide a consistent and complete set of
interactions with OpenStack's many services, along with complete documentation,
examples, and tools.

It also contains an abstraction interface layer. Clouds can do many things,
but there are probably only about 10 of them that most people care about
with any regularity. If you want to do complicated things, the per-service
oriented portions of the SDK are for you. However, if what you want is
to be able to write an application that talks to any OpenStack cloud regardless
of configuration, then the Cloud Abstraction layer is for you.

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

%build
%python3_build

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
%python3_install

%if_with docs
# install man page
install -pDm 644 man/%oname.1 %buildroot%_man1dir/%oname.1
%endif

# Install missing files to proper location
cp openstack/config/*.json %buildroot%python3_sitelibdir/openstack/config

%check
export OS_LOG_CAPTURE=true
export OS_TEST_TIMEOUT=30
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/openstack-inventory
%python3_sitelibdir/openstack
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/openstack/tests

%files tests
%python3_sitelibdir/openstack/tests
%exclude %python3_sitelibdir/openstack/tests/functional/examples

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Automatically updated to 1.0.1.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.102.0-alt2
- Fixed build with check.

* Sat Oct 22 2022 Grigory Ustinov <grenka@altlinux.org> 0.102.0-alt1
- Automatically updated to 0.102.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 0.101.0-alt2
- Spec refactoring.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 0.101.0-alt1
- Automatically updated to 0.101.0.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 0.61.0-alt1
- Automatically updated to 0.61.0.
- Unified (thx for felixz@).
- Build without check.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 0.46.0-alt1
- Automatically updated to 0.46.0.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 0.36.0-alt1
- Automatically updated to 0.36.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 0.27.0-alt1
- Automatically updated to 0.27.0

* Wed Jan 30 2019 Alexey Shabalin <shaba@altlinux.org> 0.17.2-alt2
- package configs: defaults.json, schema.json, vendor-schema.json

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 0.17.2-alt1
- 0.17.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.13-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 0.9.13-alt1
- 0.9.13
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 0.9.8-alt1
- initial build
