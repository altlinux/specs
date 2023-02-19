%define oname oslo.upgradecheck
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 2.1.0
Release: alt1

Summary: OpenStack Common code for writing OpenStack upgrade checks

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.upgradecheck

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-upgradecheck = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-oslo.utils >= 4.5.0
BuildRequires: python3-module-oslo.policy >= 2.0.0

%if_with check
BuildRequires: python3-module-hacking >= 3.0
BuildRequires: python3-module-oslotest >= 3.5.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-oslo.serialization >= 2.21.1
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-openstackdocstheme >= 2.2.0
BuildRequires: python3-module-reno >= 3.1.0
BuildRequires: python3-module-sphinx >= 2.0.0
%endif

%description
This project contains the common code necessary for writing upgrade checks
in OpenStack projects. It includes a module for the common code as well as an
example of integrating that code into a project.

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
Provides: python3-module-oslo-upgradecheck-doc = %EVR

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
install -pDm 644 man/osloupgradecheck.1 %buildroot%_man1dir/osloupgradecheck.1
%endif

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/oslo_upgradecheck
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/oslo_upgradecheck/tests

%files tests
%python3_sitelibdir/oslo_upgradecheck/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/osloupgradecheck.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1
- Automatically updated to 2.1.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt3
- Spec refactoring.

* Wed Oct 12 2022 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt2
- Added manual.

* Wed Oct 05 2022 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Automatically updated to 2.0.0.
- Unified (thx for felixz@).

* Mon May 16 2022 Grigory Ustinov <grenka@altlinux.org> 1.5.0-alt1
- Automatically updated to 1.5.0.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Automatically updated to 1.0.1.
- Renamed spec file.

* Thu Sep 26 2019 Grigory Ustinov <grenka@altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus.
