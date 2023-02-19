%define oname os-resource-classes
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 1.1.0
Release: alt1.1

Summary: Resource Classes for OpenStack

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/os-resource-classes

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-oslotest >= 1.10.0
BuildRequires: python3-module-stestr >= 1.0.0
BuildRequires: python3-module-testtools >= 1.4.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
%endif

%description
A list of standardized resource classes for OpenStack.
A resource class is a distinct type of inventory that exists in a cloud
environment, for example VCPU, DISK_GB. They are upper case with underscores.
They often include a unit in their name.
This package provides a collection of symbols representing those standard
resource classes which are expected to be available in any OpenStack deployment.
There also exists a concept of custom resource classes. These are countable
types that are custom to a particular environment. The OpenStack placement API
provides a way to create these. A custom resource class always begins with a
CUSTOM_ prefix.

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

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/os_resource_classes
%python3_sitelibdir/os_resource_classes-%version.dist-info
%exclude %python3_sitelibdir/os_resource_classes/tests

%files tests
%python3_sitelibdir/os_resource_classes/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1.1
- Moved on modern pyproject macros.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Automatically updated to 1.1.0.

* Thu Oct 17 2019 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus.
