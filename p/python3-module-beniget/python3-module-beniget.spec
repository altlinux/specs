Name: python3-module-beniget
Version: 0.4.1
Release: alt1
Group: Development/Python3
Summary: A static analyzer for Python code
License: BSD-3-Clause
Url: https://github.com/serge-sans-paille/beniget/
Source0: %name-%version.tar
BuildArch: noarch

BuildRequires: python3-dev
BuildRequires: rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-gast

%description 
Beniget provides a static over-approximation of the global and local definitions
inside Python Module/Class/Function. It can also compute def-use chains from
each definition.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Sun Dec 04 2022 Anton Farygin <rider@altlinux.ru> 0.4.1-alt1
- first build for Sisyphus
