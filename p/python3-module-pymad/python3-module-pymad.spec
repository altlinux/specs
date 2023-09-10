%define modname pymad
%def_enable check

Name: python3-module-%modname
Version: 0.11.3
Release: alt1

Summary: A Python wrapper for the MPEG Audio Decoder library
Group: Development/Python3
License: LGPL-2.0
Url: https://pypi.org/project/%modname

Vcs: https://github.com/jaqx0r/pymad.git
Source: https://pypi.io/packages/source/p/%modname/%modname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: libmad-devel
BuildRequires: python3(wheel) python3(setuptools_scm)
%{?_enable_check:BuildRequires: python3(pytest)}

%description
%summary

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 tests

%files
%python3_sitelibdir/*
%doc README*


%changelog
* Sun Sep 10 2023 Yuri N. Sedunov <aris@altlinux.org> 0.11.3-alt1
- 0.11.3
- ported to %%pyproject* macros
- enabled check

* Sat Jun 25 2022 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- first build for Sisyphus



