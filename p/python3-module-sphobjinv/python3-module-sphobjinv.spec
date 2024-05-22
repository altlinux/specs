%define modname sphobjinv
# network required
%def_disable check

Name: python3-module-%modname
Version: 2.3.1.1
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
BuildRequires: python3-module-wheel python3-module-setuptools
%{?_enable_check:BuildRequires: python3-module-tox python3(sphinx) python3(stdio_mgr)
BuildRequires: python3(dictdiffer) python3(jsonschema)}

%description
%summary

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%_bindir/*
%python3_sitelibdir_noarch/*
%doc README* CHANGELOG*


%changelog
* Wed May 22 2024 Yuri N. Sedunov <aris@altlinux.org> 2.3.1.1-alt1
- 2.3.1.1

* Thu Apr 20 2023 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Tue Nov 15 2022 Yuri N. Sedunov <aris@altlinux.org> 2.3-alt1
- 2.3
- ported to %%pyproject macros
- prepared %%check

* Fri Mar 25 2022 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Sat Mar 05 2022 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Thu Apr 15 2021 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt1
- 2.1

* Sun Mar 07 2021 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- first build for Sisyphus




