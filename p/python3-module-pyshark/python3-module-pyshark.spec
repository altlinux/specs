%define _unpackaged_files_terminate_build 1

%def_with check

%define pypi_name pyshark

Name: python3-module-%pypi_name
Version: 0.6
Release: alt1

Summary: Python wrapper for tshark, allowing python packet parsing using wireshark dissectors
License: MIT
Group: Development/Python3

Url: https://github.com/KimiNewt/pyshark
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildArch: noarch

Requires: tshark

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: tshark
BuildRequires: python3(appdirs)
BuildRequires: python3(termcolor)
BuildRequires: python3(pytest)
BuildRequires: python3(mock)
BuildRequires: python3(lxml)
BuildRequires: python3(packaging)
%endif

%description
Python wrapper for tshark, allowing python packet parsing using wireshark dissectors.

%prep
%setup
%patch0 -p1

%build
cd src
%pyproject_build

%install
cd src
%pyproject_install

%check
cd src
%tox_check_pyproject

%files
%doc LICENSE.txt README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Sep 02 2023 Egor Ignatov <egori@altlinux.org> 0.6-alt1
- First build for ALT
