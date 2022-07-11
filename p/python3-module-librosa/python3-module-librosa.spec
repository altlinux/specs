%define modname librosa
# no tests
%def_disable check

Name: python3-module-%modname
Version: 0.9.1
Release: alt1

Summary: A python package for music and audio analysis
Group: Development/Python3
License: ISC
Url: https://pypi.org/project/%modname

Vcs: https://github.com/librosa/librosa.git
Source: https://pypi.io/packages/source/l/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools >= 48 python3-module-wheel >= 0.29

%description
%summary

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py check

%files
%python3_sitelibdir_noarch/*
%doc README*


%changelog
* Sat Jun 25 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- first build for Sisyphus



