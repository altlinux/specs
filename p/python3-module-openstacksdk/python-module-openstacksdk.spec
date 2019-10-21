%define oname openstacksdk

Name: python3-module-%oname
Version: 0.36.0
Release: alt1
Summary: An SDK for building applications to work with OpenStack

Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-stevedore >= 1.17.1
BuildRequires: python3-module-keystoneauth1 >= 3.16.0
BuildRequires: python3-module-deprecation >= 1.0

%description
The python-openstacksdk is a collection of libraries for building applications to work with OpenStack clouds.
The project aims to provide a consistent and complete set of interactions
with OpenStack's many services, along with complete documentation, examples, and tools.

This SDK is under active development, and in the interests of providing a high-quality interface,
the APIs provided in this release may differ from those provided in future release.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack SDK
Group: Development/Documentation

%description doc
The python-openstacksdk is a collection of libraries for building applications to work with OpenStack clouds.
The project aims to provide a consistent and complete set of interactions 
with OpenStack's many services, along with complete documentation, examples, and tools.

This package contains auto-generated documentation.

%prep
%setup -n %oname-%version

# We handle requirements ourselves, pkg_resources only bring pain
rm -rf requirements.txt test-requirements.txt

# Remove bundled egg-info
#rm -rf *.egg-info

%build
%python3_build

%install
%python3_install

#export PYTHONPATH="$( pwd ):$PYTHONPATH"
#sphinx-build -b html doc/source html
#sphinx-build -b man doc/source man

# Fix hidden-file-or-dir warnings
#rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/openstack-inventory
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%doc examples
%python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/tests/functional/examples

%changelog
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
