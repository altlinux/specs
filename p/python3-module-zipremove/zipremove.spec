%define _unpackaged_files_terminate_build 1
%define pypi_name zipremove
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.10.0
Release: alt1
Summary: Extend `zipfile` with remove-related capabilities
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/zipremove
Vcs: https://github.com/danny0838/zipremove
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
%pyproject_configure_without_autodiscovery
%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0
%if_with check
# subpackaged in alt
BuildRequires: python3-test
%endif

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
%pyproject_run_unittest -v

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Nov 18 2026 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- Initial build for sisyphus.
