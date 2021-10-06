%define modname langdetect
%def_enable check

Name: python3-module-%modname
Version: 1.0.9
Release: alt1

Summary: Python3 language-detection library
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

Vcs: https://github.com/Mimino666/langdetect.git
Source: https://pypi.io/packages/source/l/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-six}

%description
Port of Nakatani Shuyo's language-detection library (version from
03/03/2014) to Python.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%python3_sitelibdir_noarch/*
%doc README* NOTICE

%changelog
* Wed Oct 06 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.9-alt1
- first build for Sisyphus




