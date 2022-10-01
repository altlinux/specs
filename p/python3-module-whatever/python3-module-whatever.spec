%define _unpackaged_files_terminate_build 1
%define pypi_name whatever

%def_with check

Name: python3-module-%pypi_name
Version: 0.6
Release: alt1

Summary: Easy anonymous functions by partial application of operators
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/whatever/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
An easy way to make lambdas by partial application of python operators.

Inspired by Perl 6 one, see http://perlcabal.org/syn/S02.html#The_Whatever_Object

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE CHANGELOG README.rst
%python3_sitelibdir/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 0.6-alt1
- initial build for Sisyphus

