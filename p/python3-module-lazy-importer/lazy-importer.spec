%define _unpackaged_files_terminate_build 1
%define pypi_name lazy-importer
%define mod_name lazy_importer

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.0
Release: alt1
Summary: A context manager for portable, opt-in lazy imports
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/lazy-importer
Vcs: https://github.com/pganssle/lazy_importer
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 10 2026 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1
- Initial build for sisyphus.
