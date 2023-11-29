%define pypi_nname needly
%define _unpackaged_files_terminate_build 1

Name: python3-module-%pypi_nname
Version: 2.5.80
Release: alt1
Summary: Python Needle Editor for openQA
License: GPLv3 
Group: Development/Python
Url: https://pypi.org/project/needly/
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(poetry-core)

%description
Needly is an openQA needle editor written in Python.
It creates or modifies needles for the openQA tests.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%_bindir/%pypi_nname
#%%python3_sitelibdir/*
%python3_sitelibdir/%pypi_nname/
%python3_sitelibdir/%{pyproject_distinfo %pypi_nname}/

%changelog
* Tue Nov 28 2023 Mikhail Chernonog <snowmix@altlinux.org> 2.5.80-alt1
- Initial build for Sisyphus
