%define oname os-service-types
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 1.7.0
Release: alt2.1

Summary: Python library for consuming OpenStack sevice-types-authority data

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/os-service-types

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0

%if_with check
BuildRequires: python3-module-hacking >= 1.1.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-six >= 1.10.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
%endif

%description
Python library for consuming OpenStack sevice-types-authority data

The OpenStack Service Types Authority contains information about official
OpenStack services and their historical service-type aliases.

The data is in JSON and the latest data should always be used. This simple
library exists to allow for easy consumption of the data, along with a built-in
version of the data to use in case network access is for some reason not
possible and local caching of the fetched data.

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
install -pDm 644 man/%oname.1 %buildroot%_man1dir/%oname.1
%endif

# Install missing file to proper location
cp os_service_types/data/service-types.json %buildroot%python3_sitelibdir/os_service_types/data

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/os_service_types
%python3_sitelibdir/os_service_types-%version.dist-info
%exclude %python3_sitelibdir/os_service_types/tests

%files tests
%python3_sitelibdir/os_service_types/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt2.1
- Moved on modern pyproject macros.

* Sat Oct 22 2022 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt2
- Unified.

* Wed Oct 23 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- new version 1.7.0.
- Build without python2.

* Mon Feb 11 2019 Alexey Shabalin <shaba@altlinux.org> 1.5.0-alt1
- 1.5.0

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt1
- Initial packaging
