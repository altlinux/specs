%define oname esutils

Name: python3-module-esutils
Version: 1.0.1
Release: alt1.gitce16f4e

Summary: esutils is utility box for ECMAScript language tools.

Url: https://github.com/0o120/esutils-python
License: BSD-2-Clause
Group: Development/Python3

# Source-url: https://github.com/0o120/esutils-python.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel) 
BuildRequires: python3(hatchling)

BuildArch: noarch

%description
%summary

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
* Tue Dec 02 2025 Ivan Mazhukin <vanomj@altlinux.org> 1.0.1-alt1.gitce16f4e
- Init build for ALT Sisyphus

