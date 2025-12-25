%define oname esprima
%define pypi_name esprima2

Name: python3-module-%oname
Version: 5.0.1
Release: alt1

Summary: modern javascript parser

Url: https://pypi.org/project/esprima2/
License: BSD-2-Clause
Group: Development/Python3

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3-module-pytest

BuildArch: noarch

%description
esprima2 is a javascript parser written in python. It works for ECMAScript 2024 and has ~1500 unit tests

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%_bindir/%oname

%changelog
* Tue Dec 02 2025 Ivan Mazhukin <vanomj@altlinux.org> 5.0.1-alt1
- Init build for ALT Sisyphus

