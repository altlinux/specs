%define oname os-service-types

Name: python3-module-%oname
Version: 1.7.0
Release: alt1
Summary: Python library for consuming OpenStack sevice-types-authority data
Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0


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

%package doc
Summary: Documentation for OpenStack sevice-types-authority data
Group: Development/Documentation

%description doc
Documentation for the os-service-types library.

%prep
%setup -n %oname-%version
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%build
%python3_build

#python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
#rm -fr doc/build/html/.buildinfo

%install
%python3_install

#%check
#python setup.py test

#%if_with python3
#pushd ../python3
#python3 setup.py test
#popd
#%endif

%files
%doc ChangeLog CONTRIBUTING.rst PKG-INFO README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Wed Oct 23 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- new version 1.7.0.
- Build without python2.

* Mon Feb 11 2019 Alexey Shabalin <shaba@altlinux.org> 1.5.0-alt1
- 1.5.0

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt1
- Initial packaging
