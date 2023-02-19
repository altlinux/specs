%define oname os-vif
%def_without check
%def_with docs

Name: python3-module-%oname
Version: 3.0.0
Release: alt3.1

Summary: A library for plugging and unplugging virtual interfaces in OpenStack

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/os-vif

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-oslo.concurrency >= 3.20.0
BuildRequires: python3-module-oslo.config >= 5.1.0
BuildRequires: python3-module-oslo.log >= 3.30.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.privsep >= 1.23.0
BuildRequires: python3-module-oslo.versionedobjects >= 1.28.0
BuildRequires: python3-module-ovsdbapp >= 0.12.1
BuildRequires: python3-module-pyroute2 >= 0.5.2
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-debtcollector >= 1.19.0

%if_with check
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-oslotest >= 1.10.0
BuildRequires: python3-module-openvswitch >= 2.9.2
BuildRequires: python3-module-stestr >= 1.0.0
BuildRequires: python3-module-testscenarios >= 0.4
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 2.0.0
BuildRequires: python3-module-reno >= 1.8.0
BuildRequires: python3-module-openstackdocstheme >= 2.2.1
%endif

%description
A library for plugging and unplugging virtual interfaces in OpenStack.
Features:
- A base VIF plugin class that supplies a plug() and unplug() interface
- Versioned objects that represent a virtual interface and its components

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
install -pDm 644 man/os_vif.1 %buildroot%_man1dir/%oname.1
%endif

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/os_vif
%python3_sitelibdir/vif_plug_linux_bridge
%python3_sitelibdir/vif_plug_noop
%python3_sitelibdir/vif_plug_ovs
%python3_sitelibdir/os_vif-%version.dist-info
%exclude %python3_sitelibdir/os_vif/tests
%exclude %python3_sitelibdir/vif_plug_linux_bridge/tests
%exclude %python3_sitelibdir/vif_plug_noop/tests
%exclude %python3_sitelibdir/vif_plug_ovs/tests

%files tests
%python3_sitelibdir/os_vif/tests
%python3_sitelibdir/vif_plug_linux_bridge/tests
%python3_sitelibdir/vif_plug_noop/tests
%python3_sitelibdir/vif_plug_ovs/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt3.1
- Moved on modern pyproject macros.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt3
- Spec refactoring.

* Wed Oct 12 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt2
- Added manual.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.
- Unified (thx for felixz@).
- Built without check.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Automatically updated to 2.0.0.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.17.0-alt1
- Automatically updated to 1.17.0.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.15.1-alt1
- Updated to 1.15.1.
- Build without python2.

* Tue Dec 18 2018 Alexey Shabalin <shaba@altlinux.org> 1.11.1-alt1
- 1.11.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.1-alt1
- 1.4.1
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- Initial packaging
