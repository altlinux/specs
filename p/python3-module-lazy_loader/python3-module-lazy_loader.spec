%define modname lazy_loader
%def_enable check

Name: python3-module-%modname
Version: 0.2
Release: alt1

Summary: lazy_loader makes it easy to load subpackages and functions on demand
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/lazy_loader

Vcs: https://github.com/scientific-python/lazy_loader.git
Source: https://pypi.io/packages/source/l/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel python3-module-flit-core
%{?_enable_check:BuildRequires: python3(pytest-cov) python3(pre_commit)}

%description
%summary
See also https://scientific-python.org/specs/spec-0001/

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
/usr/bin/py.test3

%files
%python3_sitelibdir_noarch/*
%doc README* CHANGELOG*

%changelog
* Fri Mar 31 2023 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- 0.2

* Wed Feb 22 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus




