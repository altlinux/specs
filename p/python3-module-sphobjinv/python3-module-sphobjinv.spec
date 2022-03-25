%define modname sphobjinv
# no tests defined
%def_disable check

Name: python3-module-%modname
Version: 2.2.2
Release: alt1

Summary: Sphinx objects.inv Inspection/Manipulation Tool
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

Vcs: https://github.com/bskinn/sphobjinv.git
#Source: https://pypi.io/packages/source/s/%modname/%modname-%version.tar.gz
Source: https://github.com/bskinn/%modname/archive/v%version/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%{?_enable_check:BuildRequires: python3-module-pytest}

%description
%summary

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3

%files
%_bindir/*
%python3_sitelibdir_noarch/*
%doc README* CHANGELOG*


%changelog
* Fri Mar 25 2022 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Sat Mar 05 2022 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Thu Apr 15 2021 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt1
- 2.1

* Sun Mar 07 2021 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- first build for Sisyphus




