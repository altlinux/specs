%define oname openstacksdk
%def_with python3

Name: python-module-%oname
Version: 0.9.13
Release: alt1.1
Summary: An SDK for building applications to work with OpenStack

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-stevedore >= 1.17.1
BuildRequires: python-module-os-client-config >= 1.22.0
BuildRequires: python-module-keystoneauth1 >= 2.18.0

# for build doc
BuildRequires: python-module-mock
BuildRequires: python-module-requests-mock
BuildRequires: python-module-fixtures
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-stevedore >= 1.17.1
BuildRequires: python3-module-os-client-config >= 1.22.0
BuildRequires: python3-module-keystoneauth1 >= 2.18.0
%endif

%description
The python-openstacksdk is a collection of libraries for building applications to work with OpenStack clouds.
The project aims to provide a consistent and complete set of interactions
with OpenStack's many services, along with complete documentation, examples, and tools.

This SDK is under active development, and in the interests of providing a high-quality interface,
the APIs provided in this release may differ from those provided in future release.

%package tests
Summary: Tests for %oname
Group: Development/Python
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

%package -n python3-module-%oname
Summary: An SDK for building applications to work with OpenStack
Group: Development/Python3

%description -n python3-module-%oname
The python-openstacksdk is a collection of libraries for building applications to work with OpenStack clouds.
The project aims to provide a consistent and complete set of interactions 
with OpenStack's many services, along with complete documentation, examples, and tools.

This SDK is under active development, and in the interests of providing a high-quality interface,
the APIs provided in this release may differ from those provided in future release.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

# We handle requirements ourselves, pkg_resources only bring pain
rm -rf requirements.txt test-requirements.txt

# Remove bundled egg-info
rm -rf *.egg-info

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

#export PYTHONPATH="$( pwd ):$PYTHONPATH"
#sphinx-build -b html doc/source html
#sphinx-build -b man doc/source man

# Fix hidden-file-or-dir warnings
#rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%doc examples openstack/tests/examples
%python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/tests/examples

#%files doc
#%doc html

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%doc examples openstack/tests/examples
%python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/tests/examples
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.13-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 0.9.13-alt1
- 0.9.13
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 0.9.8-alt1
- initial build
