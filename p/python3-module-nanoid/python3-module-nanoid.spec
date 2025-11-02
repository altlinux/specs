%define _unpackaged_files_terminate_build 1

%define pypi_name nanoid

%def_without check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1

Summary: Python Nanoid
License: MIT
Group: Development/Python3
URL: https://github.com/puyuan/py-nanoid

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
A tiny, secure, URL-friendly, unique string ID generator for Python

* Safe. It uses cryptographically strong random APIs and tests
  distribution of symbols.
* Compact. It uses a larger alphabet than UUID (A-Za-z0-9_-).
  So ID size was reduced from 36 to 21 symbols.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Nov 02 2025 Nikolay Strelkov <snk@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
