%define modname odfpy
%def_disable check

Name: python3-module-odf
Version: 1.4.1
Release: alt1

Summary: Python3 library and utilities to manipulate OD-1.2 files
Group: Development/Python3
License: GPL-2.0 and Apache-2.0
Url: https://pypi.org/project/%modname

#VCS: https://github.com/pschmitt/pykeepass.git
Source: https://pypi.io/packages/source/o/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%{?_enable_check:BuildRequires: python3-module-tox python3-module-defusedxml}

%description
ODFPY is a collection of utility programs written in Python to manipulate
OpenDocument 1.2 files.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
tox.py3

%files
%_bindir/*
%python3_sitelibdir_noarch/*
%_man1dir/*
%doc README* ChangeLog


%changelog
* Thu Apr 09 2020 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- first build for Sisyphus




