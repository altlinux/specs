%define modname pymad

Name: python3-module-%modname
Version: 0.10
Release: alt1

Summary: A Python wrapper for the MPEG Audio Decoder library
Group: Development/Python3
License: LGPL-2.0
Url: https://pypi.org/project/%modname

Source: https://pypi.io/packages/source/p/%modname/%modname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: libmad-devel
BuildRequires: python3-module-setuptools

%description
%summary

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
%doc README*


%changelog
* Sat Jun 25 2022 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- first build for Sisyphus



