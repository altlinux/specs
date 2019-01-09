%define oname os-traits

Name: python-module-%oname
Version: 0.9.0
Release: alt1
Summary: A library containing standardized trait strings
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-six >= 1.10.0

BuildRequires: python-module-sphinx
BuildRequires: python-module-reno >= 0.8.0
BuildRequires: python-module-openstackdocstheme

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 0.8.0
BuildRequires: python3-module-openstackdocstheme

%description
Traits are strings that represent a feature of some resource provider.  This
library contains the catalog of constants that have been standardized in the
OpenStack community to refer to a particular hardware, virtualization, storage,
network, or device trait.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
Documentation for OpenStack os-brick library

%package -n python3-module-%oname
Summary: A library containing standardized trait strings
Group: Development/Python3

%description -n python3-module-%oname
Traits are strings that represent a feature of some resource provider.  This
library contains the catalog of constants that have been standardized in the
OpenStack community to refer to a particular hardware, virtualization, storage,
network, or device trait.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

sed -i '/warning-is-error/d' setup.cfg

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files doc
%doc README.rst doc/build/html

%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%changelog
* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 0.9.0-alt1
- Initial packaging
