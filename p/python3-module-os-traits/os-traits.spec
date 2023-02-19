%define oname os-traits
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 2.10.0
Release: alt1

Summary: OpenStack library containing standardized trait strings

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/os-traits

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0

%if_with check
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-testtools >= 2.2.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 0.8.0
BuildRequires: python3-module-openstackdocstheme
%endif

%description
Traits are strings that represent a feature of some resource provider.  This
library contains the catalog of constants that have been standardized in the
OpenStack community to refer to a particular hardware, virtualization, storage,
network, or device trait.

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

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/os_traits
%python3_sitelibdir/os_traits-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/os_traits/tests

%files tests
%python3_sitelibdir/os_traits/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 2.10.0-alt1
- Automatically updated to 2.10.0.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 2.9.0-alt1
- Automatically updated to 2.9.0.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1
- Automatically updated to 2.1.0.
- Added watch file.
- Renamed spec file.

* Wed Oct 23 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- new version 1.1.0
- Build without python2.

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 0.9.0-alt1
- Initial packaging
