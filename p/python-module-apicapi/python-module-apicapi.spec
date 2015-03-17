%define oname apicapi
%def_with python3

Name:       python-module-%oname
Version:    1.0.3
Release:    alt1
Summary:    Library for APIC REST api
License:    ASL 2.0
URL:       http://github.com/noironetworks/%oname
Source:    %name-%version.tar
Group:      Development/Python

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-oslo.config >= 1.4.0
BuildRequires: python-module-oslo.db >= 1.0.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-oslo.config >= 1.4.0
BuildRequires: python3-module-oslo.db >= 1.0.0
%endif

%description
There is a Python library provides an interface to the APIC REST api.

%if_with python3
%package -n python3-module-%oname
Summary: Library for APIC REST api
Group: Development/Python3

%description -n python3-module-%oname
There is a Python library provides an interface to the APIC REST api.
%endif

%prep
%setup

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

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
mv %buildroot%_bindir/apic-cleanup %buildroot%_bindir/python3-apic-cleanup
mv %buildroot%_bindir/apic-route-reflector %buildroot%_bindir/python3-apic-route-reflector
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/test
rm -fr %buildroot%python3_sitelibdir/*/test

%files
%doc AUTHORS README.rst
%_bindir/*
%exclude %_bindir/python3-*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%_bindir/python3-*
%python3_sitelibdir/*
%endif

%changelog
* Fri Mar 13 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- Initial release for Sisyphus

