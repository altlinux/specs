%define sname openstacksdk
%def_with python3

Name: python-module-%sname
Version: 0.9.8
Release: alt1
Summary: An SDK for building applications to work with OpenStack

Group: Development/Python
License: ASL 2.0
Url: http://developer.openstack.org/sdks/python/openstacksdk
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-stevedore >= 1.16.0
BuildRequires: python-module-os-client-config >= 1.13.1
BuildRequires: python-module-keystoneauth1 >= 2.10.0

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
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-stevedore >= 1.16.0
BuildRequires: python3-module-os-client-config >= 1.13.1
BuildRequires: python3-module-keystoneauth1 >= 2.10.0
%endif

%description
The python-openstacksdk is a collection of libraries for building applications to work with OpenStack clouds.
The project aims to provide a consistent and complete set of interactions
with OpenStack's many services, along with complete documentation, examples, and tools.

This SDK is under active development, and in the interests of providing a high-quality interface,
the APIs provided in this release may differ from those provided in future release.


%package doc
Summary: Documentation for OpenStack SDK
Group: Development/Documentation

%description doc
The python-openstacksdk is a collection of libraries for building applications to work with OpenStack clouds.
The project aims to provide a consistent and complete set of interactions 
with OpenStack's many services, along with complete documentation, examples, and tools.

This package contains auto-generated documentation.

%package -n python3-module-%sname
Summary: An SDK for building applications to work with OpenStack
Group: Development/Python3

%description -n python3-module-%sname
The python-openstacksdk is a collection of libraries for building applications to work with OpenStack clouds.
The project aims to provide a consistent and complete set of interactions 
with OpenStack's many services, along with complete documentation, examples, and tools.

This SDK is under active development, and in the interests of providing a high-quality interface,
the APIs provided in this release may differ from those provided in future release.


%prep
%setup

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

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

#export PYTHONPATH="$( pwd ):$PYTHONPATH"
#sphinx-build -b html doc/source html
#sphinx-build -b man doc/source man

# Fix hidden-file-or-dir warnings
#rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%python_sitelibdir/*

#%files doc
#%doc html

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 0.9.8-alt1
- initial build
