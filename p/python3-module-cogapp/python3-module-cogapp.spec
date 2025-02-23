%define _unpackaged_files_terminate_build 1
%define pypi_name cogapp

%def_with check

Name: python3-module-%pypi_name
Version: 3.4.1
Release: alt1

Summary: Small bits of Python computation for static files
License: MIT
Group: Development/Python3
URL: https://github.com/nedbat/cog

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Cog is a file generation tool. It lets you use pieces of Python code as
generators in your source files to generate whatever text you need.

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
%doc AUTHORS.txt README.rst
%_bindir/cog
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Feb 23 2025 Nikolay Strelkov <snk@altlinux.org> 3.4.1-alt1
- Initial build for Sisyphus
