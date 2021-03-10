%define modname cchardet
%def_enable check

Name: python3-module-%modname
Version: 2.1.7
Release: alt1

Summary: cChardet is high speed universal character encoding detector
Group: Development/Python3
License: GPL-2.0 and LGPL-2.1 and MPL-1.1
Url: https://pypi.org/project/%modname

#VCS: https://github.com/PyYoshi/cChardet.git
Source: https://pypi.io/packages/source/c/%modname/%modname-%version.tar.gz

Requires: uchardet

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ python3-devel python3-module-Cython python3-module-setuptools
%{?_enable_check:BuildRequires: python3-module-nose python3-module-chardet}

%description
cChardet is high speed universal character encoding detector - binding to
uchardet.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd src
%__python3 tests/test.py
#%%__python3 tests/bench.py
popd

%files
%_bindir/*
%python3_sitelibdir/*
%doc README*

%changelog
* Wed Mar 10 2021 Yuri N. Sedunov <aris@altlinux.org> 2.1.7-alt1
- 2.1.7

* Tue Jul 21 2020 Yuri N. Sedunov <aris@altlinux.org> 2.1.6-alt1
- first build for Sisyphus




