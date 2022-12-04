Name: python3-module-gast
Version: 0.5.3
Release: alt1
Group: Development/Python3
Summary: Python AST that abstracts the underlying Python version
License: BSD
Url: https://github.com/serge-sans-paille/gast
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildArch: noarch

BuildRequires: python3-dev
BuildRequires: rpm-build-python3
BuildRequires: python3-module-wheel

%description 
A generic AST to represent Python2 and Python3's Abstract Syntax Tree (AST).
GAST provides a compatibility layer between the AST of various Python versions,
as produced by ast.parse from the standard ast module.

%prep
%setup
%patch0 -p1

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
* Sat Dec 03 2022 Anton Farygin <rider@altlinux.ru> 0.5.3-alt1
- first build for Sisyphus, based on specfile from Fedora
