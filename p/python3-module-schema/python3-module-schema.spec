%define modname schema

Name: python3-module-%modname
Version: 0.7.5
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
BuildRequires: python3-devel python3-module-setuptools

%description
%modname is a library for validating Python data structures, such as
those obtained from config-files, forms, external services or
command-line parsing, converted from JSON/YAML (or something else) to
Python data-types.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/*
%doc README*

%changelog
* Mon Dec 06 2021 Yuri N. Sedunov <aris@altlinux.org> 0.7.5-alt1
- 0.7.5

* Wed Mar 10 2021 Yuri N. Sedunov <aris@altlinux.org> 0.7.4-alt1
- 0.7.4

* Tue Jul 21 2020 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- first build for Sisyphus




