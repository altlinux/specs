%define _unpackaged_files_terminate_build 1
%define pypi_name funcy

%def_with check

Name: python3-module-%pypi_name
Version: 1.17
Release: alt1

Summary: A fancy and practical functional tools
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/funcy/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(more_itertools)
BuildRequires: python3(whatever)
%endif

BuildArch: noarch

%description
A collection of fancy functional tools focused on practicality.

Inspired by clojure, underscore and my own abstractions.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE CHANGELOG README.rst TODO.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 1.17-alt1
- initial build for Sisyphus

