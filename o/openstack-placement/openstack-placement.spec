Name:    openstack-placement
Version: 2.0.0
Release: alt1

Summary: OpenStack resource provider inventory allocation service

License: ASL 2.0
Group:   Development/Python3
URL:     http://tarballs.openstack.org/os-resource-classes

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-pbr >= 2.0

BuildArch: noarch

Source:  %name-%version.tar

%description
OpenStack Placement provides an HTTP service for managing, selecting,
and claiming providers of classes of inventory representing available resources
in a cloud.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/*
%python3_sitelibdir/placement/
%python3_sitelibdir/placement_db_tools
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Thu Oct 17 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus.
