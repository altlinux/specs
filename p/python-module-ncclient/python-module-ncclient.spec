%define oname ncclient

Summary: Python library for NETCONF clients
Name: python-module-%oname
Version: 0.6.3
Release: alt1
Url: https://github.com/leopoul/ncclient
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: ASL 2.0
Group: Development/Python

BuildArch: noarch
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-paramiko >= 1.15.0
BuildRequires: python-module-lxml >= 3.3.0
BuildRequires: python-module-six


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-paramiko >= 1.15.0
BuildRequires: python3-module-lxml >= 3.3.0
BuildRequires: python3-module-six

%description
ncclient is a Python library that facilitates client-side scripting
and application development around the NETCONF protocol. ncclient
was developed by Shikar Bhushan. It is now maintained by Leonidas
Poulopoulos (@leopoul)

%package -n python3-module-%oname
Summary: Python library for NETCONF clients
Group: Development/Python3

%description -n python3-module-%oname
ncclient is a Python library that facilitates client-side scripting
and application development around the NETCONF protocol. ncclient
was developed by Shikar Bhushan. It is now maintained by Leonidas
Poulopoulos (@leopoul)



%prep
%setup

cp -fR . ../python3

%build
%add_optflags -fno-strict-aliasing
%python_build

pushd ../python3
%python3_build
popd

%install
%python_build_install --prefix=/usr

pushd ../python3
%python3_install --prefix=/usr
popd

%files
%doc Changelog LICENSE README README.md README.rst requirements.txt
%python_sitelibdir/*

%files -n python3-module-%oname
%doc Changelog LICENSE README README.md README.rst requirements.txt
%python3_sitelibdir/*

%changelog
* Thu Jan 10 2019 Alexey Shabalin <shaba@altlinux.org> 0.6.3-alt1
- 0.6.3
- build python3 package

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.2-alt1
- New version

* Fri Jun 10 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.7-alt1
- New version

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.3-alt1
- New version

* Thu Oct 30 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.2-alt1
- Initla build for ALT

