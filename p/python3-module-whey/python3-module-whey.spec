%define _unpackaged_files_terminate_build 1
%define pypi_name whey

# circular dependecy at tox-envlist
%def_without check

Name: python3-module-%pypi_name
Version: 0.0.23
Release: alt1

Summary: A simple Python wheel builder for simple projects
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/whey/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
A simple Python wheel builder for simple projects.

whey:

* supports PEP 621 metadata.

* can be used as a PEP 517 build backend.

* creates PEP 427 wheels.

* handles type hint files (py.typed and *.pyi stubs).

* is distributed under the MIT License.

* is the liquid remaining after milk has been curdled and strained.
  It is a byproduct of the manufacture of cheese and has several
  commercial uses.


%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE README.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.0.23-alt1
- initial build for Sisyphus

