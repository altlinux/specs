%define modname schema

Name: python3-module-%modname
Version: 0.7.7
Release: alt1

Summary: Simple data validation library
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

Vcs: https://github.com/keleshev/schema.git
Source: https://pypi.io/packages/source/s/%modname/%modname-%version.tar.gz

BuildArch: noarch

Requires: python3-module-contextlib2 >= 0.5.5

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)

%description
%modname is a library for validating Python data structures, such as
those obtained from config-files, forms, external services or
command-line parsing, converted from JSON/YAML (or something else) to
Python data-types.

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir_noarch/*
%doc README*

%changelog
* Sat May 04 2024 Yuri N. Sedunov <aris@altlinux.org> 0.7.7-alt1
- 0.7.7

* Mon Dec 06 2021 Yuri N. Sedunov <aris@altlinux.org> 0.7.5-alt1
- 0.7.5

* Wed Mar 10 2021 Yuri N. Sedunov <aris@altlinux.org> 0.7.4-alt1
- 0.7.4

* Tue Jul 21 2020 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- first build for Sisyphus




