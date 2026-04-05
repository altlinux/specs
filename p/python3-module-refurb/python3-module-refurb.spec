%define _unpackaged_files_terminate_build 1

%define pypi_name refurb

%def_without check

Name: python3-module-%pypi_name
Version: 2.3.1
Release: alt1

Summary: tool for refurbishing and modernizing Python codebases
License: GPL-3.0
Group: Development/Python3
URL: https://github.com/dosisod/refurb

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(poetry)
BuildRequires: python3(poetry.core)

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
A tool for refurbishing and modernizing Python codebases. It can give 
hints on possible improvements and new features to use in an existing
Python codebase.
Refurb is not a style/type checker. It is not meant as a first-line of
defense for linting and finding bugs, it is meant for making good code
even better.

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
%doc LICENSE README.md docs
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%_bindir/%pypi_name

%changelog
* Sun Apr 05 2026 Nikolay Strelkov <snk@altlinux.org> 2.3.1-alt1
- New version 2.3.1.

* Sun Feb 22 2026 Nikolay Strelkov <snk@altlinux.org> 2.3.0-alt1
- New version 2.3.0.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 2.2.0-alt1
- New version 2.2.0.

* Sun Jun 22 2025 Nikolay Strelkov <snk@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
