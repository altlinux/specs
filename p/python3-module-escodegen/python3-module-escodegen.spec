%define oname escodegen

Name: python3-module-escodegen
Version: 1.0.11
Release: alt1.gita396adb

Summary: Escodegen is an ECMAScript code generator from Mozilla's Parser API AST

Url: https://github.com/0o120/escodegen-python
License: BSD-2-Clause
Group: Development/Python3

# Source-url: https://github.com/0o120/escodegen-python.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel) 
BuildRequires: python3(hatchling)

BuildArch: noarch

%description
Escodegen (escodegen) is an ECMAScript (also popularly known as JavaScript) code generator from 
Mozilla's Parser API AST. 

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Tue Dec 02 2025 Ivan Mazhukin <vanomj@altlinux.org> 1.0.11-alt1.gita396adb
- Init build for ALT Sisyphus

