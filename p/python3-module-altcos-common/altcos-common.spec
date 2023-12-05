%define pypi_name altcos-common
%define module_name altcos

%define common_requires ostree python3-module-pygobject3

%def_with check

Name:    python3-module-%pypi_name
Version: 3.0.0
Release: alt1

Summary: A library for convenient interaction with altcos repositories
License: MIT
Group:   Development/Python3
URL:     https://github.com/fl0pp5/altcos-common

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel %common_requires
Requires: %common_requires

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest tests/*

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name.py

%changelog
* Mon Sep 25 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 3.0.0-alt1
- 2.0.0 -> 3.0.0

* Fri Aug 25 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 2.0.0-alt1
- Initial build for ALT 

