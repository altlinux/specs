%define  modulename os-resource-classes

Name:    python3-module-%modulename
Version: 0.5.0
Release: alt1

Summary: A list of standardized resource classes for OpenStack

License: ASL 2.0
Group:   Development/Python3
URL:     http://tarballs.openstack.org/os-resource-classes

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-pbr >= 2.0

BuildArch: noarch

Source:  %modulename-%version.tar

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

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/os_resource_classes/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Thu Oct 17 2019 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus.
